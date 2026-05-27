class Employee:
    def __init__(self, emp_id, name, email):
        self.emp_id = emp_id
        self.name = name
        self.email = email

    def __str__(self):
        return f"{self.emp_id} - {self.name} ({self.email})"