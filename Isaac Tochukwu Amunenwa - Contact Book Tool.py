from tkinter import *
import tkinter.messagebox as tkMessageBox
import sqlite3
import re
import csv


#####################################################################################
# The code snippet below create a GUI main or parent window via the tkinter module  #
# then configures the title, background , size.                                     #
#####################################################################################
root = Tk()
root.title("ConCloud: Contact Book Tool")
root.configure(background = "AliceBlue")

root.attributes('-fullscreen', False)


#Regular Expression for validation of Email
reg = r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
emails = re.compile(reg)


#=======================================VARIABLES=====================================
# Variables that will be used to collect inputs from the user via the GUI application 
username = StringVar()
password = StringVar()
first_name = StringVar()
last_name = StringVar()
email = StringVar()

name = StringVar()
address = StringVar()
phone_number = StringVar()
email_address = StringVar()


#=======================================METHODS=======================================
def database():
    """
    This function creates an sqlite3 database 'contact_book_db.sqlite' through the sqlite3 
    module then creates the 'users' and 'contacts' table. The 'users' table stores the 
    registration/login details like the name, username, password, email address etc while 
    the 'contacts' table store the contacts associated to each user via a foreign key which is 
    the id of the user.
    """
    global conn, cursor

    #Creates the database
    conn = sqlite3.connect("contact_book_db.sqlite")

    #Connects to the database to enable it perform some operation
    cursor = conn.cursor()

    #Creates the 'users' table
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT NOT NULL, password TEXT NOT NULL, first_name NOT NULL, last_name TEXT NOT NULL, email TEXT NOT NULL)")

    #Creates the 'contacts' table 
    cursor.execute("CREATE TABLE IF NOT EXISTS contacts (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, name TEXT NOT NULL, address TEXT, phone_number TEXT NOT NULL, email_address TEXT, user_id INTEGER NOT NULL, FOREIGN KEY (user_id) REFERENCES users (id))")

def quit():
    """
    Function that terminates the GUI application entirely if the user clicks 'yes' 
    when a prompt is shown.
    """
    result = tkMessageBox.askquestion('System', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        root.destroy()
        exit()


def login_form():
    """ 
    Displays the Login form for the User to Login into their Account if created.
    The LoginFrame and lbl_result1 are global variables because they are used in 
    other functions
    """
    global LoginFrame, lbl_result1

    #Creates another frame LoginFrame for the login form from the main frame - root
    LoginFrame = Frame(root, bg = "AliceBlue", highlightbackground="Grey",  highlightcolor = "Grey", highlightthickness = 5, width = 100, height = 100, bd= 0)
    LoginFrame.pack(side=TOP, pady=80, expand = True)

    #Creates the username label in form of a button then positions it using the grid function
    lbl_username = Button(LoginFrame, text="Username", font=('arial', 18))
    lbl_username.grid(row=2, padx = 20)

    #Creates the password label in form of a button then positions it using the grid function
    lbl_password = Button(LoginFrame, text="Password", font=('arial', 18), width = 9)
    lbl_password.grid(row=3, padx = 20)

    #A label that outputs any notification if there is any
    lbl_result1 = Label(LoginFrame, text="", font=('arial', 18))
    lbl_result1.grid(row=4, columnspan=2)

    # Creates an entry box for the username and positons it using the grid function
    Username = Entry(LoginFrame, font=('arial', 20), textvariable= username, width=15)
    Username.grid(row=2, column=1, padx= 20, pady=20)

    # Creates an entry box for the username and positons it using the grid function    
    Password = Entry(LoginFrame, font=('arial', 20), textvariable=password, width=15, show="*")
    Password.grid(row=3, column=1, padx= 20, pady = 20)

    #Login button to click after completing the form which calls the login() function to 
    #perform the required action e.g Validation and Confirmation
    btn_login = Button(LoginFrame, text="Login", font=('arial', 18), width=10, command= login)
    btn_login.grid(row=5, columnspan=2, padx=20, pady=20)

    #Outputs a Welcome note at the top of the login form
    lbl_welcome = Label(LoginFrame, text="Welcome to ConCloud: Solution to your contact safety problem", fg="Red", font=('arial', 12))
    lbl_welcome.grid(row=0, columnspan=2)

    # A Registration Form button at the top of the login form where user can toggle in to Register
    lbl_register = Button(LoginFrame, text="Register",  font=('arial', 12), command = toggle_to_register)
    lbl_register.grid(row=1, sticky=W, pady = 20)



def registration_form():
    """ 
    Displays the Registration form for the User to register an account.
    The RegisterFrame and lbl_result2 are global variables because they are used in 
    other functions
    """
    global RegisterFrame, lbl_result2

    #Creates another frame 'RegisterFrame' for the registration form from the main frame - root
    RegisterFrame = Frame(root, bg = "AliceBlue",  highlightbackground="Grey",  highlightcolor = "Grey", highlightthickness = 5, width = 100, height = 100, bd= 0)
    RegisterFrame.pack(side=TOP, pady=40, expand = True)

    #Creates the username label in form of a button then positions it using the grid function
    lbl_username = Button(RegisterFrame, text="Username", font=('arial', 18), width = 11)
    lbl_username.grid(row=2, padx =20, pady = 10)

    #Creates the password label in form of a button then positions it using the grid function
    lbl_password = Button(RegisterFrame, text="Password", font=('arial', 18), width = 11)
    lbl_password.grid(row=3, padx =20, pady = 10)

    #Creates the first name label in form of a button then positions it using the grid function
    lbl_firstname = Button(RegisterFrame, text="Firstname", font=('arial', 18), width = 11)
    lbl_firstname.grid(row=4, padx =20, pady = 10)

    #Creates the last name label in form of a button then positions it using the grid function
    lbl_lastname = Button(RegisterFrame, text="Last Name", font=('arial', 18), width = 11)
    lbl_lastname.grid(row=5, padx =20, pady = 10)

    #Creates the email label in form of a button then positions it using the grid function
    lbl_email = Button(RegisterFrame, text="Email Address", font=('arial', 18), width = 11)
    lbl_email.grid(row=6, padx =20, pady = 10)

    #A label that outputs any notification if there is any
    lbl_result2 = Label(RegisterFrame, text="", font=('arial', 18))
    lbl_result2.grid(row=7, columnspan=2)

    # Creates an entry box for the username and positons it using the grid function
    Username = Entry(RegisterFrame, font=('arial', 20), textvariable=username, width=15)
    Username.grid(row=2, column=1, padx = 20)

    # Creates an entry box for the password and positons it using the grid function
    Password = Entry(RegisterFrame, font=('arial', 20), textvariable=password, width=15)
    Password.grid(row=3, column=1, padx = 20)

    # Creates an entry box for the first name and positons it using the grid function
    firstname = Entry(RegisterFrame, font=('arial', 20), textvariable=first_name, width=15)
    firstname.grid(row=4, column=1, padx = 20)

    # Creates an entry box for the last name and positons it using the grid function
    lastname = Entry(RegisterFrame, font=('arial', 20), textvariable=last_name, width=15)
    lastname.grid(row=5, column=1, padx = 20)

    # Creates an entry box for the email and positons it using the grid function
    emailadd = Entry(RegisterFrame, font=('arial', 20), textvariable=email, width=15)
    emailadd.grid(row=6, column=1,padx = 20)

    # Register button to click after completing the form which calls the register() function to 
    #perform the required action e.g Validation and Insertion
    btn_login = Button(RegisterFrame, text="Register", font=('arial', 18), width=10, command= register)
    btn_login.grid(row=8, columnspan=2, pady=20)

    #Outputs a Welcome note at the top of the login form
    lbl_welcome = Label(RegisterFrame, text="Welcome to ConCloud: Solution to your contact safety problem", fg="Red", font=('arial', 12))
    lbl_welcome.grid(row=0, columnspan=2)

    # A Registration Form button at the top of the login form where user can toggle in to Register
    lbl_login = Button(RegisterFrame, text="Login", font=('arial', 12), command = toggle_to_login)
    lbl_login.grid(row=1, sticky=W, pady = 20)

def home():
    """
    Displays the user's personalized dashboard and this function is only called after a successful
    login. The HomeFrame is a global variable because it's used in another function
    """
    global HomeFrame

    #Creates another frame 'HomeFrame' for the dashboard from the main frame - root    
    HomeFrame = Frame(root, bg = "AliceBlue")

    #Outputs a welcome message to the user
    welcome_note = Button(HomeFrame, text="Welcome, " + user + "!", font=('arial', 15), fg='Blue', bg='AliceBlue', bd = 0)
    welcome_note.pack(side = TOP, pady = 10, fill = BOTH, expand = True)

    #Log out button that calls logout_to_login() function to allow the users to logout when clicked
    btn_logout = Button(HomeFrame, text="Logout", font=('arial', 12), bg="Red", width=10, bd = 5, command= logout_to_login)
    btn_logout.pack(side =TOP, anchor = NW)

    #Button that calls the add_contacts_details() function to add contacts
    btn_add_contacts = Button(HomeFrame, text="Add Contacts", font=('arial', 12), bg="LawnGreen", width=10, bd = 5, command= add_contacts_details)
    btn_add_contacts.pack(side = TOP, pady = 10)

    id_option()


    # A label that displays the text 'Contacts'
    btn_contacts = Button(HomeFrame, text="Contacts", font=('arial', 12, 'bold'), width=10, bd = 5, command= login)
    btn_contacts.pack(side = TOP, pady = 10)

    # A column that shows id(#), name, address, phone number, email and actions 
    btn_view_contacts =  Button(HomeFrame, text = "#\t\tName\t\t\tAddress\t\t\tPhone Number\t\t\tEmail Address\t\t", font=('arial', 12, 'bold'), command= login)
    btn_view_contacts.pack(fill = BOTH, expand = True)


    # Calls the Function contacts_details() to displays contacts if available
    contact_details()

def add_contacts_details():
    """ 
    Displays a form for the User to add contacts.
    The ContactDetailsFrame and lbl_result3 are global variables because they are used in 
    other functions
    """
    global ContactDetailsFrame, lbl_result3

    #Destroys or Remove the HomeFrame in other to display the ContactDetailsFrame
    HomeFrame.destroy()

    #Creates another frame 'ContactDetailsFrame' for the contact form from the main frame - root
    ContactDetailsFrame = Frame(root, bg = "AliceBlue", highlightbackground= "Grey", highlightcolor = "Grey", highlightthickness = 5, height = 100, width = 100, bd = 0)
    ContactDetailsFrame.pack(side = TOP, pady = 40, expand = True)

    # Output the text 'New Contact'
    lbl_prompt = Button(ContactDetailsFrame, text="New Contact", font=('arial', 12), width = 12, bd = 1)
    lbl_prompt.grid(row = 0, columnspan = 2, padx = 20, pady = 20 )

    #Creates the name label in form of a button then positions it using the grid function
    lbl_name = Button(ContactDetailsFrame, text= "Name", font = ('arial', 12), width = 12)
    lbl_name.grid(row = 1, padx = 20, pady = 20)

    #Creates the phone number label in form of a button then positions it using the grid function
    lbl_phone = Button(ContactDetailsFrame, text = "Phone Number", font = ('arial', 12), width = 12)
    lbl_phone.grid(row = 2, padx = 20, pady = 20)

    #Creates the address label in form of a button then positions it using the grid function
    lbl_address = Button(ContactDetailsFrame, text = "Contact Address", font = ('arial', 12), width = 12)
    lbl_address.grid(row = 3, padx = 20, pady = 20)

    #Creates the email label in form of a button then positions it using the grid function
    lbl_email = Button(ContactDetailsFrame, text = "Email Address", font = ('arial', 12), width = 12)
    lbl_email.grid(row = 4, padx = 20, pady = 20)

    # Creates an entry box for the name and positons it using the grid function  
    name_add = Entry(ContactDetailsFrame, font = ('arial', 15), textvariable = name,  width = 20)
    name_add.grid(row = 1, column = 1, padx = 20)

    # Creates an entry box for the phone number and positons it using the grid function  
    phone_number_add = Entry(ContactDetailsFrame,  font = ('arial', 15), textvariable = phone_number, width = 20)
    phone_number_add.grid(row = 2, column = 1, padx = 20)

    # Creates an entry box for the address and positons it using the grid function  
    address_add = Entry(ContactDetailsFrame,  font = ('arial', 15), textvariable = address, width = 20)
    address_add.grid(row = 3, column = 1, padx = 20)

    # Creates an entry box for the email and positons it using the grid function  
    email_add = Entry(ContactDetailsFrame,  font = ('arial', 15), textvariable = email_address, width = 20)
    email_add.grid(row = 4, column = 1, padx = 20)

    #A label that outputs any notification if there is any
    lbl_result3 = Label(ContactDetailsFrame,  font = ('arial', 18),  text= "")
    lbl_result3.grid(row = 5, columnspan = 2)

    # A button that calls the add_contacts() Function in other add the contact
    btn_add_contact = Button(ContactDetailsFrame,  font = ('arial', 12),text = "Add Contact", width = 11, bg = "LawnGreen", bd= 5, command = add_contacts)
    btn_add_contact.grid(row = 6, columnspan = 2, padx = 20, pady = 10)

    #A button that calls the toggle_to_home() in other to go back to the dashboard
    lbl_back = Button(ContactDetailsFrame, font = ('arial', 12), text = "Back", command = toggle_to_home)
    lbl_back.grid(sticky = W)

def update_contacts_details():
    """ 
    Displays a form for the User to add contacts.
    The ContactDetailsFrame and lbl_result3 are global variables because they are used in 
    other functions
    """
    global ContactDetailsFrame, lbl_result3

    #Destroys or Remove the HomeFrame in other to display the ContactDetailsFrame
    HomeFrame.destroy()

    #Creates another frame 'ContactDetailsFrame' for the contact form from the main frame - root
    ContactDetailsFrame = Frame(root, bg = "AliceBlue", highlightbackground= "Grey", highlightcolor = "Grey", highlightthickness = 5, height = 100, width = 100, bd = 0)
    ContactDetailsFrame.pack(side = TOP, pady = 40, expand = True)

    # Output the text 'New Contact'
    lbl_prompt = Button(ContactDetailsFrame, text=" Update Contact", font=('arial', 12), width = 12, bd = 1)
    lbl_prompt.grid(row = 0, columnspan = 2, padx = 20, pady = 20 )

    #Creates the name label in form of a button then positions it using the grid function
    lbl_name = Button(ContactDetailsFrame, text= "Name", font = ('arial', 12), width = 12)
    lbl_name.grid(row = 1, padx = 20, pady = 20)

    #Creates the phone number label in form of a button then positions it using the grid function
    lbl_phone = Button(ContactDetailsFrame, text = "Phone Number", font = ('arial', 12), width = 12)
    lbl_phone.grid(row = 2, padx = 20, pady = 20)

    #Creates the address label in form of a button then positions it using the grid function
    lbl_address = Button(ContactDetailsFrame, text = "Contact Address", font = ('arial', 12), width = 12)
    lbl_address.grid(row = 3, padx = 20, pady = 20)

    #Creates the email label in form of a button then positions it using the grid function
    lbl_email = Button(ContactDetailsFrame, text = "Email Address", font = ('arial', 12), width = 12)
    lbl_email.grid(row = 4, padx = 20, pady = 20)

    # Creates an entry box for the name and positons it using the grid function  
    name_add = Entry(ContactDetailsFrame, font = ('arial', 15), textvariable = name,  width = 20)
    name_add.grid(row = 1, column = 1, padx = 20)

    # Creates an entry box for the phone number and positons it using the grid function  
    phone_number_add = Entry(ContactDetailsFrame,  font = ('arial', 15), textvariable = phone_number, width = 20)
    phone_number_add.grid(row = 2, column = 1, padx = 20)

    # Creates an entry box for the address and positons it using the grid function  
    address_add = Entry(ContactDetailsFrame,  font = ('arial', 15), textvariable = address, width = 20)
    address_add.grid(row = 3, column = 1, padx = 20)

    # Creates an entry box for the email and positons it using the grid function  
    email_add = Entry(ContactDetailsFrame,  font = ('arial', 15), textvariable = email_address, width = 20)
    email_add.grid(row = 4, column = 1, padx = 20)

    #A label that outputs any notification if there is any
    lbl_result3 = Label(ContactDetailsFrame,  font = ('arial', 18),  text= "")
    lbl_result3.grid(row = 5, columnspan = 2)

    # A button that calls the update_contacts() Function in other add the contact
    btn_update_contact = Button(ContactDetailsFrame,  font = ('arial', 12),text = "Update", width = 11, bg = "Orange", bd= 5, command = update_contacts)
    btn_update_contact.grid(row = 6, columnspan = 2, padx = 20, pady = 10)

    #A button that calls the toggle_to_home() in other to go back to the dashboard
    lbl_back = Button(ContactDetailsFrame, font = ('arial', 12), text = "Back", command = toggle_to_home)
    lbl_back.grid(sticky = W)

def logout_to_login():
    """
    Function that logs out a user if the user clicks 'yes' 
    when a prompt is shown.
    """
    result = tkMessageBox.askquestion('Log Out', 'Are you sure you want to Log out?', icon="warning")
    if result == 'yes':
        HomeFrame.destroy()
        login_form()


def toggle_to_home(event = None):
    #Destroys the ContactDetailsFrame then calls the home() Function
    ContactDetailsFrame.destroy()
    home()

def toggle_to_login(event=None):
    #Destroys the RegisterFrame then calls the login_form() Function
    RegisterFrame.destroy()
    login_form()

def toggle_to_register(event=None):
    #Destroys the LoginFrame then calls the registration_form() Function
    LoginFrame.destroy()
    registration_form()

def export_warning():
    """
    Function that moves to the export_contacts() if the user clicks 'yes' 
    when a prompt is shown.
    """
    result = tkMessageBox.askquestion('Export Contacts', 'Are you sure you want to Export your contacts now?', icon="warning")
    if result == 'yes':
        export_contacts()

def update_warning():
    """
    Calls the update_details() function to update a contact if a valid ID number is chosen and 
    the prompt reply is yes else it shows an error
    """
    if num.get() != "Select ID":
        result = tkMessageBox.askquestion('Update Contact', 'Are you sure you want to update that contact ?', icon="warning")
        if result == 'yes':
            update_details()
    else:
        tkMessageBox.showerror('Invalid Contact ID', 'Please select a contact ID number')


def delete_warning():
    """
    Calls the delete_contact() function to update a contact if a valid ID number is chosen and 
    the prompt reply is yes else it shows an error
    """
    if num.get() != "Select ID":
        result = tkMessageBox.askquestion('Delete Contact', 'Are you sure you want to delete that contact ?', icon="warning")
        if result == 'yes':
            delete_contact()
    else:
        tkMessageBox.showerror('Invalid Contact ID', 'Please select a contact ID number')

def register():
    """
    Function that validates and add user to the database
    """

    #Calls the databases function
    database()

    #Validates if the username, password, first name, last name and email is not empty else it displays an error message
    if username.get == "" or password.get() == "" or first_name.get() == "" or last_name.get == "" or email.get == "":
        lbl_result2.config(text="Please complete the required field!", fg="orange")
    else:
        #Checks if the user has not been registered in the database before else reports an error
        cursor.execute("SELECT * FROM users WHERE `username` = ? and `email` = ?", (username.get(), email.get()))
        if cursor.fetchone() is not None:
            lbl_result2.config(text="Username or Email Address is already taken", fg="red")
        else:

            #Validation of Email Address during registration
            try:
                if emails.search(str(email.get())):
                    pass
                else:
                    raise NameError

                if str(first_name.get()).replace(" ", "").isalpha():
                    pass
                else:
                    raise TypeError

                if str(last_name.get()).replace(" ", "").isalpha():
                    pass
                else:
                    raise TypeError

            except (NameError, TypeError):
                lbl_result2.config(text="Invalid First Name, Last Name or Email Address!", fg="red")

            else:

                # Add the user's details to the users table then set the variables of registration to an empty string
                cursor.execute("INSERT INTO users (username, password, first_name, last_name, email) VALUES(?, ?, ?, ?, ?)", (str(username.get()), str(password.get()), str(first_name.get()), str(last_name.get()), str(email.get())))
                conn.commit()
                username.set("")
                password.set("")
                first_name.set("")
                last_name.set("")
                email.set("")

                #Reports a success mesaage
                lbl_result2.config(text="Successfully Created!", fg="black")
        
        #Closes the database connection
        cursor.close()
        conn.close()


def login():
    """
    Function that validates and add user to the database
    id_number and user are global variables used in other fucntions
    """
    
    global id_number, user

    #Calls the databases function
    database()

    #Returns an error message if the username and password is empty
    if username.get() == "" or password.get() == "":
        lbl_result1.config(text="Please complete the required field!", fg="orange")
    else:
        #Confirms if the login detail is valid then logs in the user..
        cursor.execute("SELECT * FROM users WHERE `username` = ? and `password` = ?", (username.get(), password.get()))
        if cursor.fetchone() is not None:
            LoginFrame.destroy()
            cursor.execute("SELECT * FROM users WHERE `username` = ? and `password` = ?", (username.get(), password.get()))
            user_ids = cursor.fetchall()
            
            #Gets the user's ID
            id_number = user_ids[0][0]

            #Get's the user's username
            user = username.get()

            #Sets the username and password variable to an empty string
            username.set("")
            password.set("")
            home()
        else:
            #Returns an error message if the login details cannot be found in the database
            lbl_result1.config(text="Invalid Username or password", fg="red")



def add_contacts():
    """
        Adds contacts to the contacts table in the database attached 
        to the user.
    """

    #Calls the database() function
    database()

    #Returns an error message if the name and phone number is empty
    if name.get() == "" and phone_number.get() == "":
        lbl_result3.config(text="Please complete the required field!", fg="orange")
    else:

        #Returns an eror if the details already exist in the contacts table attached to the user
        cursor.execute("SELECT * FROM contacts WHERE  `phone_number` = ? and `user_id` = ?", (phone_number.get(), id_number))
        if cursor.fetchone() is not None:
            lbl_result3.config(text="Phone Number Already Exists!", fg="red")
        else:

            #Validation of Name, Email Address and Phone Number when adding contacts
            try:

                if int(str(phone_number.get())) and len(str(phone_number.get())) >= 10 and len(str(phone_number.get())) <= 11:
                    pass
                elif int(str(phone_number.get())[1:]) and len(str(phone_number.get())) == 14 and str(phone_number.get())[0] == '+':
                    pass
                else:
                    raise ValueError

                if emails.search(str(email_address.get())) or email_address.get() == "":
                    pass
                else:
                    raise NameError

                if str(name.get()).replace(" ", "").isalpha():
                    pass
                else:
                    raise TypeError

            except (ValueError, NameError, TypeError):
                lbl_result3.config(text="Invalid Name, Phone number or Email Address!", fg="red")

            else:

                #Adds the contact to the contacts table and save
                cursor.execute("INSERT INTO contacts (name, address, phone_number, email_address, user_id) VALUES(?, ?, ?, ?, ?)", (str(name.get()), str(address.get()), str(phone_number.get()), str(email_address.get()), int(id_number)))
                conn.commit()

                #Sets name, address, phone number and email address variable to an empty string
                name.set("")
                address.set("")
                phone_number.set("")
                email_address.set("")

                #Outputs a success message
                lbl_result3.config(text="Contact added Successfully!", fg="black")

        #Closes the connection in the database
        cursor.close()
        conn.close()


def id_option():
    #ID option frame
    global num
    #Creates an empty list to store the number each user has
    contact_num  = []

    #Calls the database function
    database()

    #Fectches all the contacts associated to the user
    cursor.execute("SELECT * FROM contacts WHERE  `user_id` = ?", (id_number,))
    contacts = cursor.fetchall()

    # Outputs the contacts if any
    if contacts:
        for contact in contacts:
            #Adds the contact id to the contact_num list
            contact_num.append(contacts.index(contact)+1)

        # num - A variable for user's input
        num = StringVar()

        #num initial value
        num.set("Select ID")


        #Export button to update contacts by invoking the delete_warning() function         
        btn_update = Button(HomeFrame, text = "Export Contacts", font = ('arial', 12), width=12, bg = "blue", command = export_warning)
        btn_update.pack(side = TOP, anchor = NW)

        #Creates an option menu that has the number of contacts
        option = OptionMenu(HomeFrame, num, *contact_num,)
        option.pack(side = TOP, anchor = NE)

        #Update button to update contacts by invoking the delete_warning() function         
        btn_update = Button(HomeFrame, text = "Update", font = ('arial', 12), width=10, bg = "orange", command = update_warning)
        btn_update.pack(side = TOP, anchor = NE, pady = 5)


        #Delete button to delete contacts by invoking the delete_warning() function        
        btn_delete = Button(HomeFrame, text = "Delete", font = ('arial', 12), width=10, bg = "red", command = delete_warning)
        btn_delete.pack(side = TOP, anchor = NE, pady = 5)

def contact_details():
    """
    Displays all contacts associated to the user in the user's 
    dashboard
    """

    #Global variables that are use in other functions
    global scrollable_frame, num

    ##############################################################################
    # Scripts that creates a canvas and scrollbar from the tkinter module in     #
    # order for multiple contacts to be shown by scrolling up and down           #                                                          
    ##############################################################################
    canvas = Canvas(HomeFrame)
    scrollbar = Scrollbar(HomeFrame, orient="vertical", command=canvas.yview)
    scrollable_frame = Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    canvas.configure(yscrollcommand=scrollbar.set)
    HomeFrame.pack()
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    #Creates an empty list to store the number each user has
    contact_num  = []

    #Calls the database function
    database()

    #Fectches all the contacts associated to the user
    cursor.execute("SELECT * FROM contacts WHERE  `user_id` = ?", (id_number,))
    contacts = cursor.fetchall()

    # Outputs the contacts if any
    if contacts:
        for contact in contacts:

            #Outputs each contact row by row
            number = Button(scrollable_frame, text = str(contacts.index(contact)+1) + "\t\t" + str(contact[1]) + "  "*(18- len(str(contact[1]))) +"\t\t" + str(contact[2]) + "  "*(26 - len(str(contact[2]))) + "\t\t" + str(contact[3]) + "  "*(11 - len(str(contact[3]))) + "\t\t\t" + str(contact[4]) + "  "*(25 - len(str(contact[4]))), font = ('arial', 10, 'bold'), bg = "AliceBlue")
            number.pack(pady = 20, fill =  BOTH, expand = True)


    else:
        #Output "No Contacts Added yet" if not contact was found in the database
        no_contact = Label(scrollable_frame, text ="\n" + "\t" * 7+ "No Contacts Added yet", font = ('arial', 12, 'bold'))
        no_contact.pack()

def export_contacts():
    #Calls the database function
    database()
    #Fectches all the contacts associated to the user
    cursor.execute("SELECT id, name, address, phone_number, email_address FROM contacts WHERE  `user_id` = ?", (id_number,))
    contacts = cursor.fetchall()

    file_name = str(user) + "-contacts.csv"
    contacts_to_export = []

    #Stores and append the user's contacts in the contacts_to_export list by making sure the 
    #id number is well ordered
    if contacts:
        for contact in contacts:         
           con = [str(contacts.index(contact)+1), str(contact[1]) , str(contact[2]), str(contact[3]), str(contact[4])]
           contacts_to_export.append(con)

    try:
        #Stores the program in a csv file
        headers = [i[0] for i in cursor.description]
        csvfile = csv.writer(open(file_name, 'w', newline=''),
                             delimiter=',', lineterminator='\r\n',
                             quoting=csv.QUOTE_ALL, escapechar='\\')

        csvfile.writerow(headers)
        csvfile.writerows(contacts_to_export)

        #Report a confirmation message if the contacts have been stored properly
        tkMessageBox.showinfo('Contacts Exported Successfully', 'Your contacts file has been stored in the directory where this program is stored in a file named "' + str(file_name) + '"')
    except:
        pass



def delete_contact():
    #Stores the contact that wants to be deleted
    contact = int(num.get()) - 1

    #Calls the database() function
    database()

    #Fetches all the contacts associated to the user 
    cursor.execute("SELECT * FROM contacts WHERE  `user_id` = ?", (id_number,))
    contacts = cursor.fetchall()
    #Gets the right id of contact to be deleted
    contact_to_delete = contacts[contact][0]

    #Deletes the contact the saves
    cursor.execute("DELETE FROM contacts WHERE  `id` = ?", (contact_to_delete,))
    conn.commit()
    cursor.close()
    conn.close()

    #Destroys the HomeFrame and calls back the home() function which is the dashboard
    HomeFrame.destroy()
    home()

def update_details():

    #Stores the contact id to be updated
    contact = int(num.get()) - 1

    #Calls the database() Function 
    database()

    #Fetches all the contact associated with the user
    cursor.execute("SELECT * FROM contacts WHERE  `user_id` = ?", (id_number,))
    contacts = cursor.fetchall()

    #Populates the name, address, phone number and email with the acual data stored
    name.set(contacts[contact][1])
    address.set(contacts[contact][2])
    phone_number.set(str(contacts[contact][3]))
    email_address.set(contacts[contact][4])

    #Calls this function that prompts the user to update the contact
    update_contacts_details()


def update_contacts():
    #Calls the database() function
    database()

    #Stores the contact id to be updated in the contact variable
    contact = int(num.get()) - 1

    #Fetches all the contacts associated with the user from the database
    cursor.execute("SELECT * FROM contacts WHERE  `user_id` = ?", (id_number,))
    contacts = cursor.fetchall()

    #Gets the actual id number of the contact in the database
    id_num = contacts[contact][0]

    #Returns error if the name and phone number variable is empty
    if name.get() == "" and phone_number.get() == "":
        lbl_result3.config(text="Please complete the required field!", fg="red")
    else:
        #Validates if the contact is not in the database else returns error
        cursor.execute("SELECT * FROM contacts WHERE  `phone_number` = ? and `user_id` = ?", (phone_number.get(), id_number))
        if cursor.fetchone() is not None:
            lbl_result3.config(text="Phone Number Already Exists!", fg="red")
        else:

            #Validation of Name, Email Address and Phone Number when updating contacts
            try:

                if int(str(phone_number.get())) and len(str(phone_number.get())) >= 10 and len(str(phone_number.get())) <= 11:
                    pass
                elif int(str(phone_number.get())[1:]) and len(str(phone_number.get())) == 14 and str(phone_number.get())[0] == "+":
                    pass
                else:
                    raise ValueError

                if emails.search(str(email_address.get())) or email_address.get() == "":
                    pass
                else:
                    raise NameError

                if str(name.get()).replace(" ", "").isalpha():
                    pass
                else:
                    raise TypeError

            except (ValueError, NameError, TypeError):
                lbl_result3.config(text="Invalid Name, Phone number or Email Address!", fg="red")

            else: 
            #Updates the contact then saves
                cursor.execute("UPDATE contacts SET name = ?, address = ?, phone_number = ?, email_address = ?  WHERE id = ?", (str(name.get()), str(address.get()), str(phone_number.get()), str(email_address.get()), int(id_num)))
                conn.commit()

                #Sets name, address, phone number and email address to an empty string
                name.set("")
                address.set("")
                phone_number.set("")
                email_address.set("")

                #Returns a success message
                lbl_result3.config(text="Contact updated Successfully!", fg="black")

        #Closes the connection
        cursor.close()
        conn.close()

#The program starts the login_form() function when executed
login_form()

#========================================MENUBAR WIDGETS==================================
#The Menu Bar 'File' with 'Exit' as it's file
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Exit", command=quit)
menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)


#========================================INITIALIZATION===================================
#Checks if the it's a script file before executing
if __name__ == '__main__':

    #Makes the GUI window not to disappear until a user performs the right action
    root.mainloop()
