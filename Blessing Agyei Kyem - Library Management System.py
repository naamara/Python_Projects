print()
print()
print("_________________________________________________________________________________________________")
print("\t\t\t\tWELCOME TO BLESSING'S LIBRARY",end="")
print("\U0001f600","\U0001f600","\U0001f600")
print("__________________________________________________________________________________________________")
print()
import re
import random
import datetime
import time

today = datetime.datetime.now()
year = today.year
month = today.month + 2
day = today.day
deadline = datetime.datetime(year, month, day)

                      #key    #value
StudentDetails = { } #name : [email address, AccountId, password ,books borrowed]
Generated_Email_Addresses = [ ] #Houses all the email addresses of all users
AvailableBooks = {"Lord Of The Rings": 5,"The Colour Of Magic":12,"A Game Of Thrones":25, "The Fellowship Of The Ring":16,"Pride And Prejudice":10,
                   "Fifty Shades Of Grey":4,"The Hating Game":6,"Vision White":14,"Gone With The Wind":2,"The Thorn Birds":7,
                    "The Calculating Stars":3,"Semiosis":13,"Space Opera":7,"The Book Of M":11,"The Gone World":13,"Blackfish City":15,
                    "Into Thin Air":8,"Into The World":12,"Treasure Island":5,"Journey To The Centre Of The Earth":6, "Heart of Darkness":4,
                     "The Power Of Positive Thinking":3,"Think And Grow Rich":0, "You Are A Badass":17, "You Can Heal Your Life":16}


def Book_Management(book):
    """
    This would add 5 books when the book is out of stock
    """
    global AvailableBooks
    if AvailableBooks[book] == 0:
        AvailableBooks[book] += 5



def CreateAccount():
    """
    This allows you to create your Account
    """
    global StudentDetails
    global Generated_Email_Addresses
    while True:
        print()
        print("Enter your name: ")
        print("Name should be valid and must contain numbers. eg: Blesing123 ")
        username= input().strip()
        print()
        if username in StudentDetails:
            print("Username already exists")
            print()
            continue
        if re.search(r"^[A-Za-z]+[A-Za-z]{4}[0-9]", username):
            break
        else:
            print("Invalid Username")
            print()

    while True:
        print("Enter Password")
        password = input(" ").strip()
        print()
        if  8<=len(password)<=16:
            if re.search(r"[A-Za-z]", password):
                if re.search(r"[0-9]", password):
                    if re.search(r"[*#@!^$%]", password):
                        break
                    else:
                        print("Password must contain special characters or symbols")
                        continue
                else:
                    print("Password must contain numbers")
                    continue
            else:
                print("Password must contain letters")
                continue
        else:
            print("Password must be between 8 - 16 characters")
            continue
    while True:
        print("Enter a valid email address: ")
        email_address = input().strip()
        print()

        if re.search("^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$", email_address) :
            if email_address not in Generated_Email_Addresses:
                break
            else:
                print("An account already exists with this email")
                print()
                continue
        else:
            print("Invalid email address")
            continue

    AcountId = random.randint(10000, 99999) #AccountId generator
    StudentDetails[username] = [email_address, str(AcountId), password]
    Generated_Email_Addresses.append(email_address)
    print("Please wait..............")
    time.sleep(5)
    print("..............")
    time.sleep(3)
    print(".........")
    time.sleep(2)
    print()
    print("Account Created Succesfully")
    print()
    print("____________________________________________")
    print(f"Your Account Id is {AcountId}")
    print("_____________________________________________")
    print()

def login():
    """
    Allows you to access an existing account
    """
    global StudentDetails
    while True:
        print("Enter your name: ")
        username = input().strip()
        print()

        if re.search(r"^[A-Za-z]+[A-Za-z]{4}[0-9]", username) and username:
            if username in StudentDetails:
                break
            else:
                print("Invalid Username")
                continue
        else:
            print("Invalid Username")
            continue

    while True:
        print("Enter your email address: ")
        email_address = input().strip()
        print()
        if email_address in StudentDetails[username]:
            break
        else:
            print("Invalid email address")
            continue

    while True:

        print("Enter your password: ")
        password = input().strip()
        if re.search(r"[A-Z0-9a-z*#@!^$%]", password):
            if password in StudentDetails[username]:
                break
            else:
                print("Invalid password")
                continue
        else:
            print("Invalid password")
            continue
    print("Access Granted")
    print()
# What the library does
def display_books( ):
    global AvailableBooks
    print()
    print("\t\t\tAvailable Books: ")
    for book in AvailableBooks:
        print("___________________________________________________________")
        print("\t\t\t", book)
        print("____________________________________________________________")
#What the user does
def request_a_book():
    global deadline
    my_deadline = deadline.strftime("%A, %B %d, %Y")
    global StudentDetails
    global AvailableBooks
    while True:
        print("Enter the book you are requesting: ")
        book = input( ).strip().title()
        if  isinstance(book, str):
            if book in AvailableBooks:
                break
            else:
                print("Book not available")
                continue
        else:
            print("Invalid input")
            continue
    print("You are supposed to enter your login credentials to secure your identity")
    while True:
        print("What is your name: ")
        name = input( )
        print()

        if re.search(r"[A-Za-z][A-Za-z][^0-9]",name) and isinstance(name, str):
            if name in StudentDetails:
                break
            else:
                print("Invalid name")
                continue
        else:
            print("Invalid Input")
    while True:
        print("What is your accountId: ")
        accountid = input()
        print()

        if re.search(r"^[0-9]", accountid) and len(accountid)==5 :
            if accountid in StudentDetails[name]:
                break
            else:
                print("Invalid AccountId")
                continue
        else:
            print("Invalid AccountId")
            continue
    if book not in StudentDetails[name] and AvailableBooks[book] >=1:
        StudentDetails[name].append(book)
        AvailableBooks[book]-=1
        print(f"You have borrowed {book} successfully")
        print("____________________________________________________________")
        print(f"The deadline for submission is on {my_deadline}")
        print("_____________________________________________________________")
        print()
    elif book in StudentDetails[name]:
        print(f"You have borrowed {book} already")
    elif book not in AvailableBooks:
        print(f"We dont have {book} in our Library. Management services will make Modifications")
    elif book in AvailableBooks and AvailableBooks[book]==0:

        print(f"{book} out of stock. Check up later")


def return_a_book():
    global StudentDetails
    global AvailableBooks
    while True:
        print("Which book are you returning: ")
        book = input().strip().title()
        if re.search(r"[A-za-z][^0-9]", book) and isinstance(book, str):
            if book in AvailableBooks:
                break
            else:
                continue
        else:
            continue
    print("You are supposed to enter your login credentials to secure your identity")
    while True:
        print("What is your name: ")
        name = input()
        print()

        if re.search(r"[A-Za-z][A-Za-z][^0-9]", name) and isinstance(name, str):
            if name in StudentDetails:
                break
            else:
                print("Invalid name")
                continue
        else:
            print("Invalid Input")
    while True:
        print("What is your accountId: ")
        accountid = input()
        print()

        if re.search(r"^[0-9]", accountid) and len(accountid) == 5:
            if accountid in StudentDetails[name]:
                break
            else:
                print("Invalid accountid")
                continue
        else:
            print("Invalid input")
            print()
            continue
    if book in StudentDetails[name]:
        StudentDetails[name].remove(book)
        AvailableBooks[book]+=1
        print(f"You have successfully returned {book}")
        print()
    else:
        print(f"{book} isn't inside your Archives!")


while True:
    try:
        print("________________________________________________________________")
        print("Press 1 to Login or access an existing account")
        print("Press 2 to Create Account")
        print("Press 3 to quit")
        print("_________________________________________________________________")
        print()
        useroption = int(input())


        if isinstance(useroption, int):
            if useroption ==1:
                login()
                status = False
                while True:

                    print("__________________________________________________________________________________________")
                    print("Press 1 to display available books")
                    print("Press 2 to request a book")
                    print("Press 3 to return a book")
                    print("Press 4 to return to previous menu ")
                    print("___________________________________________________________________________________________")
                    print()
                    useroption = int(input())
                    if isinstance(useroption, int):
                        if useroption == 1:
                            display_books()
                    else:
                        print("Invalid input")
                        continue
                    if isinstance(useroption, int):
                        if useroption == 2:
                            request_a_book()
                    else:
                        print("Invalid input")
                        continue
                    if isinstance(useroption, int):
                        if useroption == 3:
                            return_a_book()
                    else:
                        print("Invalid input")
                        continue
                    if isinstance(useroption, int):
                        if useroption == 4:
                            break
                    else:
                        print("Invalid input")
                        continue


        else:
            print("Invalid input")
            contnue
        if isinstance(useroption, int):
            if useroption == 2:
                CreateAccount()
                status = False
                while True:
                    print("_____________________________________________________________________")
                    print("Press 1 to display available books")
                    print("Press 2 to request a book")
                    print("Press 3 to return a book")
                    print("Press 4 to return to previous menu ")
                    print("______________________________________________________________________")
                    print()
                    useroption = int(input())
                    if isinstance(useroption, int):
                        if useroption == 1:
                            display_books()
                    else:
                        print("Invalid input")
                        continue
                    if isinstance(useroption, int):
                        if useroption ==2:
                            request_a_book()
                    else:
                        print("Invalid input")
                        continue
                    if isinstance(useroption, int):
                        if useroption == 3:
                            return_a_book()
                    else:
                        print("Invalid input")
                        print()
                        continue
                    if isinstance(useroption, int):
                        if useroption == 4:
                            break
                    else:
                        print("Invalid input")
                        print()
                        continue

        if isinstance(useroption, int):
            if useroption == 3:
                print()

                quit()
    except ValueError:
        print("Invalid input")
        print()
