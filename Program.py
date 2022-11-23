import getpass as gp
import time

import pandas as pd
from pandas.errors import EmptyDataError

from Employee import Employee
from Manager import Manager


class Program:
    def __init__(self):
        self.is_active = None
        self.employees = []

    def import_employees_from_file(self, filename, *args, **kwargs):
        try:
            data = pd.read_csv(filename, *args, **kwargs)
            for index, row in data.iterrows():
                if row['position'] == "Menadżer":
                    emp = Manager(row['id'], row['first_name'], row['last_name'], row['salary'], row['position'])
                else:
                    emp = Employee(row['id'], row['first_name'], row['last_name'], row['salary'], row['position'])
                self.employees.append(emp)
        except EmptyDataError:
            print("Brak danych w pliku employees.csv")

    def log_in(self):
        self.import_employees_from_file('employees.csv')
        pwd = gp.getpass('Wpisz hasło: ')
        if pwd == 'Company':
            self.is_active = True
            print('Zalogowano!')
            time.sleep(1)
            print('\n' * 20)
            while self.is_active:
                self.main_menu()
        else:
            print('You entered wrong password')
            return

    def main_menu(self):
        print('\n1. Panel zarządzania pracownikami\n2. Wyloguj\n')
        opcja_1 = input('Wybierz opcję: ')
        if opcja_1 == '1' or opcja_1 == "1.":
            print('\n' * 20)
            print('Wybierz opcję:\na) Wyświetl informacje o pracownikach\nb) Dodaj pracownika\nc) Edytuj pracownika')
            opcja_2 = input()
            if opcja_2 == 'a' or opcja_2 == 'a)':
                print('\n' * 20)
                self.display_employees()
            elif opcja_2 == 'b' or opcja_2 == 'b)':
                self.add_employee()
            elif opcja_2 == 'c' or opcja_2 == 'c)':
                print('\n' * 20)
                self.display_employees()
                employee_id = int(input("Wybierz id pracownika:"))
                if employee_id == '' or employee_id > self.get_max_id():
                    print("Podano nieprawidłowy numer identyfikacyjny pracownika!")
                else:
                    print('\n1. Zmień wysokość wynagrodzenia\n2. Zmień dane osobowe\n3. Przyznaj podwyżkę\n'
                          '4. Usuń pracownika z bazy danych\n5. Powrót do menu głównego')
                    opcja_4 = int(input("Wybierz opcję: "))
                    if opcja_4 == 1:
                        self.change_salary(employee_id)
                    elif opcja_4 == 2:
                        self.change_personal_data(employee_id)
                    elif opcja_4 == 3:
                        self.give_raise_to_employee(employee_id)
                    elif opcja_4 == 4:
                        self.delete_employee(employee_id)
                    elif opcja_4 == 5:
                        print("\n")
                    else:
                        print('\nPodano złą cyfrę!')
            else:
                print("Podano złą literę!")
        elif opcja_1 == '2' or opcja_1 == "2.":
            self.log_out()
        else:
            return

    def log_out(self):
        print('Wylogowano!')
        self.is_active = False
        self.export_employees()

    def add_employee(self):
        print('\n' * 20)
        print('Dodaj pracownika')
        print("Wybierz rodzaj pracownika:\n1. Zwykły pracownik\n2. Menadżer")
        opcja_3 = input("Opcja: ")
        if opcja_3 == '1':
            self.add_ordinary_employee()
        elif opcja_3 == '2':
            self.add_manager()

    def change_personal_data(self, employee_id):
        for e in self.employees:
            if e.id == employee_id:
                print('\n' * 2)
                e.first_name = int(input("Podaj nowe imię: "))
                e.last_name = int(input("Podaj nowe nazwisko: "))
                self.export_employees()

    def change_salary(self, employee_id):
        for e in self.employees:
            if e.id == employee_id:
                print('\n' * 2)
                e.salary = int(input("Podaj nową wysokość wynagrodzenia: "))
                self.export_employees()

    def add_ordinary_employee(self):
        print('\n' * 20)
        id = self.get_max_id() + 1
        first_name = input("Podaj imię pracownika: ")
        last_name = input("Podaj nazwisko pracownika: ")
        salary = input("Podaj wysokość wynagrodzenia: ")
        position = "Pracownik"
        try:
            emp = Employee(id, first_name, last_name, salary, position)
            self.employees.append(emp)
            self.export_employees()
            print("Pracownik został poprawnie dodany do bazy!")
        except ValueError:
            print("Podano zbyt niskie wynagrodzenie. Wysokość miesięcznego wynagrodzenia powinno wynosić co"
                  " najmniej 3000. Pracownik nie został dodany do bazy.")

    def add_manager(self):
        print('\n' * 20)
        id = self.get_max_id() + 1
        first_name = input("Podaj imię menadżera: ")
        last_name = input("Podaj nazwisko menadżera: ")
        salary = input("Podaj wysokość wynagrodzenia: ")
        position = "Menadżer"
        try:
            emp = Manager(id, first_name, last_name, salary, position)
            self.employees.append(emp)
            self.export_employees()
            print("Pracownik został poprawnie dodany do bazy!")
        except ValueError:
            print(
                "Podano zbyt niskie wynagrodzenie. Wysokość miesięcznego wynagrodzenia powinno wynosić co "
                "najmniej 3000. Pracownik nie został dodany do bazy.")

    def give_raise_to_employee(self, employee_id):
        for e in self.employees:
            if e.id != employee_id:
                continue
            print('\n' * 2)
            if e.position == "Menadżer":
                e.give_raise(int(input("Podaj kwotę podwyżki: ")), float(input("Podaj wysokość bonusu (w zakresie 0-1): ")))
                self.export_employees()
            else:
                e.give_raise(int(input("Podaj kwotę podwyżki: ")))
                self.export_employees()

    def export_employees(self):
        list_of_dict = [o.to_dict() for o in self.employees]
        df = pd.DataFrame(list_of_dict)
        df.to_csv('employees.csv', header=True, index=False)

    def display_employees(self):
        print('Dostępni pracownicy:')
        df_employees = self.get_employees_df()
        print(df_employees.to_markdown(tablefmt='grid'))

    def get_employees_df(self):
        df_employees = pd.read_csv('employees.csv', header=0, index_col=0)
        return df_employees

    def delete_employee(self, employee_id):

        self.employees = [i for i in self.employees if not (i.id == employee_id)]
        self.export_employees()

    def get_max_id(self):
        if len(self.employees) == 0:
            return 0
        else:
            list_of_dict = [o.to_dict() for o in self.employees]
            df = pd.DataFrame(list_of_dict)
            return df["id"].max()


if __name__ == '__main__':
    run = Program()
    run.log_in()
