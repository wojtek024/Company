# Company
Repository contains "company" python project.
The aim of the project was to create a progam to simulate the human resources management of a small company. The aim of the project was to create a progam to simulate the human resources management of a small company.
The programme uses the object-oriented programming paradigm.
The programme wa created using python 3.9.13

Programme useage instruction:

1. To run the programme, install all packages listed in the file "requirements.txt" (pip install -r requirements.txt)

2. Then run the file "Programm.py" in terminal. (python Programm.py)

3. Enter the password: "Company" and press Enter to log in.

4. Then you will be in the main menu. You can choose whether you want to go to the management panel or to log out.
To choose the option enter the number of option and press Enter.


### Types of employees ###

1) Ordinary employee
    * Attributes:
      * First Name
      * Last Name
      * Salary
      * Position (='Pracownik')
    * Methods:
      * give_raise - give raise to the employee in the amount specified by the user
    
2) Manager
    * Attributes:
      * First Name
      * Last Name
      * Salary
      * Position (='Menadżer')
    * Methods:
      * give_raise - give raise to the employee in the amount specified by the user and adds also previuos salary multiplied by bonus (also set by the user)
