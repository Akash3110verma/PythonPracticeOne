import unittest
from Emk_management import Emp, EMS

class TestEmployeeManagementSystem(unittest.TestCase):
    def setUp(self):
        self.emp1 = Emp("Barkha", 1, "Manager", 5, 30)
        self.emp2 = Emp("Harshdip", 2, "Developer", 3, 28)
        self.emp3 = Emp("Chaitali", 3, "Designer", 2, 25)
        self.emp_system = EMS()
        self.emp_system.add_employee(self.emp1)
        self.emp_system.add_employee(self.emp2)
        self.emp_system.add_employee(self.emp3)

    def test_add_employee(self):
        self.assertEqual(len(self.emp_system.employees), 3)
        new_emp = Emp("Soham", 4, "Analyst", 1, 24)
        self.emp_system.add_employee(new_emp)
        self.assertEqual(len(self.emp_system.employees), 4)

    def test_delete_employee(self):
        self.assertEqual(len(self.emp_system.employees), 3)
        self.emp_system.delete_employee(1)
        self.assertEqual(len(self.emp_system.employees), 2)
        self.assertIsNone(self.emp_system.search_employee_by_id(1))

    def test_search_employee_by_id(self):
        self.assertEqual(self.emp_system.search_employee_by_id(2), self.emp2)
        self.assertIsNone(self.emp_system.search_employee_by_id(4))

    def test_search_employee_by_name(self):
        self.assertEqual(self.emp_system.search_employee_by_name("Barkha"), self.emp1)
        self.assertIsNone(self.emp_system.search_employee_by_name("Soham"))


if __name__ == "__main__":
    unittest.main()