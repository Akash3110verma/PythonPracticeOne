from src.Employee import Employee


class Manager(Employee):

    def __init__(self, name, designation, experience, age):
        super().__init__(name, designation, experience, age)
        self.team = []

    def add_employee_to_team(self, employee):
        self.team.append(employee)

    def display_team(self):
        print(f"Manager {self.name}'s Team:")
        for employee in self.team:
            print(f"- {employee.name}")
