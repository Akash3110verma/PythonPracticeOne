from src.Employee_management_system import EmplooyeeManagementSystem
from src.Employee import Employee

# from PythonPracticeOne.src.Employee_management_system import EmplooyeeManagementSystem


def main():

    emps = EmplooyeeManagementSystem()

    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. Search Employee")
        print("3. Get all Employees")
        print("4. Validate Employee Details")
        print("5. Delete and Employee Record")

        choice = input("Enter your choice: ")

        if choice == "1":
            employee_name = input("Enter employee name: ")
            employee_id = int(input("Enter employee ID: "))
            designation = input("Enter employee designation: ")
            experience = int(input("Enter employee experience (in years): "))
            age = int(input("Enter employee age: "))
            emps.add_employee(employee_name, employee_id, designation, experience, age)

        elif choice == "2":
            employee_id = int(input("Enter employee ID to search "))
            details = emps.get_employee_details(employee_id)
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


if __name__ == "__main__":
    main()
