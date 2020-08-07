"""
PROJECT TITLE: STUDENT GRADING SYSTEM
DEVELOPED BY: BOCKARIE LAHAI as a Final project in Scholar Network Python Course

This is a STUDENT GRADING SYSTEM developed using PYTHON and TEXT FILE
The program basically utilised Python Function and Object Oriented Programming(Classes)
In this Grading System, the administrator  will be authorized to operate the system with an authenticated login system
The system will ease the work of college examiners in calculating and keeping track of students' grades and record
With the help of option numbers for navigation, you can chose to return to login page, Register/Enter students details, 
retrieve their details and logout of the system. The records will be kept in a text file that is automatically created
Each Student will have a text file to store his details based on the ID No

The Administrator has a default login username and password to be used for any login prompt
username: admin
password: 12345
upon starting the program the administrator is required to log into the system.
"""
#These are the standard library imported to ease the working with codes. The regular expression (re) is specifically 
#used to validating students details inputs ranging from name, subjects, ID No., Grades etc. The time module was used for 
#delaying the display of certain information for efficient reading.
#The datetime module was used to tell the time the Administrator logged-in and also logged-out
import re
import time
import datetime

#These are CONSTANTS defined that were used throughtout the program without rewriting them anywhere they were needed.
#This reduceses lines of codes and give clear look on the entire codes
WELCOME_MESSAGE = "\nWELCOME TO THE STUDENT GRADING SYSTEM"
MESSAGE = "Choose any of the option below:\n"
LOGIN_MESSAGE = "This system is Authorized to one Admin User!\n"
RETRIEVE_GRADES = "Press 2: To Retrieve Grades"
REGISTER = "Press 1: To Record Students' Details"
LOGOUT = "Press 3: To Logout"
ASTERISK = ("*" * 50)


#This Function is defined to accomplish the task of navigating back to the Home page from another page
def home_button():
    """
    This function is used to navigate to the Home Page from any part of the application
    It is the back button that ease you from the stress of accessing the home page from another page
    It can also help you logout of the system from any page by pressing the login button
    """
    print("\nYOU ARE ALLOWED TO NAVIGATE THE SYSTEM")
    time.sleep(1)
    print(MESSAGE)
    while True:
        try:
            button= int(input(f'Press 1: To Return to Home Page \nPress 2: To Logout \nEnter Here > '))
            if button == 1:
                grading_system()
                break
            elif button == 2:
                time.sleep(1)
                print(f"\nLogout Successful at {datetime.datetime.today()}")
                print(ASTERISK)
                print("\nTHANK YOU FOR USING THE SYSTEM DEVELOPED BY BOCKARIE LAHAI!")
                print(ASTERISK)
                exit()
            else:
                print("You Pressed the wrong Number")
                time.sleep(0.5)
                print("Try again\n")
        except ValueError:
            print("\nYou Enter an invalid character, Try again!\n")
            time.sleep(1)
            print(MESSAGE)
            

#This is the general function defined within which all the classes are used to accomplish the required goal of the program
def grading_system():
    """
    This function accepts no argument, but the implementation of the codes are being done within this function.
    """
    time.sleep(1)
    print(WELCOME_MESSAGE) #Here the system welcomes the administrator to give a clear picture of the application
    print(ASTERISK + "\n")
    time.sleep(1)
    print(MESSAGE) #This message direct the user on the next step after logging-in
    time.sleep(1)
    
    #A dictionary used to store the options to access the various classes responsible for login, resgistration and retrieving
    #students information etc.
    prompts = {
        1: StudentRegistration,
        2: RetrieveStudentsInformation
    }
    
    #This loop allows user input to choose the various options to access the sytem functionalities. These options are validated
    #such that only option numbers that display can be used to access the corresponding programs. All possible errors are being handled
    while True:
        try:
            prompt = int(input(f'{REGISTER} \n{RETRIEVE_GRADES}  \n{LOGOUT} \nEnter Here > '))
            if prompt in prompts:
                prompts[prompt]() #This code grant access to the classes defined in the prompts dictionary above
                break
            elif prompt == 3:
                time.sleep(1)
                print(f"\nLogout Successful at {datetime.datetime.today()}")
                print(ASTERISK)
                print("\nTHANK YOU FOR USING THE SYSTEM DEVELOPED BY BOCKARIE LAHAI!")
                print(ASTERISK)
                exit()
            else:
                print("You Pressed the wrong Number")
                time.sleep(0.5)
                print("Try again\n")
        except ValueError:
            print("\nYou Enter an invalid character, Try again!\n")
            time.sleep(0.5)
            print(MESSAGE)
    
    #The classes are instantiated here with conditional statements. Prompt 1 instantiate the Student Registration class
    #that allows the administrator to Register/Enter students information in the system and calculate total percentage and ranking of students
    #prompt 2 will take you back to the login form
    #Prompt 3 let you to retrieve the details of students in the system
    #Prompt 4 is the logout option
    if prompt == 1:
        student_registration = StudentRegistration() #Instantiation the Student Registration Class
        student_registration.register_student()
    elif prompt == 3:
        retrieve = RetrieveStudentsInformation() #Instantiation of the Retrieve Student Information
        retrieve.student_grades()
        

#Classes are defined in this section with it various methods for accomplishing specific goals
#The AdminLog class here. Few classes were defined with many instance methods that makes the application functionalities
#Work as expected. 
class AdminLog():
    """
    This is a super class that holds the default admin username and password. It has a child class Login
    The proper use of the system start here as without this default username and password the administrator can not
    access the system
    """
    def __init__(self):
        self.users = {
            "root":{
                "password": 12345,
                "group": "admin"
            }
        } 

#This class will help in accpeting the input from admin user for the username and password. These inputs are validated to avoid 
#Logging in without authentication  
class Login(AdminLog):
    """
    The Login Class has two instance methods responsible for accepting login details from the administrator
    with username and password validation before logging into the sytem
    """
    def __init__(self):
        super().__init__()
        print("\nWELCOME TO THE LOGIN PAGE")
        print(ASTERISK)
    def admin_login_detail(self):
        time.sleep(1)
        print("\nLogin Form!")
        print(LOGIN_MESSAGE)
        time.sleep(1)
        print("Enter your Login details Here:")
        
        #Using a while loop to get redirecting the administrator to the Login form when ever a wrong input is done
        #based on the validation instance method 
        while True:
            self.username = input("Username> ")
            try:
                self.password = int(input("Password> "))
                self.password_validation()
                break 
            except ValueError:
                print("\nYou Entered an invalid character, Try again!\n")
                time.sleep(1.3)
                print("Enter your Login details Here:")
    
    #The validation method that check whether the username and password is contained in the users dictionary
    #in the parent class Admin Log
    def password_validation(self):
        if self.password == self.users["root"]["password"] and self.username == self.users["root"]["group"]:
            print(f"\nLogin successful at {datetime.datetime.today()}")
            print(ASTERISK)
        else:
            print("\nLogin details Not Correct" + "\n" "Try again!")
            self.admin_login_detail()

#This class handled bulk of the implimentation of the application's functionalities. This is a super class with many instance 
#Instance methods
class StudentRegistration():
    """
    The Student Registration Class Handled Bulk of the work to complete the functionalities of the application
    For efficiency as bulk of the information the application uses are received from a user, therefore some of the instance 
    attributes were set to default empty strings, and empty lists for proper code reuseability.
    The methods here such as register students is responsible for storing all other instance methods implementation 
    to register students details into the system
    """
    #The various attributes defined in the __init__
    def __init__(self):  
        self.student_id = 0
        self.name = ""
        self.department = ""
        self.programme = ""
        self.marks =[]
        self.subject_name = []
        self.total_score = 0
        self.percentage_score = 0
    
    #This is responsible for storing information related to recording students details which is invoked on
    #on the instantiated object.
    def register_student(self):
        print("\nEnter Student details Here:")
        time.sleep(2)
        self.check_id()
        self.check_name()
        self.check_file_and_id()
        self.student_mark()
        time.sleep(1)
        home_button()
        
    #This check the Student ID with Existing IDs in the systems. If the ID entered correspond with an
    #existing Student ID the admin will be prompted to Enter another ID No.
    def check_file_and_id(self):
        try:
            with open(f"{self.student_id}.txt", "r") as text_file:
                line = text_file.readline()
                if self.name in line:
                    self.check_department()
                    self.check_programme()
                else:
                    print("Student ID already exist with different Name. Try another ID")
                    self.check_id()
                    self.check_name()
                    self.check_file_and_id()
        except FileNotFoundError:
            # self.check_name()
            self.check_department()
            self.check_programme()
        

    #This method is used to recieve input from the administrator. Students IDs are received here.
    #It validate the input it recieves by handling possible Errors that will arise during input.
    #It helps the system to accept only positive hold numbers as Student ID.
    def check_id(self):
        try:
            self.student_id = (input ("\nEnter Student ID No.: "))
            if int(self.student_id) <= 0:
                print("Student ID field must be Numeric and above 0!\n")
                time.sleep(0.5)
                self.check_id()
        except:
            print("\nYou Entered an invalid character, Try again!")
            time.sleep(0.5)
            self.check_id()

    #This method helps for students name input and also validate the name by checking charecters that should not be 
    #be included in a name
    def check_name(self):
        self.name = input ("Enter Student Full Name: " ).title()
        pattern = re.compile('[0-9]|^$')
        if pattern.search(self.name):
            print("Name field must be alphabeth!\n")
            time.sleep(0.5)
            self.check_name()
    
    #Prompt to input Department. It is also validated using regular expression(re)
    def check_department(self):
        self.department = input ("Enter Department Name: " )
        pattern = re.compile('[0-9]|^$')
        if pattern.search(self.department):
            print("Department field must be alphabeth!\n")
            time.sleep(0.5)
            self.check_department()
    
    #This prompt for the input of the prohramme of study. It is also validated using regular expression(re)      
    def check_programme(self):
        self.programme = input ("Enter Name of Programme: " )
        pattern = re.compile('[0-9]|^$')
        if pattern.search(self.programme):
            print("Programme field must be alphabeth!\n")
            time.sleep(0.5)
            self.check_programme()
            
    #Another key instance method that holds all the subjects and grades implementation methods     
    def student_mark(self):        
        print ("\nEnter marks of 5 subjects: " )
        self.subject_one()
        self.subject_two()
        self.subject_three()
        self.subject_four()
        self.subject_five()
        self.display_student()
    
    #The system is developed to accept five 5 subject inputs from the administrator. This is one of the methods responsible for receiving
    #Subject names and grades and validates them before manipulating on them. Scores between 0 and 100 are only allowed
    def subject_one(self):
        self.subject = input("\nEnter Subject 1 Name: ")
        pattern = re.compile('[0-9]|^$')
        if pattern.search(self.subject):
            print("Invalid Entry for Subject Name. Try again!\n")
            time.sleep(0.5)
            self.subject_one()
        else:
            self.subject_name.append(self.subject)
            self.grade_one()
            
    def grade_one(self):
        try:
            self.subject_mark = int(input(f"Enter {self.subject} Grade: "))
        except ValueError:
            print("Invalid Entry for Grade. Try again!\n")
            time.sleep(0.5)
            self.grade_one()
        else:
            mark_pattern = re.compile('[A-Za-z]|^$')
            if mark_pattern.search(str(self.subject_mark)):
                print("Invalid Entry for Grade. Try again!\n")
                time.sleep(0.5)
                self.grade_one()
            elif self.subject_mark >= 0 and self.subject_mark <= 100:
                self.marks.append(self.subject_mark)
            else:
                print("Grade must be between 0 and 100")
                time.sleep(0.5)
                self.grade_one()
        
        
    def subject_two(self):
        self.subject = input("\nEnter Subject 2 Name: ")
        pattern = re.compile('[0-9]|^$')
        if pattern.search(self.subject):
            print("Invalid Entry for Subject Name. Try again!\n")
            time.sleep(0.5)
            self.subject_two()
        else:
            self.subject_name.append(self.subject)
            self.grade_two()
            
    def grade_two(self):
        try:
            self.subject_mark = int(input(f"Enter {self.subject} Grade: "))
        except ValueError:
            print("Invalid Entry for Grade. Try again!\n")
            time.sleep(0.5)
            self.grade_two()
        else:
            mark_pattern = re.compile('[A-Za-z]|^$')
            if mark_pattern.search(str(self.subject_mark)):
                print("Invalid Entry for Grade. Try again!\n")
                time.sleep(0.5)
                self.grade_two()
            elif self.subject_mark >= 0 and self.subject_mark <= 100:
                self.marks.append(self.subject_mark)
            else:
                print("Grade must be between 0 and 100")
                time.sleep(0.5)
                self.grade_two()
    
    
    def subject_three(self):
        self.subject = input("\nEnter Subject 3 Name: ")
        pattern = re.compile('[0-9]|^$')
        if pattern.search(self.subject):
            print("Invalid Entry for Subject Name. Try again!\n")
            time.sleep(0.5)
            self.subject_three()
        else:
            self.subject_name.append(self.subject)
            self.grade_three()
            
    def grade_three(self):
        try:
            self.subject_mark = int(input(f"Enter {self.subject} Grade: "))
        except ValueError:
            print("Invalid Entry for Grade. Try again!\n")
            time.sleep(0.5)
            self.grade_three()
        else:
            mark_pattern = re.compile('[A-Za-z]|^$')
            if mark_pattern.search(str(self.subject_mark)):
                print("Invalid Entry for Grade. Try again!\n")
                time.sleep(0.5)
                self.grade_three()
            elif self.subject_mark >= 0 and self.subject_mark <= 100:
                self.marks.append(self.subject_mark)
            else:
                print("Grade must be between 0 and 100")
                time.sleep(0.5)
                self.grade_three()
        
        
    def subject_four(self):
        self.subject = input("\nEnter Subject 4 Name: ")
        pattern = re.compile('[0-9]|^$')
        if pattern.search(self.subject):
            print("Invalid Entry for Subject Name. Try again!\n")
            time.sleep(0.5)
            self.subject_four()
        else:
            self.subject_name.append(self.subject)
            self.grade_four()
            
    def grade_four(self):
        try:
            self.subject_mark = int(input(f"Enter {self.subject} Grade: "))
        except ValueError:
            print("Invalid Entry for Grade. Try again!\n")
            time.sleep(0.5)
            self.grade_four()
        else:
            mark_pattern = re.compile('[A-Za-z]|^$')
            if mark_pattern.search(str(self.subject_mark)):
                print("Invalid Entry for Grade. Try again!\n")
                time.sleep(0.5)
                self.grade_four()
            elif self.subject_mark >= 0 and self.subject_mark <= 100:
                self.marks.append(self.subject_mark)
            else:
                print("Grade must be between 0 and 100")
                time.sleep(0.5)
                self.grade_four()
        
        
    def subject_five(self):
        self.subject = input("\nEnter Subject 5 Name: ")
        pattern = re.compile('[0-9]|^$')
        if pattern.search(self.subject):
            print("Invalid Entry for Subject Name. Try again!\n")
            time.sleep(0.5)
            self.subject_five()
        else:
            self.subject_name.append(self.subject)
            self.grade_five()
    def grade_five(self):
        try:
            self.subject_mark = int(input(f"Enter {self.subject} Grade: "))
        except ValueError:
            print("Invalid Entry for Grade. Try again!\n")
            time.sleep(0.5)
            self.grade_five()
        else:
            mark_pattern = re.compile('[A-Za-z]|^$')
            if mark_pattern.search(str(self.subject_mark)):
                print("Invalid Entry for Grade. Try again!\n")
                time.sleep(0.5)
                self.grade_five()
            elif self.subject_mark >= 0 and self.subject_mark <= 100:
                self.marks.append(self.subject_mark)
            else:
                print("Grade must be between 0 and 100")
                time.sleep(0.5)
                self.grade_five()

    #This method add all the scores inputted into the system
    def student_total_score(self):
        for score in self.marks:
            self.total_score += score
    
    #This calculate the Total percentage score of each student that can be used to rank student
    def calculate_percentage(self):
        self.total_percentage_score = self.total_score /5
    
    #The ranking of the students is done here based on the information from total percentage calculation. This will give
    #the students a clear picture of their performance throughout
    def rank_student(self):
        if self.total_percentage_score >= 75:
            return "You got DISTINCTION!"
        elif self.total_percentage_score >=65:
            return "You got a CREDIT!"
        elif self.total_percentage_score >=50:
            return "You got a PASS!"
        else:
            return "You FAILED!"
    
    #This method store all the information to be displayed after inputting them as a confirmation
    def display_student(self):
        self.student_total_score()
        self.calculate_percentage()
        self.show()
        print(self.rank_student())
        self.store_grades()
    
    #This method is used to implement the information to be viewed at the end of using the application. It is stored in the display student
    #method
    def show(self):  
        print("\nView your Grade details below:")
        print(ASTERISK)
        time.sleep(2)
        print(f'Name: {self.name} \nID: {self.student_id} \nTotal Score: {self.total_score} \
            \nTotal Percentage: {self.total_percentage_score} \nDepartment: {self.department} \
            \nProgramme: {self.programme}')
        
        for sub, grades in zip(self.subject_name, self.marks):
            print(f"{sub}: {grades}")
    
    #The main purpose of the program is to store the students information in a text file. This was accomplished here by 
    #Writing all the necessary information in a text file
    def store_grades(self):
        store = (f'Name: {self.name}, ID: {self.student_id}, Total Score: {self.total_score}, \
Total Percentage: {self.total_percentage_score}, Department: {self.department}, \
Programme: {self.programme}, {self.rank_student()}\n')
        with open(f"{self.student_id}.txt", "a") as text_file:
            text =text_file.write(store)
            return text
    
#This is a sub class responsible for retrieving students information from the database file. For students information 
#already in the file       
class RetrieveStudentsInformation(StudentRegistration):
    """
    This class is a sub class of the Student Registration class. Retrieving the students information is implemented here
    The adminwill be required to enter a student ID No and the system will search it database file to retrieve
    information related to that ID No.
    """
    def __init__(self):
        super().__init__()
        print("\nSearch for student's information from the text file")
        print(ASTERISK)
        self.student_grades()
    
    #This method helps by asking for students ID No to retrieve information related to that ID No.
    def student_grades(self):
        try:
            self.file_info = input("Enter Student ID No to Search> ")
            with open(f"{self.file_info}.txt", "r") as text_file:
                lines = text_file.read()
                print(f"\nThe information for Student with ID No.: {self.file_info} is shown below:")
                print(ASTERISK)
                time.sleep(1)
                print(lines.strip())
                time.sleep(1)
                home_button() #Invoking the home button function
        except FileNotFoundError:
            print("\nThe ID No is not available in the file")
            print(ASTERISK)
            time.sleep(1)
            home_button() #Invoking the home button function
    
#This instance help by making the login page the first page which is the access point for all the functionalities of the application
student = Login()
student.admin_login_detail()

#Invocation of the main function. Without invoking this function all the codes contained within it body will not work
grading_system()
