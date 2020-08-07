import sqlite3     #    import sqlite3 module
import math

class Customers():  #   create a class Customers
    
    def __init__(self):
        print("WELCOME TO ASPIRE ELECTRICITY DISTRIBUTION COMPANY")
        self.conn = sqlite3.connect('AspireDb.db')  #   initialize connection to Aspiredb.db
        self.cursor = self.conn.cursor()    #   initialize cursor
        self.create_table() #   call method to create table
        self.user_input()   #   call method to obtain input from user
    
    def user_input(self):   #   create method to obtain user input
        print("ENTER (1) TO SIGN IN")   #   request user to move to sign in section
        print("ENTER (2) TO SIGN UP")   #   request user to move to sign up section
        print('> ')
        self.response = int(input())    #   variable to store user response
        if self.response == 2:  #   condition to check if user response is 2
            self.insert()   #   call insert method
        elif self.response == 1:    #   condition to check if user response is 1
            self.signin()   #   call signin method
        elif self.response not in [1,2]:    #   if user input is neither 1 or 2, instantiate the customer object and start afresh
            customer = Customers()
            
    def signin(self):   #   create the signin method
        with self.conn: #   establish connection to Aspire.db
            c_email = input("Enter Email: ")    #   request user to enter email
            c_password = input("Enter password: ")  #   request user to ennter password
            self.cursor.execute("SELECT email, password FROM customerdb WHERE email = ?", (c_email,))   #   sqlite3 statement to select email and password from the table customers where email is c_mail
            records = self.cursor.fetchone()    #   assign the email and password to records if it's in tables
            if records is not None:     #   check if c_mail in table
                db_email, db_password = records #   assign email and password to db_email and db_password respectively
                if c_email == db_email and c_password == db_password:   #   check email and password are correct
                    self.purchase() #   call the purchase method
                else:
                    print("incorrect password") #   print if password is incorrect
                    customer = Customers()  #   return to main section
            else:
                print("incorrect username") #   print if email isn't correct
                customer = Customers()  #   return to main section
        
    def commit(self):   #   commit method
        self.conn.commit()  #   this enables us to commit changes to databases
    
    def close(self):    #   close method
        self.conn.close()   #   this enables us to close database after committing chages
    
    def create_table(self): #   create table method to create method
        with self.conn: #   connect to Aspire database
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS customerdb(
                name text,
                email text,
                address text,
                mobile integer,
                password text,
                meter_no integer,
                units real,
                total_units real)""")   #   sqlite3 statement to create a table customerdb
        
        
    def insert(self):   #   insert method
        with self.conn:
            c_name = input("Enter Name: ")
            c_email = input("Enter email: ")
            c_address = input("Enter address: ")
            c_mobile = input("Enter telephone number: ")
            c_password = input("Enter password: ")
            c_meter_no = input("Enter meter number: ")
            c_units = ''
            c_total_units = 0
            
            if '@' in c_email: #    check if email exists
                self.cursor.execute("INSERT INTO customerdb VALUES(:name, :email, :address, :mobile, :password, :meter_no, :units, :total_units)",
                                    {'name': c_name,
                                    'email': c_email,
                                    'address': c_address,
                                    'mobile': c_mobile,
                                    'password': c_password,
                                    'meter_no': c_meter_no,
                                    'units': c_units,
                                    'total_units': c_total_units })   #   sqlite3 statement to insert user input to the table customerdb
            else:
                print("incorrect email")
        customer = Customers()
    
    def purchase(self): #   purchase method
        print("WELCOME TO THE PURCHASE SECTION")
        c_meter_no = input("Enter meter number: ")  #   request user meter's number
        with self.conn: #   connect to Aspiredb
            self.cursor.execute("SELECT meter_no, name, units, total_units from customerdb WHERE meter_no = ?",(c_meter_no,))   #   aqlite3 statement to select meter numbber and name where meter number is c_meter_no
            records = self.cursor.fetchone()    #   assign values to records
            if records is not None: #   check if c_meter_no in customerdb table
                db_meter_no, db_name, db_units, db_total_units = records  #   assign meter number name, units and total units to db_meter_no, db_name, db_units and db_total_units respectively
                # if c_meter_no == db_meter_no:
                c_acct_no = input("Enter account number: ")
                c_bank = input("Enter bank name: ")
                c_amount = int(input("Enter amount: "))
                c_units = round(c_amount/21.83, 2)
                c_total_units = db_total_units + c_units    #   add units bought to existing total units in database 
                with self.conn:
                
                    self.cursor.execute("UPDATE customerdb SET units=? WHERE meter_no=?", (c_units, db_meter_no))   #   update units to the current units bought
                    self.cursor.execute("UPDATE customerdb SET total_units=? WHERE meter_no=?", (c_total_units, db_meter_no))   #   add units bought to units in database
                
                print(f"Name: {db_name}")
                print(f"Meter number: {db_meter_no}")
                print(f"Amount paid: #{c_amount}")
                print(f"units bought: {c_units}")
                print("PURCHASE SUCCESSFUL!")
                print()
                input("press any key to ENTER to main menu")
                customer = Customers()
            else:
                print("INCORRECT METER NUMBER")
                customer = Customers()
                    
        

customer = Customers()
