import sqlite3
import random
import string
import datetime
from datetime import date
from sqlite3 import Error
import re
 
def sql_connection():
    try:
        con = sqlite3.connect('NCRemployesdatabase.sql')
        return con
    except Error:
        print(Error)
con = sql_connection()
def sql_table(con):
    cursorObj = con.cursor()
 
    cursorObj.execute("CREATE TABLE IF NOT EXISTS employees(id integer PRIMARY KEY, name text, surname text, age integer, address text, department text, hireDate text, grade text, basic_salary real)")
    cursorObj.execute("CREATE TABLE IF NOT EXISTS registeration(Name text PRIMARY KEY, Email text, Password txt, Re_enter_password text)")
    con.commit()
 
sql_table(con)
 
def sql_insert(con, entities):
    cursorObj = con.cursor()
    cursorObj.execute('insert into employees(id, name, surname, age, address, department, hireDate, grade, basic_salary) Values (?,?,?,?,?,?,?,?,?)', entities)
    con.commit()
 
entity = [(1, 'Zeinab', 'Osman', 55, 'khartoum', 'science', '1995-1-23', 'Professor', 17387),
          (2, 'Ilham', 'Mohamed', 50, 'Bahari', 'adminstration','1997-8-2', 'Associate Professor', 15490),
          (3, 'Bothaina', 'Abdallah', 48, 'Umdurman', 'scientific Research','1997-11-20', 'Assistant Professor', 13800)
         ,(4, 'Ahmed', 'Awad', 45, 'khartoum', 'External Relation', '2000-3-4', 'Assistant Professor', 12294)
         ,(5, 'Asma', 'Ali', 40, 'Bahri', 'Training','2003-3-14', 'Technician', 10953)
         ,(6, 'Amani', 'Waleed', 38, 'Umdurman', 'HR', '2005-9-10', 'Technician assistant', 10450)
         ,(7, 'Intisar', 'Farah', 36, 'Bahri', 'Finance', '2006-6-2', 'Technician-1', 9758)
         ,(8, 'Eiman', 'Mohamed', 32, 'Burri Almahas', 'Statistic','2015-9-1', 'Technician assistant-1', 8694)        
         ,(9, 'Al samani', 'Tawfeg', 30, 'khartoum', 'stratigy & planning', '2016-7-8', 'Researcher Assistant', 7745)]
 
try:
    for entities in entity:
        sql_insert(con, entities)
except sqlite3.IntegrityError:
    pass
 
 
def sql_fetch(con):
    cursorObj = con.cursor()
    cursorObj.execute('SELECT id, name, basic_salary, hireDate FROM employees')
    rows = cursorObj.fetchall()
    for row in rows:
        print(row[0],row[1],MonthlySalary (row[2]))
        print('pay period ',PayPeriod(row[-1]))
        print('pay Ref', PayRef(row[0]))
    menu(con)
 
#add new Admin
def registeration(con,place):
        N = input("Enter your name: ")
        while not(N.isalpha()):
            print("invalid name")
            N = input("Enter Name: ")
        print('does not support outlook')
        E = input("Enter your Email: ")
        while not(E.endswith('@gmail.com') or E.endswith('@yahoo.com') or E.endswith('@hotmail.com')):
            print("invalid Email")
            E = input("Enter Email: ")
       
        P = input("Enter your password: ")
        Re_P = input("Re-enter your password: ")
        while P != Re_P:
            print("password doesn't match")
            P = input("Enter your password: ")
            Re_P = input("Re-enter your password: ")
        try:
            print("successfuly Registration")
            con.cursor().execute('insert into registeration(Name, Email, Password, Re_enter_password) Values (?,?,?,?)',(N, E, P, Re_P))
            con.commit()
        except sqlite3.IntegrityError:
            print('user already exist')
            registeration (con,place)
           
        if place == 'new':
            login(con)
        else:
            menu(con)
 
#add new employee
def employee(con):
    id = input('Enter id: ')
    while not id.isnumeric():
        print("invalid input")
        id = input("enter id: ")
    first_name = input('Enter First Name: ')
    while not first_name.isalpha():
        print("invalid first_name")
        first_name = input("Enter first name: ")          
    last_name = input('Enter Last Name: ')
    while not last_name.isalpha():
        print('invalid last Name')
        last_name = input('Enter Last Name: ')
    age = input('age: ')
    while not age.isnumeric():
        print("invalid age")
        age = input("age: ")
    while int(age)> 150:
        print('check the value enter')
        age = input("Enter age: ")
           
    address = input('address: ')
    department = input('department: ')
    while not department.isalpha():
        print("invalid input")
        department = input('department: ')
           
    hireDate = input("enter hireDate (yyyy-mm-dd): ")
    while not re.match(re.compile(r'^[0-9]{4}-[0-9]{2}-[0-9]{2}$'),hireDate):
        print("invalid input")    
        hireDate = input('enter date (yyyy-mm-dd): ')
           
    grade = input('grade: ')
    while not grade.isalpha():
        print("invalid input")
        grade = input('grade: ')
    basic_salary = input('basic sallary: ')
    while not basic_salary.isnumeric():
        print("invalid input")
        basic_salary = input('basi salary: ')
    try:
        sql_insert(con,(id,first_name,last_name,age,address,department,hireDate,grade,basic_salary))
        print('Record has been added')
        menu(con)
    except sqlite3.IntegrityError:
        print('ID taken, try another ID')
        employee(con)
               
def login(con):
    if(True):
        print(" Wellcome to the NCR Payroll Management System ")
        data = con.cursor().execute("SELECT name,password FROM registeration").fetchall()
        details = {}
        for i in data:
            details[i[0]] = i[1]
        username = input("Enter your name: ")
        password = input("Enter your password: ")
        if (username == 'admin' and password =='12345') or (username in details.keys() and details[username]==password):
            print('successful ')
            menu(con)
         
        else:
            print("You don't have an account, please register \n1. To register \n2.Exit")
            user_input= input('')
            while user_input !='1' and user_input != '2':
                user_input = input('Enter 1 or 2 ')
            if user_input =='1':
                registeration(con,'new')
                print('logging in...')
                menu(con)
            else:
                login(con)
 
def PayRef(id):
    Pay_Ref = "NCR" + "_" + str(id)
    #print('Pay Ref', Pay_Ref)
    return Pay_Ref
 
def PayPeriod(hireDate):
    today = date.today()
    pay_period = today - datetime.datetime.strptime(hireDate,'%Y-%m-%d').date()
    #print('pay period',pay_period)
    return pay_period.days
 
def MonthlySalary(basic_salary):
    BS = basic_salary
    OT = 0.5 * BS
    Health_insurance = 0.15 * BS
    cost_of_transportation = 0.22 * BS
 
    Total_income = (BS + OT + Health_insurance + cost_of_transportation)
    Income_Payment = "SDG", str('%.2f' %(Total_income))
    #print('Income Payment ',Income_Payment)
 
    tax = 0.2 * BS
    social_insurance = 0.16 * BS
    M_Pension = 0.026 * BS
 
    Total_deduction = (tax + social_insurance + M_Pension)
    Deduct_Payment = "SDG", str('%.2f' %(Total_deduction))
    #print('Deduct Payment ',Deduct_Payment)
 
    Net_Salary = (Total_income - Total_deduction)
    Net_Salary = str('%.2f'%(Net_Salary)) + " " + "SDG"
    return (Net_Salary)
 
def menu(con):
    print('Enter \n1. To Add New Admin in\n2. To Add New Employee \n3. Print Monthly Salary \n4. Logout')
    user_input = input()
    if user_input=='1':
        registeration(con,'menu')
        menu(con)
    elif user_input=='2':
        employee(con)
    elif user_input =='3':
        sql_fetch(con)
    elif user_input =='4':
        login(con)
    else:
        menu(con)
login(con)
con.close()