"""Load all doit-like tasks from notebooks."""
import json
import os
import traceback
from pathlib import Path

import importnb

HERE = Path(__file__).parent
IPYNB = sorted(HERE.glob("*.ipynb"))
SELF = bool(json.loads(os.environ.get("JPYK_SELF", "0")))


def register_tasks(stem, module, tasks, all_tasks):
    def _tasks():
        for name, task_fn in tasks.items():
            for subtask_dict in task_fn():
                subtask_name = subtask_dict["name"]
                subtask_dict["name"] = f"""{name.replace("task_", "")}:{subtask_name}"""
                if "doc" not in subtask_dict:
                    subtask_dict["doc"] = task_fn.__doc__
                yield subtask_dict

    _tasks.__name__ = f"""task_{"_".join(stem.split("_")[1:])}"""
    _tasks.__doc__ = module.__doc__
    all_tasks[_tasks.__name__] = _tasks


def load_tasks():
    all_tasks = {}
    modules = {}
    module_tasks = {}
    with importnb.Notebook():
        for ipynb in IPYNB:
            stem = ipynb.stem
            if ipynb.stem == "_self" and not SELF:
                continue
            try:
                with importnb.Notebook():
                    module = getattr(__import__(f"jupyak.tasks.{stem}").tasks, stem)
            except Exception as err:
                traceback.print_exception(err)
                print("!!!", ipynb)
                continue
            tasks = {
                name: task_fn
                for name, task_fn in module.__dict__.items()
                if name.startswith("task_")
            }
            if tasks:
                module_tasks[stem] = tasks
            modules[stem] = module

        for stem, module in module_tasks.items():
            if stem in module_tasks:
                register_tasks(stem, module, module_tasks[stem], all_tasks)

    return all_tasks
