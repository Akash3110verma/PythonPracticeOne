class Employee:
    def __init__(self, employee_name, employee_id, designation, experience, age):
        self.employee_name = employee_name
        self.employee_id = employee_id
        self.designation = designation
        self.experience = experience
        self.age = age

    #print("emp table done")

    def get_emp_name(self):
        return self.employee_name
