import pandas as pd
import getpass as gp
import time
import tabulate
from Employee import Employee
from Manager import Manager
from pandas.errors import EmptyDataError


class Program:
    def __init__(self):
        self.is_active = None
        self.employees = []

    def import_employees_from_file(self, filename, *args, **kwargs):
        try:
            data = pd.read_csv(filename, *args, **kwargs)
            for index, row in data.iterrows():
                emp = Employee(row['id'], row['first_name'], row['last_name'], row['salary'], row['position'])
                self.employees.append(emp)
        except EmptyDataError:
            print("Brak danych w pliku employees.csv")

    def log_in(self):
        self.import_employees_from_file('employees.csv')
        pwd = gp.getpass('Wpisz hasło: ')
        if pwd == 'Wojtek':
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
        if opcja_1 == '1':
            print('\n' * 20)
            print('Wybierz opcję:\na) Wyświetl informacje o pracownikach\nb) Dodaj pracownika\nc) Edytuj pracownika')
            opcja_2 = input()
            if opcja_2 == 'a' or opcja_2 == 'a)':
                print('\n' * 20)
                self.display_employees()
            elif opcja_2 == 'b' or opcja_2 == 'b)':
                print('\n' * 20)
                print('Dodaj pracownika')
                print("Wybierz rodzaj pracownika:\n1. Zwykły pracownik\n2. Menadżer")
                opcja_3 = input("Opcja: ")
                if opcja_3 == '1':
                    id = self.get_max_id() + 1
                    first_name = input("Podaj imię pracownika: ")
                    last_name = input("Podaj nazwisko pracownika: ")
                    salary = input("Podaj wysokość wynagrodzenia: ")
                    position = input("Podaj stanowisko pracownika: ")
                    try:
                        emp = Employee(id, first_name, last_name, salary, position)
                        self.employees.append(emp)
                        self.export_employees()
                    except ValueError:
                        print("Podano zbyt niskie wynagrodzenie. Wysokość miesięcznego wynagrodzenia powinno wynosić co "
                              "najmniej 3000. Pracownik nie został dodany do bazy.")
                elif opcja_3 == '2':
                    id = self.get_max_id() + 1
                    first_name = input("Podaj imię menadżera: ")
                    last_name = input("Podaj nazwisko menadżera: ")
                    salary = input("Podaj wysokość wynagrodzenia: ")
                    position = input("Podaj stanowisko pracownika: ")
                    try:
                        emp = Manager(id, first_name, last_name, salary, position)
                        self.employees.append(emp)
                        self.export_employees()
                    except ValueError:
                        print(
                            "Podano zbyt niskie wynagrodzenie. Wysokość miesięcznego wynagrodzenia powinno wynosić co "
                            "najmniej 3000. Pracownik nie został dodany do bazy.")
            elif opcja_2 == 'c' or opcja_2 == 'c)':
                print('\n' * 20)
                self.display_employees()
                employee_id = int(input("Wybierz id pracownika:"))
                if employee_id == '':
                    raise ValueError("Invalid employee id")
                else:
                    print('\n1. Zmień wysokość wynagrodzenia\n2. Zmień dane osobowe\n3. Przyznaj podwyżkę\n'
                          '4. Usuń pracownika z bazy danych')
                    opcja_4 = int(input("Wybierz opcję: "))

                    if opcja_4 == 1:
                        for e in self.employees:
                            if e.id == employee_id:
                                e.salary = int(input("Podaj nową wysokość wynagrodzenia: "))
                                self.export_employees()

                    elif opcja_4 == 2:
                        for e in self.employees:
                            if e.id == employee_id:
                                e.first_name = int(input("Podaj nowe imię: "))
                                e.last_name = int(input("Podaj nowe nazwisko: "))
                                self.export_employees()

                    elif opcja_4 == 3:
                        for e in self.employees:
                            if e.id != employee_id:
                                continue
                            e.give_raise(int(input("Podaj kwotę podwyżki: ")))
                            self.export_employees()

                    elif opcja_4 == 4:
                        self.delete_employee(employee_id)
                    else:
                        print('\nPodano złą cyfrę!')
                    # employee = Employee(employee_data)
            else:
                print("Podano złą literę!")
        elif opcja_1 == '2':
            print('Wylogowano!')
            self.is_active = False
            self.export_employees()
        else:
            return

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
