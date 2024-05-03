class Emp:
    def __init__(self, name, emp_id, designation, experience, age):
        self.name = name
        self.emp_id = emp_id
        self.designation = designation
        self.experience = experience
        self.age = age


class EMS:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def delete_employee(self, emp_id):
        self.employees = [emp for emp in self.employees if emp.emp_id != emp_id]

    def search_employee_by_id(self, emp_id):
        for emp in self.employees:
            if emp.emp_id == emp_id:
                return emp
        return None
    def search_employee_by_name(self, name):
        for emp in self.employees:
            if emp.name.lower() == name.lower():
                return emp