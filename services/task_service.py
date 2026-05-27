from data.storage import get_connection
from models.task import Task
from exceptions.custom_exceptions import TaskNotFoundException, EmployeeNotFoundException
from utils.validator import validate_task


class TaskService:

    @staticmethod
    def create_task(task_id, title, emp_id):
        validate_task(task_id, title)

        conn = get_connection()
        cursor = conn.cursor()

        # Check employee exists
        cursor.execute("SELECT * FROM employees WHERE emp_id = ?", (emp_id,))
        if cursor.fetchone() is None:
            raise EmployeeNotFoundException("Employee not found")

        cursor.execute("INSERT INTO tasks VALUES (?, ?, ?, ?)",
                       (task_id, title, emp_id, "Pending"))

        conn.commit()
        conn.close()

        return Task(task_id, title, emp_id)

    @staticmethod
    def update_task_status(task_id, status):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM tasks WHERE task_id = ?", (task_id,))
        if cursor.fetchone() is None:
            raise TaskNotFoundException("Task not found")

        cursor.execute("UPDATE tasks SET status = ? WHERE task_id = ?",
                       (status, task_id))

        conn.commit()
        conn.close()

    @staticmethod
    def list_tasks():
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM tasks")
        rows = cursor.fetchall()

        conn.close()

        return [Task(*row) for row in rows]