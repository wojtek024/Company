import pandas as pd
import getpass as gp
import time
import tabulate
from Employee import Employee
from Manager import Manager


def export_employees():
    df = pd.DataFrame(Employee.list_of_employees)
    df.to_csv('employees.csv', header=True, index=False)


class Program:
    is_active = None

    def main_menu(self):
        print('\n1. Panel zarządzania pracownikami\n2. Wyloguj\n')
        opcja_1 = input('Wybierz opcję: ')
        if opcja_1 == '1':
            print('\n' * 20)
            print('Wybierz opcję:\na) Wyświetl informacje o pracownikach\nb) Dodaj pracownika\n'
                  'c) Edytuj pracownika\nd) Edytuj pracownika\ne) Inne')
            opcja_2 = input()
            if opcja_2 == 'a' or opcja_2 == 'a)':
                print('\n' * 20)
                self.display_employees()
            elif opcja_2 == 'b' or opcja_2 == 'b)':
                print('\n' * 20)
                print('Dodaj pracownika')
                first_name = input("Give first name: ")
                last_name = input("Give last name: ")
                salary = input("Give salary: ")
                Employee(first_name, last_name, salary)
                export_employees()
            elif opcja_2 == 'c' or opcja_2 == 'c)':
                print('\n' * 20)
                self.display_employees()
                employee_id = int(input("Wybierz id pracownika:"))
                if employee_id == '':
                    raise ValueError("Invalid employee id")
                else:
                    df_employees = pd.read_csv('employees.csv', header=0, index_col=0)
                    # employee_data = df_employees.loc[employee_id].tolist() -- jest coś źle
                    print('\n1. Zmień wysokość wynagrodzenia\n2. Zmień dane osobowe\n3. Przyznaj podwyżkę\n'
                          '4. Usuń pracownika z bazy danych')
                    opcja_3 = int(input("Wybierz opcję: "))

                    if opcja_3 == 1:
                        print('1')
                    elif opcja_3 == 2:
                        print('2')
                    elif opcja_3 == 3:
                        print('3')
                    elif opcja_3 == 4:
                        Employee.list_of_employees = [i for i in Employee.list_of_employees
                                                      if not (i['id'] == employee_id)]
                        export_employees()
                    else:
                        print('\nPodano złą cyfrę!')
                    # employee = Employee(employee_data)

            elif opcja_2 == 'd' or opcja_2 == 'd)':
                print('\n' * 20)
                self.display_employees()
                employee_id = input("Wybierz id pracownika:")
                if employee_id == '':
                    raise ValueError("Invalid employee id")
                else:
                    df_employees = pd.read_csv('employees.csv', header=0, index_col=0)
                    employee_data = df_employees.iloc[employee_id].tolist()
                    print('\n1. Zmień wysokość wynagrodzenia\n2. Zmień dane osobowe\n3. Przyznaj podwyżkę\n')
                    opcja_3 = input("Wybierz opcję: ")

                    if opcja_3 == 1:
                        print('1')
                    elif opcja_3 == 2:
                        print('2')
                    elif opcja_3 == 3:
                        print('3')
                    else:
                        print('\nPodano złą cyfrę!')
                    # employee = Employee(employee_data)
            elif opcja_2 == 'e' or opcja_2 == 'e)':
                print('\n' * 20)
                # print("Wybierz
                # give_raise(input("Podaj kwotę podwyżki: "))
                print('Podaj podwyżka')
            else:
                print("Podano złą literę!")
        elif opcja_1 == '2':
            print('Wylogowano!')
            Program.is_active = False
            export_employees()
        else:
            return

    def log_in(self):
        Employee.import_employees_from_file('employees.csv')
        pwd = gp.getpass('Wpisz hasło: ')
        if pwd == 'Wojtek':
            Program.is_active = True
            print('Zalogowano!')
            time.sleep(1.5)
            print('\n' * 20)
            while Program.is_active:
                self.main_menu()
        else:
            print('You entered wrong password')
            return

    def display_employees(self):
        print('Dostępni pracownicy:')
        df_employees = pd.read_csv('employees.csv', header=0, index_col=0)
        print(df_employees.to_markdown(tablefmt='grid'))

    def get_employees_df(self):
        df_employees = pd.read_csv('employees.csv', header=0, index_col=0)
        return df_employees

if __name__ == '__main__':
    # Employee('Wojciech', 'Sajecki', 10000)
    # Employee('Jan', 'Kowalski', 4652)
    # Employee('Anna', "Nowak", 7896)
    # Employee('Barbara', "Barwinek", 6354
    run = Program()
    run.log_in()
