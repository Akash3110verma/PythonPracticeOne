from src.Employee_management_system import EmplooyeeManagementSystem
from src.model.Employee import Employee
from src.model.Manager import Manager


def main():

    emps = EmplooyeeManagementSystem()

    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. Search Employee")
        print("3. Get all Employees")
        print("4. Validate Employee Details")
        print("5. Delete and Employee Record")
        print("6. Display Manager's Team")

        choice = input("Enter your choice: ")

        if choice == "1":
            emp_or_mng = input(
                "Do you want to add Developer press D or Manager press M"
            )
            if emp_or_mng.lower() == "d":
                employee_name = input("Enter employee name: ")
                designation = input("Enter employee designation: ")
                experience = int(input("Enter employee experience (in years): "))
                age = int(input("Enter employee age: "))
                new_employee = Employee(employee_name, designation, experience, age)
                emps.add_employee(new_employee)
            if emp_or_mng.lower() == "m":
                name = input("Enter manager name: ")
                experience = int(input("Enter Experience: "))
                age = int(input("Enter Age: "))
                new_mng = Manager(name, experience, age)
                emps.add_employee(new_mng)

        elif choice == "2":
            employee_name = input("Enter employee name to search ")
            details = emps.search_employee(employee_name)
            if not details:
                print("Employee not found")
            else:
                print(details)

        elif choice == "3":
            # employee_id = int(input("Enter employee ID to search "))
            # details = emps.get_employee_details(employee_id)
            print(emps.get_all_emp())

        elif choice == "4":
            employee_id = int(input("Enter employee ID to get details: "))
            details = emps.valid_employee_details(employee_id)
            print(details)

        elif choice == "5":
            while True:
                try:
                    employee_id = int(input("Enter employee ID to delete: "))
                    emps.delete_employee(employee_id)
                    break
                except ValueError:
                    print("Invalid input")

        elif choice == "6":
            manager_id = int(input("Enter manager ID to display team: "))
            manager = next(
                (mgr for mgr in emps.managers if mgr.employee_id == manager_id), None
            )
            if manager:
                manager.display_team()
            else:
                print(f"Manager with ID {manager_id} not found.")


if __name__ == "__main__":
    main()
