# from Employee import Employee
from src.Employee import Employee


class EmplooyeeManagementSystem:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee_name, employee_id, designation, experience, age):
        new_employee = Employee(
            employee_name, employee_id, designation, experience, age
        )
        self.employees.append(new_employee)
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

    def search_employee(self, emp_id):
        for employee in self.employees:
            if employee.employee_id == emp_id:
                return employee

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
            print(f"Employee '{deleted_employee.name}' with ID {employee_id} deleted.")
        except StopIteration:
            print(f"Employee Id not found")
