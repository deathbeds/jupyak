import datetime
import json
import os
import sys
import time
from io import StringIO
from pathlib import Path

import doit.reporter

os.environ.update(
    PYTHONUNBUFFERED="1",
    PIP_DISABLE_PIP_VERSION_CHECK="1",
    PYDEVD_DISABLE_FILE_VALIDATION="1",
    JPYK_SELF="1",
)

try:
    import jupyak
    from jupyak.tasks import load_tasks

    globals().update(load_tasks())
except ImportError as err:
    if "bootstrap" not in sys.argv:
        print(f"Please run `doit bootstrap` to get more tasks: {err}")

__all__ = ["tasks"]


def task_bootstrap():
    """# ensure a sane working environment."""
    history = []

    if not (E.RTD or E.BINDER or E.CI):
        history += [P.HISTORY]
        prefix = ["--prefix", P.ENV]

        if P.BINDER_LOCK.exists():
            yield dict(
                name="mamba:create",
                doc="> ensure the host environment is installed (from lockfile)",
                actions=[["mamba", "create", "-y", *prefix, "--file", P.BINDER_LOCK]],
                targets=history,
                file_dep=[P.BINDER_LOCK],
            )
        else:
            yield dict(
                name="mamba:update",
                doc="> ensure the host environment is installed (from loose env)",
                actions=[["mamba", "env", *prefix, "--update", P.ENV_YAML]],
                targets=history,
                file_dep=[P.ENV_YAML],
            )

    yield dict(
        name="pip",
        doc="> ensure the package-under-development is installed",
        actions=[[*C.CONDA_RUN, "--prefix", P.ENV, *C.PIP_E]],
        file_dep=[*history, P.PPT],
    )


class E:
    RTD = json.loads(os.environ.get("READTHEDOCS", "False").lower())
    BINDER = json.loads(os.environ.get("IN_BINDER", "False").lower())
    WORK_DIR = os.environ.get("JPYK_WORK_DIR", "work")
    LOG_NAME = os.environ.get("JPYK_LOG_NAME")
    CI = bool(json.loads(os.environ.get("CI", "0").lower()))


class P:
    DODO = Path(__file__)
    ROOT = DODO.parent
    BINDER = ROOT / ".binder"
    PPT = ROOT / "pyproject.toml"
    ENV_YAML = ROOT / ".binder/environment.yml"
    ENV = Path(sys.prefix if (E.CI or E.RTD or E.BINDER) else ROOT / ".venv")
    HISTORY = ENV / "conda-meta/history"
    LOGS = ROOT / E.WORK_DIR / "build/logs"
    BINDER_LOCK = BINDER / "conda-linux-64.lock"


class C:
    CONDA_RUN = ["conda", "run", "--no-capture-output"]
    PIP = ["python3", "-m", "pip"]
    PIP_E = [*PIP, "install", "-e", ".", "-vv", "--no-deps", "--no-build-isolation"]


class TaskResult:

    """result object used by JsonReporter"""

    # FIXME what about returned value from python-actions ?
    def __init__(self, task):
        self.task = task
        self.result = None  # fail, success, up-to-date, ignore
        self.out = None  # stdout from task
        self.err = None  # stderr from task
        self.error = None  # error from doit (exception traceback)
        self.started = None  # datetime when task execution started
        self.elapsed = None  # time (in secs) taken to execute task
        self._started_on = None  # timestamp
        self._finished_on = None  # timestamp

    def start(self):
        """Called when task starts its execution"""
        self._started_on = time.time()

    def set_result(self, result, error=None):
        """Called when task finishes its execution"""
        self._finished_on = time.time()
        self.result = result
        line_sep = "\n"
        self.out = line_sep.join([a.out for a in self.task.actions if a.out])
        self.err = line_sep.join([a.err for a in self.task.actions if a.err])
        self.error = error

    def to_dict(self):
        """Convert result data to dictionary"""
        if self._started_on is not None:
            started = datetime.datetime.utcfromtimestamp(self._started_on)
            self.started = str(started.strftime("%Y-%m-%d %H:%M:%S.%f"))
            self.elapsed = self._finished_on - self._started_on
        return {
            "name": self.task.name,
            "result": self.result,
            "out": self.out,
            "err": self.err,
            "error": self.error,
            "started": self.started,
            "elapsed": self.elapsed,
        }


class JsonReporter(doit.reporter.JsonReporter):
    def __init__(self, outstream, options=None):  # pylint: disable=W0613
        # options parameter is not used
        # json result is sent to stdout when doit finishes running
        self.t_results = {}
        # when using json reporter output can not contain any other output
        # than the json data. so anything that is sent to stdout/err needs to
        # be captured.
        self._old_out = sys.stdout
        sys.stdout = sys.stderr = StringIO()
        self._old_err = sys.stderr
        sys.stderr = StringIO()
        self.outstream = outstream
        # runtime and cleanup errors
        self.errors = []
        jupyak._STDOUT, jupyak._STDERR = sys.stdout, sys.stderr

    def get_status(self, task):
        """Called when task is selected (check if up-to-date)"""
        print(f"- {task.name}:", file=self._old_out, flush=True)
        self.t_results[task.name] = TaskResult(task)

    def skip_uptodate(self, task):
        """Skipped up-to-date task"""
        super().skip_uptodate(task)
        print("    - skip", file=self._old_out, flush=True)

    def skip_ignore(self, task):
        """Skipped ignored task"""
        super().skip_ignore(task)
        print("    - skip", file=self._old_out, flush=True)

    def add_success(self, task):
        """Called when execution finishes successfully"""
        super().add_success(task)
        print("    - ok", file=self._old_out, flush=True)

    def add_failure(self, task, exception):
        """Called when execution finishes with a failure"""
        print(exception.get_msg(), flush=True)
        print(exception.get_msg(), file=self._old_out, flush=True)
        super().add_failure(task, exception)

    def complete_run(self):
        """Called when finished running all tasks"""
        # restore stdout
        log_out = sys.stdout.getvalue()
        sys.stdout = self._old_out
        log_err = sys.stderr.getvalue()
        sys.stderr = self._old_err

        if self.errors:
            log_err += "\n".join(self.errors)

        task_result_list = []
        for tr in self.t_results.values():
            tr_dict = tr.to_dict()
            for split_field in ["out", "err"]:
                tr_dict[split_field] = tr_dict[split_field].splitlines(True)
            task_result_list += [tr_dict]
        json_data = {
            "tasks": task_result_list,
            "out": log_out.splitlines(True),
            "err": log_err.splitlines(True),
        }
        json.dump(json_data, self.outstream, indent=2, sort_keys=True)


if E.LOG_NAME:
    LOG_PATH = P.LOGS / f"{E.LOG_NAME}.json"
    print(f"Writing logs to {LOG_PATH}", flush=True)
    P.LOGS.mkdir(parents=True, exist_ok=True)
    DOIT_CONFIG = {
        "reporter": JsonReporter,
        "outfile": str(LOG_PATH),
    }
