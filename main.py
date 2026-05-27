from services.employee_service import EmployeeService
from services.task_service import TaskService
from data.storage import create_tables, reset_tables


def main():
    #  Initialize DB and reset data
    create_tables()
    reset_tables()

    #  Add Employees
    EmployeeService.add_employee(1, "Manohar", "manohar@gmail.com")
    EmployeeService.add_employee(2, "Rahul", "rahul@gmail.com")
    EmployeeService.add_employee(3, "Anita", "anita@gmail.com")
    EmployeeService.add_employee(4, "Kiran", "kiran@gmail.com")
    EmployeeService.add_employee(5, "Sneha", "sneha@gmail.com")

    print("=== Employees ===")
    for emp in EmployeeService.list_employees():
        print(emp)

    #  Create Tasks
    TaskService.create_task(101, "Prepare Report", 1)
    TaskService.create_task(102, "Data Analysis", 2)
    TaskService.create_task(103, "Dashboard Creation", 3)
    TaskService.create_task(104, "Client Presentation", 4)
    TaskService.create_task(105, "Model Training", 1)
    TaskService.create_task(106, "Data Cleaning", 2)
    TaskService.create_task(107, "Requirement Gathering", 5)

    print("\n=== Tasks (Before Update) ===")
    for task in TaskService.list_tasks():
        print(task)

    #  Update Task Status
    TaskService.update_task_status(101, "Completed")
    TaskService.update_task_status(103, "In Progress")
    TaskService.update_task_status(106, "Completed")

    print("\n=== Tasks (After Update - With Employee Names) ===")

    #  Using JOIN
    for row in TaskService.list_tasks_with_employee():
        task_id, title, status, name = row
        print(f"{task_id} - {title} [{status}] Assigned to: {name}")


if __name__ == "__main__":
    main()