class Employee:
    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary

    def give_raise(self, raise_amount=5000):
        self.salary += raise_amount
        return self.salary


