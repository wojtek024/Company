class Employee:
    MIN_SALARY = 3000

    def __init__(self, id, first_name, last_name, salary, position):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = int(salary)
        self.id = id
        self.position = position

    def __str__(self):
        emp_str = """
        Employee name: {first_name}
        Employee last name: {last_name}
        Employee salary: {salary}
        Employee position: {position}
        """.format(first_name=self.first_name, last_name=self.last_name, salary=self.salary, position=self.position)
        return emp_str

    def give_raise(self, amount=0):
        self.salary += amount

    def to_dict(self):
        emp_dict = {"id": self.id, "first_name": self.first_name, "last_name": self.last_name, "salary": self.salary,
                    "position": self.position}
        return emp_dict

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, new_salary):
        if new_salary < Employee.MIN_SALARY:
            raise ValueError("Invalid salary")
        else:
            self._salary = new_salary




