import pandas as pd
import getpass as gp
from Employee import Employee
from Manager import Manager


def export_employees():
    df = pd.DataFrame(Employee.list_of_employees)
    df.to_csv('employees.csv', header=True)


class Program:
    is_active = None

    def main_menu(self):
        print('1. Panel zarządzania pracownikami\n2. Wyloguj\n')
        opcja_1 = input('Wybierz opcję: ')
        if opcja_1 == '1':
            print('\n' * 20)
            print('Wybierz opcję:\na) Wyświetl informacje o pracownikach\nb) Dodaj pracownika\n'
                  'c) Usuń pracownika\nd) Ustaw wysokość bonusu\ne) Przyznaj podwyżkę jednemu z pracowników')
            opcja_2 = input()
            if opcja_2 == 'a' or opcja_2 == 'a)':
                print('\n' * 20)
                print('pracownicy')
                print(Employee.list_of_employees)
            elif opcja_2 == 'b' or opcja_2 == 'b)':
                print('\n' * 20)
                print('dodaj pracownika')
                first_name = input("Give first name: ")
                last_name = input("Give last name: ")
                salary = input("Give salary: ")
                Employee(first_name, last_name, salary)
            elif opcja_2 == 'c' or opcja_2 == 'c)':
                print('\n' * 20)
                print('usuń pracownika')
            elif opcja_2 == 'd' or opcja_2 == 'd)':
                print('\n' * 20)
                print('bonus')
            elif opcja_2 == 'e' or opcja_2 == 'e)':
                print('\n' * 20)
                print('podwyżka')
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
            print('\n' * 20)
            while Program.is_active:
                self.main_menu()
        else:
            print('You entered wrong password')
            return



if __name__ == '__main__':
    # Employee('Wojciech', 'Sajecki', 10000)
    # Employee('Jan', 'Kowalski', 4652)
    # Employee('Anna', "Nowak", 7896)
    # Employee('Barbara', "Barwinek", 6354
    run = Program()
    run.log_in()
