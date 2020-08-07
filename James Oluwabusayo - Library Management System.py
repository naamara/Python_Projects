#The sys function that helps us terminate the Code when we choose to.
#Task to Create a Library Program, For Students and staffs of a Univeristy
#to borrow and Return books from the Library
#The progarm also requires the User to login with their Matric No and Staff ID
#for student and Staff respectively
#For the library Class, layers of abstraction ---- display available books, lend books and add book
#For the Student Class, layers of abstraction ---- request a book and return a book
#For the Login Class ---- Student login and Staff login


import sys 



class Library:
    def __init__(self, listofbooks):
        self.availablebooks = listofbooks

    def displayAvailablebooks(self):
        print("\n")
        print("The books we have in our library are as follows:")
        print("================================================")
        for book in self.availablebooks:
            print(book)
        print("================================================")

    def lendBook(self, requestedBook):
        if requestedBook in self.availablebooks:
            print("\n")
            print("You have successfully borrowed the book")
            self.availablebooks.remove(requestedBook)
        else:
            print("\n")
            print("Sorry the book you requested has been borrowed")

    def addBook(self, returnedBook):
        self.availablebooks.append(returnedBook)
        print("\n")
        print("Thanks for returning the book")




class Student():
    def requestBook(self):
        book = input("Enter the name of the book you will like to borrow: ")
        self.book = book
        return book

    def returnBook(self):
        book = input("Enter the name of the book you will like to return: ")
        return book


class Login():
    def studentLogin(self):
           
        self.matric = input("Enter your Matric No: ")
        while self.matric not in studentMatricNo:
            print("Student Not found, Please check your Matric No or see the Admin")
            print("Login System is case sensitive")
            self.matric = input("Enter your Matric No: ")
        print("Login Successful, Welcome")
        main()


    def staffLogin(self):
        self.staffID = input("Enter your Staff ID: ")
        while self.staffID not in staffIDnumber:
            print("Staff Not found, Please check your Staff ID or see the Admin")
            print("Login System is case sensitive")
            self.staffID = input("Enter your Matric No: ")
        print("Login Successful, Welcome")
        main()

staffIDnumber = ["56789Za", "67890Yb", "78901Xc"]
studentMatricNo = ["12345Aa", "23456Ba", "34567Ca"]

def main():
    library = Library(["Advanced Archeaology", "Engineering Mathematics", "Advanced Statistics", "Probability"])
    student = Student()
    done = False
    while done == False:
        print("\n")
        print("""===========LIBRARY MENU============
            1. Available Books
            2. Request a Book
            3. Return a Book 
            4. Exit
            """)
        choice = int(input("Enter Choice: "))
        if choice == 1:
            library.displayAvailablebooks()
        elif choice == 2:
            library.lendBook(student.requestBook())
        elif choice == 3:
            library.addBook(student.returnBook())
        elif choice == 4:
            sys.exit()

login = Login()

print("              Welcome to James University Library Portal              ")
print("----------------------------------------------------------------------")
print("======================Welcome to the Login Page=======================")
print("Are you a Student or Staff: ")
print("""
        1 = Student 
        2 = Staff
    """)
    
category = int(input("Category: "))
if category == 1:
    print("\n")
    login.studentLogin()
elif category == 2:
    login.staffLogin()
else:
    print("Invaild Option")




