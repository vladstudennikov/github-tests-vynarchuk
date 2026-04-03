import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from service import TaskService

def test_add_task_success():
    service = TaskService()
    service.add_task("Test task")

    tasks = service.get_tasks()
    assert len(tasks) == 1
    assert tasks[0].title == "Test task"


def test_add_task_empty():
    service = TaskService()

    with pytest.raises(ValueError):
        service.add_task("")


def test_add_task_too_short():
    service = TaskService()

    with pytest.raises(ValueError):
        service.add_task("ab")