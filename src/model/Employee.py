import random
import string
import enum

# class Designation:


class Employee:
    def __init__(self, employee_name, designation, experience, age):
        self.employee_name = employee_name
        self.employee_id = self._generate_id()
        self.designation = designation
        self.experience = experience
        self.age = age

    # print("emp table done")

    # def assign_employee_id(self, employee_id):
    #     self.employee_id = employee_id

    def get_emp_name(self):
        return self.employee_name

    def get_emp_id(self):
        return self.employee_id

    def get_emp_designation(self):
        return self.designation

    def get_emp_experience(self):
        return self.experience

    def get_emp_age(self):
        return self.age

    def _generate_id(self):
        """This will generate id to employee"""
        return "".join(random.choices(string.ascii_lowercase, k=6))
