from src.model.Employee import Employee


class Manager(Employee):

    def __init__(self, name, experience, age, dsg = "manager"):
        super().__init__(name, dsg, experience, age)
        self.team = []

    # def add_employee_to_team(self, employee):
    #     self.team.append(employee)

    # def display_team(self):
    #     print(f"Manager {self.name}'s Team:")
    #     for employee in self.team:
    #         print(f"- {employee.name}")
