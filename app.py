import getpass as gp
from Employee import Employee
from Manager import Manager


def main_menu():

    pwd = gp.getpass('Wpisz hasło: ')
    if pwd == 'Wojtek':
        print('Zalogowano!')
        print('\n' * 2)
        print('1. Panel zarządzania pracownikami\n2. Wyloguj\n')
        opcja_1 = input('Wybierz opcję: ')
        if opcja_1 == '1':
            print('\n' * 20)
            print('Wybierz opcję:\na) wyświetl informacje o pracownikach\nb) Dodaj pracownika\n'
                  'c) Usuń pracownika\nd) Ustaw wysokość bonusu\ne) Przyznaj podwyżkę jednemu z pracowników')
            opcja_2 = input()
            if opcja_2 == 'a' or opcja_2 == 'a)':
                print('\n' * 20)
                print('pracownicy')
            elif opcja_2 == 'b' or opcja_2 == 'b)':
                print('\n' * 20)
                print('dodaj pracownika')
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
            print(2)
        else:
            return
    else:
        print('You entered wrong password')
        return


class Program():
    list_of_employees = []


if __name__ == '__main__':
    Employee('Wojciech', 'Sajecki', 10000)
    Employee('Jan', 'Kowalski', 4652)
    Employee('Anna', "Nowak", 7896)
    Employee('Barbara', "Barwinek", 6354


    while True:
        main_menu()


        # print('\n' * 20)
