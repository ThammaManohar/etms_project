from exceptions.custom_exceptions import ValidationException

def validate_employee(emp_id, name, email):
    if not emp_id or not name:
        raise ValidationException("Employee ID and Name are required")

    if "@" not in email:
        raise ValidationException("Invalid email format")


def validate_task(task_id, title):
    if not task_id or not title:
        raise ValidationException("Task ID and Title are required")