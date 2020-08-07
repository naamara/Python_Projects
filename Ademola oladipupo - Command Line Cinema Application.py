import random
import datetime
from datetime import time
from datetime import date

#creating a class module to design a cinema ticket and food reservation for a one-time customer.

class cinemaBook():
	
	def __init__(self, member="", foodcost="", name="",address="",phoneno="", mail="", filmname="", filmtype="", foodname="", drink="", nname="", age="", sex="",seatno="", filmtime="", filmday="", billtotal="", movieprice = 1500): #initialization of variable that will be use in the class
		print("----------------------------------------------------")
		print("--------------Welcome To Demoore Cinema-------------")#i generate a welcome mesage
		print("----------------------------------------------------")
		
		self.seatno = seatno
		self.name = name
		self.address = address
		self.phoneno = phoneno
		self.mail = mail
		self.filmname = filmname
		self.filmtype = filmtype
		self.foodname = foodname
		self.drink = drink
		self.nname = nname
		self.sex = sex
		self.age = age
		self.billtotal = billtotal
		self.member = member
		self.foodcost = foodcost
		self.movieprice = movieprice
#declaring class function for each of the processes and activity that will be performed by the customer
			
	def inputdata(self): #i declare fuction to collect details of the customer
		self.name = input("Enter your full Name:  ")
		self.address = input("Enter your Address: ")
		self.phoneno = input("Enter your Phone Number: ")
		self.mail = input("Enter Your Email: ")
		
	def selectfilm(self):#declaring function to switch in between film to watch
		
		print("*******We have the following Types of Films*******")
		
		print("\t\t1. Hollywood")
		print("\t\t2. Bollywood")
		print("\t\t3. Nollywood")
		print("\t\t4. Yorubanolly")
		
		self.filmtype = ["Hollywood", "Bollywood", "Nollywood", "Yorubanolly"]
		while True:
			filmselect = int(input("Select your Desire Film Type e.g 1. Hollywood: "))
			self.filmname = str(input("Enter the Film to Watch: "))
			if filmselect == 1:
				print("You Have Opted for",self.filmtype[0]," Named",self.filmname)
			
			elif filmselect == 2:
				print("You Have Opted for",self.filmtype[1]," Named",self.filmname)
			
			elif filmselect == 3:
				print("You Have Opted For",self.filmtype[2]," Named",self.filmname)
			
			elif filmselect == 4:
				print("You Have Opted For",self.filmtype[3], " Named",self.filmname)
				break;
			else:
				print("You Must Select a Film Type")
			print("You Have Selected  a Film Price")
		
	def foodreservation(self):#declaring food reservation function to reserve food
		Hotdog = 200
		Popcorn = 100 
		Meatpie = 250
		Chinchin = 150
		Fishpie = 300
		print("*******************************************************")
		print("\tWe Have The Following Types of Foodsnack")
		print("\t\t1. Hotdog-> #200")
		print("\t\t2. Popcorn -> #100")
		print("\t\t3  Meatpie -> #250")
		print("\t\t4. Chinchin -> #150")
		print("\t\t5. Fishpie -> #300")
		print("******************************************************")
		print("\tWe have the folowing Drinks  at Default Price #100")
		print("\t\t1. Cocacola")
		print("\t\t1. Fanta")
		print("\t\t3. Sprite")
		print("\t\t4. Mirinda")
		print("\t\t5. Smoove")
		#declaring the default available drink to a function drinks
		drinks = ["Cocacola", "Fanta", "Sprite", "Mirinda", "Smoove"]
		
		food = int(input("Enter your Desire Food According to The number e.g 1. Hotdog\n"))
		self.foodname = input("Enter Desire Foodname:  ")
		drink = input("Enter Drink Name:  ")
		#allowing the user to input the quantity of drink and food she/he want
		drinkquantity = int(input("How Many Drinks:  "))
		foodquantity = int(input("How Many Food:  "))

		if food==1:
			food = Hotdog
		elif food == 2:
			food = Popcorn
		elif food == 3:
			food = Meatpie
		elif food == 4:
			food = Chinchin
		elif food == 5:
			food = Fishpie
		else:
			print("Enter Foodtype within, Hotdog, Popcorn, Meatpie, Chinchin, Fishpie")
		
		self.drink = 100
		total = (self.drink * drinkquantity) + (food * foodquantity)

		print("Your Reserved Food is",self.foodname,"With Quantity",foodquantity,"and",drinkquantity,drink,".Your Food Resevation Price Is",total)
		
	def ticketreservation(self):#ticketing and ticket time reservation
		print("*********Please Book Your Ticket Here and Reserve a Seat*****")#display welcome message
		reboot = ('Y')
		while reboot != ('N','NO','n','no'):
			print("1.Time of Movie")
			print("2.Ticket Reservation")
			press = int(input("\nPress your Option : \n"))
			if press == 1:
				print("********************************************")
				print("Select the Time of You Want to see the Film")
				print("\t\t1. Morning")
				print("\t\t2. Afternoon")
				print("\t\t3. Evening")
				movietime = int(input("Enter your Movie Time according to the number e.g 1. Morning"))
				day = int(input("Which Day: "))
				mon = int(input("Which Month: "))
				year = int(input("Which Year: "))
				if movietime == 1:
					self.filmtime = datetime.time(9,15,00)
					self.filmday = datetime.date(year,mon,day)
					print("Your Movie is Schedule in The Morning ")
				elif movietime == 2:
					self.filmtime = datetime.time(1,30,00)
					self.filmday = datetime.date(year,mon,day)
					print("Your Movie is Schedule in The Afternoon ")
				elif movietime == 3:
					self.filmtime = datetime.time(4,15,00)
					self.filmday = datetime.date(year,mon,day)
					print("Your Movie is Schedule in The Evening ")
				else:
					print("You Must Enter A Time")
				print("Your Film is Schedule",self.filmtime,self.filmday)
			elif press == 2:
				self.member = int(input("Enter no. of Ticket you wish : "))
				self.nname = []
				self.age = []
				self.sex = []
				self.seatno = []
				for i in range(self.member):
					names = input("Please Enter Name: ")
					self.nname.append(names)
					age = int(input("Please Enter Ages : "))
					self.age.append(age)
					seatnumber= random.randrange(500)
					self.seatno.append(seatnumber)
					sex  = input("Male or Female : ")
					self.sex.append(sex)
				reboot = str(input("Did you forget to Add Someone Please: "))
				if reboot in ('y','YES','yes','Yes'):
					restart = ('Y')
				else :
					x = 0
					print("The Total number of Ticket bought : ",self.member)
					for i in range(1,self.member+1):
						print("Ticket : ",i)
						print("Name : ", self.nname[x])
						print("Age  : ",self.age[x])
						print("Sex : ",self.sex[x])
						print("Seat number : ",self.seatno[x])
						x += 1			
	def display(self):#this is to display the bill generate by the customer
		print("\t\tYOUR CINEMA BILL IS")
		print("\t*****CUSTOMER DETAILS******")
		print("Customer Name is",self.name)
		print("Customer Address is",self.address)
		print("Customer Phone Number: ", self.phoneno)
		print("\t******Film Details*****")
		print("Your Preferrred Film Is: ",self.filmtype[filmselect])
		print("Your Preferred Film Name Is: ",self.filmname)
		print("Number of Ticket Booked : ",self.member)
		print("Names on Ticket Booked : ",self.nname)
		print("Seat number Reserved for each of them : ",self.seatno)
		print("Gender: ",self.sex)
		print("\t\t*****Food bill*****")
		self.foodcost = (self.drink*drinkquantity)+(food*foodquantity)	
		self.billtotal =  (self.movieprice * self.member) + self.foodcost		
		print("Total Cinema Cost :\n",self.billtotal)
		print("****************Thanks for Your Patronage, See You Next Time***************")

		

def usage():
	de = cinemaBook() #insantiating the class object by attaching it to a variable "de".
	
	#creating a sort of display of available option for the customer to be able to choose between the option
	while (1):#looping through the option
	#displaying option
		print("1. Enter Customer Data")
		print("2. Select Your Desire Film")
		print("3. Food Reservation")
		print("4. Reserve A Ticket")
		print("5. Display and Print Output")
		print("6. CLOSE")
		
		option = int(input("Enter Your Option : "))
		if (option ==1):
			
			de.inputdata()
			
		if (option ==2):
			
			de.selectfilm
			
		if (option == 3):
			
			de.foodreservation()
			
		if (option == 4):
			
			de.ticketreservation()
			
		if (option == 5):
			
			de.display
			
		if (option == 6):
			
			quit()
		exit(0)
usage()