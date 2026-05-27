from data.storage import get_connection
from models.employee import Employee
from exceptions.custom_exceptions import EmployeeNotFoundException
from utils.validator import validate_employee


class EmployeeService:

    @staticmethod
    def add_employee(emp_id, name, email):
        validate_employee(emp_id, name, email)

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("INSERT INTO employees VALUES (?, ?, ?)",
                       (emp_id, name, email))

        conn.commit()
        conn.close()

        return Employee(emp_id, name, email)

    @staticmethod
    def get_employee(emp_id):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM employees WHERE emp_id = ?", (emp_id,))
        row = cursor.fetchone()

        conn.close()

        if row is None:
            raise EmployeeNotFoundException("Employee not found")

        return Employee(*row)

    @staticmethod
    def list_employees():
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM employees")
        rows = cursor.fetchall()

        conn.close()

        return [Employee(*row) for row in rows]