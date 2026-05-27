class Task:
    def __init__(self, task_id, title, assigned_to, status="Pending"):
        self.task_id = task_id
        self.title = title
        self.assigned_to = assigned_to
        self.status = status

    def __str__(self):
        return f"{self.task_id} - {self.title} [{self.status}] Assigned to: {self.assigned_to}"