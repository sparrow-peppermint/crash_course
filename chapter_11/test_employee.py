import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.employee = Employee("Wilbur", "Peppermint", 50000)
        self.custom_raise = 8000

    def test_give_default_raise(self):
        new_salary = self.employee.give_raise()
        self.assertEqual(new_salary, 55000)

    def test_give_custom_raise(self):
        self.new_salary = self.employee.give_raise(raise_amount=self.custom_raise)
        self.assertEqual(self.new_salary, 58000)


if __name__ == '__main__':
    unittest.main()
