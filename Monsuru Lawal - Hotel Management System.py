from datetime import datetime
import string
import random
import time
from pprint import pprint
from sys import exit

name,number,mail,address,Night,code,details,database,price,Atm,Price,pincode,Roomcode,My_select,rum= "Admin","08162210489","","No 17, Surulere. Soka, Ibadan","","",{},{"Admin" : {"Name" : "Monsuru",
"Number" : "08162210489",
"Roomcode" : "001",
"Number": "08162210489"}
},0,"",1000000,"001","","",""
print("-"*60)
print("\t Welcome to SNP Hotel Management portal \n \t    We are Happy to have you here !!! \n ".upper())
print("-"*60)
def Verification():
	reserve= input("\n\nDo you have a reservation here ? Yes or No ! : ").title()
	if reserve=="No":
		Welcome_page()
	elif reserve =="Yes" :
		print("Please let us verify your booking!!")
		Login()
	else:
		Verification()
	
	
def Welcome_page():
	global database,details,pincode,name,address,number
	rand="".join((random.sample(string.digits,3)))
	print("\n Please let's have your details for room allocation !")
	print("Fill in your details ")
	print()
	name=input("Enter your Full name : ")
	while len(name)<3:
		print("Invalid Name, Please Enter a valid name!")
		name =input("Enter your full name : ")
	address = input("Enter your full address : ")
	while address.isalpha()==True or address.isdigit()==True:
		print("Invalid Address, please your address details should combined Texts and Digit !")
		address=input("Enter your full address : ")
	number=input("Please enter your phone number : ")
	while number.isalpha()==True or len(number) !=11:
		print("Invalid Phone number, number should be 11 by counting and must be strictly numbers ")
		number=input("Please enter your phone number : ")
	pincode=rand
	print(f"Your Pincode is {pincode}")
	
	details["Full_name"] =name
	details["Address"] = address
	details["Number"] = number
	details["Pincode"] = pincode
	
	database[name]=details
	
	
	print("\n\tYour information is saved...\n Your details is \n ")
	print("-"*60)
	pprint(details)
	print("-"*60)
	details={}
	More=input("Would you like to book more reservations ? Yes or No !").title()
	if More=="Yes":
		Verification()
	elif More =="No":
		print("Let's proceed for Room Bookings")
		level()
		
	else:
		while More !="Yes" or More !="No":
			More=input("Your choice does not exist. please choose valid options (Yes or No) : ").title()
	Login()
	level()
	
def Login():
	global name,pincode,My_select
	check_name=input("Please enter the name used for the booking : ")
	code=input("Enter your Pincode : ")
	print("\n Please wait while we're verifying your informations ")
	time.sleep(3)
	if check_name in database.keys() and code in database[check_name].values():	
		print("\tYes,  you have a booking here already ! ")
		name=check_name
		pincode=code
		level()
	
	else:
		print("You do not have any reservation yet  ")
		book= input("Will you book a reservation now ? Yes or No ! : ").title()
		if book=="Yes":
			Welcome_page()
		else:
			print("You can take your leave now")
def level():
	global price,Night,My_select
	print("\n\t\t       You are welcome here".upper())
	print("\n \t\t Select the room of your choice ".upper())
	print("\n\t 1. Master_of All : \t #60,000\n\t 2. Comfortable : \t #40,000 \n\t 3. Moderate :\t \t #20,000 \n\t 4. Mini : \t \t  #5,000" )
	My_select = input ("\n Select any of the options above : ")
	if My_select=="1":
		print()
		print("Hey! , You chose Master_of_All Room ")
		
		Night=int(input("\tHow many Nights you intend to spend : "))
		price =60000 * Night
		Room()

	elif My_select=="2":
		print("Hey! , You chose Comfortable Room ")
		
		Night=int(input("\tHow many Nights you intend to spend : "))
		price =40000* Night
		Room()
		
	elif My_select =="3":
		print("Hey! , You chose Moderate Room ")
		
		Night=int(input("\tHow many Nights you intend to spend : "))
		price =20000 * Night
		Room()
		
	elif My_select =="4":
		print("Hey! , You chose Mini Room ")
		
		Night=int(input("\tHow many Nights you intend to spend : "))
		price =5000 * Night
		Room()
	while My_select !="1" or My_select !="2" or My_select !="3" or My_select !="4" :
		print("You are selecting invalid code , please select the correct options : ")
		level()
	
def Room():
	global price,rum
	print("\n We have  other activies you can engage in \n They includes : ")
	print("\t 1.  Swimming : \t  #5,000 \n \t 2.  Table Tennis cost :  #3,000 \n\t 3.  Full Packaged Food : #4,000 \n\t 4.  Not Interested ")
	new_price=input("Please select any of the option above : ")
	if new_price =="1":
		price +=5000
		print(f"Your Bill in total is #{price} ")
	elif new_price=="2":
		price +=3000
		print(f"Your Bill in total is #{price} ")
	elif  new_price=="3":
		price +=4000
		print(f"Your Bill in total is #{price} ")
	else:
		print(f"Your Bill is #{price}")
		receipt()
		exit()
		
	Activity = input("Do you wish to engage in more activities ? Yes or No : ").title()
	if Activity == "No":
		print(f"\t\tYour Price is #{price} ")
		receipt()
		exit()
	elif Activity == "Yes":
		while Activity=="Yes":
			Room()
			exit()
	while Activity !="Yes" or Activity != "No":
		Activity = input("Do you wish to engage in more activities ? Yes or No : ").title()
		print("Wrong input!!! ")
		if Activity == "No":
			print(f"\t\tYour Price is #{price} ")
			receipt()
			exit()
		elif Activity == "Yes":
			while Activity=="Yes":
				Room()
				exit()
				
def valid():
	global Atm,Roomcode
	while Atm.isdigit()==False:
		Atm=input("Your Atm is strictly numbers : ")
	numbers=Atm
	num= list(numbers)
	number=[]
	for k in num:
		k = int(k)
		number.append(k)
	number=number[::-1]
	list1,list2,list3,list4,list5=[],[],[],[],[]
	n=0
	for i in number:
		
		if number.index(i,n)%2==1:
			list1.append(i)
			n+=1
		else:
			list2.append(i)
			n+=1
	for j in list1:
		j=j*2
		list3.append(j)
	for j in list3:
		j=str(j)
		if len(j)==2:
			list4.append(j)
		else:
			c=int(j)
			list5.append(c)
	for y in list4:
		g=int(y[0])
		u=int(y[1])
		x=g+u
		list5.append(x)

	for o in list2:
		
		list5.append(o)
	new_list=sum(list5)	

	if new_list%10==0:
		return "Valid Pin"	
	else:
		return "Invalid Pin"		
	
def atm():
	global Atm,Roomcode	
	print("-"*60)
	print("\n \t\tSession for Payment!!".upper())
	print("-"*60)
	Atm=input("Enter your Valid Atm 16 Digit Numbers : ")
	Roomcode=input("Enter your Pincode : ")
		
def receipt():
	global price,Roomcode,pincode,address,Price,My_select,rum
	if My_select =="1":
		rum="Master_of All"
	elif My_select =="2":
		rum="Comfortable"
	elif My_select =="3":
		rum="Moderate"
	elif My_select =="4":
		rum="Mini"	
	atm()
	valid()
	print("\nPlease wait for few seconds while we check for the authentication of your card details.........")
	time.sleep(3)
	if valid()=="Valid Pin" and Roomcode==pincode:
		print("\n\tAuthentication successful!!")
		
		print(f"\nThe balance in your Account is #{Price}\n")
		print(f"And your new balance is #{Price-price} \n \t\t Your Payment was Successful !!!")
		print("\n\t Please wait, while we process your receipt ....")
		time.sleep(5)
		print("-"*60)
		print("\t\t\t Your Receipt")
		print("-"*60)
		print(f" Name  : {name} \n Address : {address} \n Contact : {number} \n Pincode : {pincode} \n DaySpent : {Night} \n Room Type: {rum} \n Amount Paid : #{price} \n\n " )
		print("-"*60)
		print(f"\t Designed by Monsaw       {datetime.now()} ")
		print("-"*60)
	while valid() != "Valid Pin" or Roomcode!=pincode:
		print("\n You enter either Invalid Card Pin or Your Pincode is incorrect !!")
		receipt()
	print("\n Do you wish to perform task again or Exit?")
	exite=input("\n Press Yes to Continue or Anykey to Exit the program : ").title()
	print()
	if exite =="Yes":
		print("-"*60)
		print("\t Welcome to SNP Hotel Management portal \n \t    We are Happy to have you here !!! \n ".upper())
		print("-"*60)

		Verification()
	else:
		exit()		

Verification()
