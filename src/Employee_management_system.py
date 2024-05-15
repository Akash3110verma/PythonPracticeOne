# from Employee import Employee
# import json
# from src.model.Employee import Employee
# from src.model.Manager import Manager
# from src.model.Project import Project
from src.helper.json_operation import JsonOperation

EMPLOYEE_PATH = (
    "C:/Users/amm927862/Desktop/pythonPractice/PythonPracticeOne/data/employees.json"
)


class EmplooyeeManagementSystem:
    def __init__(self):
        self.employees = []
        self.managers = []
        self.projects = []

    def add_employee(self, new_employee):
        self.employees.append(new_employee)
        new_emp = [
            {
                "Name": new_employee.get_emp_name(),
                "Degignation": new_employee.get_emp_designation(),
                "Id": new_employee.get_emp_id(),
                "Experience": new_employee.get_emp_experience(),
                "Age": new_employee.get_emp_age(),
            }
        ]

        val = JsonOperation.load_json_data(EMPLOYEE_PATH)
        new_emp = val + new_emp
        JsonOperation.dump_json_data(EMPLOYEE_PATH, new_emp)
        print("New Employee Added")

    def get_all_emp(self):
        for emp in self.employees:
            print()
            print(f"Employee Name: {emp.employee_name}")
            print(f"Employee ID: {emp.employee_id}")
            print(f"Employee degignation: {emp.designation}")
            print(f"Employee experience: {emp.experience}")
            print(f"Employee age: {emp.age}")
            print()

    def search_employee(self, emp_name):
        all_employee = JsonOperation.load_json_data(EMPLOYEE_PATH)
        for employee in all_employee:
            if employee.get("Name") == emp_name:
                return employee
        return None

    def valid_employee_details(self, employee_id: int) -> str:
        found_employee = self.search_employee(employee_id)
        if found_employee:
            return str(found_employee.employee_name)
        else:
            return f"Employee with ID {employee_id} not found."

    def delete_employee(self, employee_id):
        try:
            index_to_delete = next(
                i
                for i, employee in enumerate(self.employees)
                if employee.employee_id == employee_id
            )
            deleted_employee = self.employees.pop(index_to_delete)
            print(
                f"Employee '{deleted_employee.employee_name}' with ID {employee_id} deleted."
            )
        except StopIteration:
            print(f"Employee Id not found")

    def add_employee_to_manager(self, manager_id, employee):
        manager = next(
            (mgr for mgr in self.managers if mgr.employee_id == manager_id), None
        )
        if manager:
            manager.add_employee(employee)
            print(f"Employee '{employee.name}' added under Manager '{manager.name}'.")
        else:
            print(f"Manager with ID {manager_id} not found.")
