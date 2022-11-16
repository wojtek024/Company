import pandas as pd


class Employee:
    list_of_employees = []
    MIN_SALARY = 3000

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = int(salary)
        self.id = self.get_max_id() + 1
        Employee.list_of_employees.append(
            {'id': self.id, 'first_name': first_name, 'last_name': last_name, 'salary': salary})

    # dodawanie pracowników poprzez zaimportowanie pliku csv

    @classmethod
    def import_employees_from_file(cls, filename, *args, **kwargs):
        data = pd.read_csv(filename, *args, **kwargs)
        for index, row in data.iterrows():
            cls(row['first_name'], row['last_name'], row['salary'])

    def get_max_id(self):
        if len(Employee.list_of_employees) == 0:
            return 0
        else:
            return pd.DataFrame(Employee.list_of_employees)["id"].max()

    def give_raise(self, amount=0):
        self.salary = + amount

    @property
    def salary(self, new_salary):
        return self._salary

    @salary.setter
    def salary(self, new_salary):
        if new_salary < Employee.MIN_SALARY:
            raise ValueError("Invalid salary")
        else:
            self._salary = new_salary

    def __str__(self):
        emp_str = """
        Employee name: {first_name}
        Employee last name: {last_name}
        Employee salary: {salary}
        """.format(first_name=self.first_name, last_name=self.last_name, salary=self.salary)
        return emp_str

# Employee('Wojciech', 'Sajecki', 10000)
# Employee('Jan', 'Kowalski', 4652)
# Employee('Anna', "Nowak", 7896)
# Employee('Barbara', "Barwinek", 6354
