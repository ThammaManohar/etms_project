from data.storage import tasks_db, employees_db
from models.task import Task
from exceptions.custom_exceptions import TaskNotFoundException, EmployeeNotFoundException
from utils.validator import validate_task


class TaskService:

    @staticmethod
    def create_task(task_id, title, emp_id):
        validate_task(task_id, title)

        if emp_id not in employees_db:
            raise EmployeeNotFoundException("Employee not found")

        task = Task(task_id, title, emp_id)
        tasks_db[task_id] = task
        return task

    @staticmethod
    def update_task_status(task_id, status):
        if task_id not in tasks_db:
            raise TaskNotFoundException("Task not found")

        tasks_db[task_id].status = status
        return tasks_db[task_id]

    @staticmethod
    def list_tasks():
        return list(tasks_db.values())