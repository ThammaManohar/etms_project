from services.employee_service import EmployeeService
from services.task_service import TaskService


def main():
    # Add Employees
    EmployeeService.add_employee(1, "Manohar", "manohar@gmail.com")
    EmployeeService.add_employee(2, "Rahul", "rahul@gmail.com")

    print("Employees:")
    for emp in EmployeeService.list_employees():
        print(emp)

    # Create Tasks
    TaskService.create_task(101, "Prepare Report", 1)
    TaskService.create_task(102, "Data Analysis", 2)

    print("\nTasks:")
    for task in TaskService.list_tasks():
        print(task)

    # Update Task Status
    TaskService.update_task_status(101, "Completed")

    print("\nUpdated Tasks:")
    for task in TaskService.list_tasks():
        print(task)


if __name__ == "__main__":
    main()