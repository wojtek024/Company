from Employee import Employee


class Manager(Employee):
    def __init__(self, first_name, last_name, salary, project=None):
        Employee.__init__(self, first_name, last_name, salary)
        self.project = project