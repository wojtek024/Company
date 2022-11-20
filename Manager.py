from Employee import Employee


class Manager(Employee):
    def give_raise(self, amount=0, bonus = 0):
        self.salary = (self.salary + amount) + (self.salary * bonus)
