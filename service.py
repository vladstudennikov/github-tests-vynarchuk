from models import TaskItem
from validator import validate_title

class TaskService:
    def __init__(self):
        self.tasks = []

    def add_task(self, title: str):
        print(f"[LOG] Adding task: {title}")
        validate_title(title.strip())
        task = TaskItem(title.strip())
        self.tasks.append(task)
        print("[LOG] Task successfully added")

    def get_tasks(self):
        return self.tasks