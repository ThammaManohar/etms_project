from data.storage import employees_db
from models.employee import Employee
from exceptions.custom_exceptions import EmployeeNotFoundException
from utils.validator import validate_employee


class EmployeeService:

    @staticmethod
    def add_employee(emp_id, name, email):
        validate_employee(emp_id, name, email)

        emp = Employee(emp_id, name, email)
        employees_db[emp_id] = emp
        return emp

    @staticmethod
    def get_employee(emp_id):
        if emp_id not in employees_db:
            raise EmployeeNotFoundException("Employee not found")

        return employees_db[emp_id]

    @staticmethod
    def list_employees():
        return list(employees_db.values())