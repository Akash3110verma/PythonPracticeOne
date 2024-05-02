from Emk_management import Emp, EMS

# Example usage
emp_system = EMS()
emp1 = Emp("Barkha", 1, "Manager", 5, 30)
emp2 = Emp("Harshdip", 2, "Developer", 3, 28)
emp3 = Emp("Chaitali", 3, "Designer", 2, 25)

emp_system.add_employee(emp1)
emp_system.add_employee(emp2)
emp_system.add_employee(emp3)

print("Employees in the system:")
for emp in emp_system.employees:
    print(f"{emp.name}, {emp.emp_id}, {emp.designation}, {emp.experience}, {emp.age}")