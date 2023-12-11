import importnb
import pytest


@pytest.fixture()
def a_yak():
    with importnb.Notebook():
        from jupyak.tasks._yak import Yak
    from jupyak.tasks import load_tasks

    load_tasks()

    yak = Yak()
    return yak


def test_yak_repo_counts(a_yak):
    """Check the number of managed repos."""
    repo_counts = (len(a_yak.repos), len(a_yak.py_repos), len(a_yak.js_repos))
    assert repo_counts == (22, 21, 7)
