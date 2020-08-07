#import the module sqlite3
import  sqlite3
import json
#imports the class datetime from datetime module
from datetime import datetime

#creates an heading for the program
print("°"*15 + "STOCK TAKING SYSTEM" + "°" *72)

#prints the date in which the program is executed
today = datetime.today()
print(today.strftime("\t\t    %m-%d-%Y"))

#prints different quotes on different days of the weeks
day = today.strftime("%A")
if day == "Monday":
	print("'Success is not final; failure is not fatal: ".center(50))
	print(" It is the courage to continue that counts.'".center(40))
elif day == "Tuesday":
	print("'Opportunities don't happen.".center(50))
	print("You create them.'".center(50))
elif day == "Wednesday":
	print( "'The only limit to our realization of tomorrow".center(50))
	print(" will be our doubts of today.'".center(50))
elif day == "Thursday":
	print( '"If you can dream it, you'.center(50))
	print("can do it.'".center(50))
elif day == "Friday":
	print( "'In order to succeed, we must first".center(50))
	print("believe you can'".center(50))
elif day == "Saturday":
	print("'The secret of success is to do the common thing".center(50))
	print("uncommonly well.'".center(50))
elif day == "Sunday":
	print("'The secret to success is to know something". center(50))
	print("nobody else knows. '".center(50))

#defines a function to create tables
def Database():
#makes the variables conn and cursor global to the entire program
	global conn, cursor
	#connects to the data base
	conn  =  sqlite3 . connect ( 'stock.sqlite' )
#needed to obtain data one row at a time
	cursor  =  conn.cursor ()

	#create the stock_taking table to store data of stock
	cursor.execute("CREATE TABLE IF NOT EXISTS stock_taking(product TEXT, unit TEXT, quantity INT NOT NULL, price INT NOT NULL, unique(product, unit))")
	
	#creates the sales table to store goods sold
	cursor.execute("CREATE TABLE IF NOT EXISTS sales(product_sold TEXT, product_unit TEXT, quantity_sold INT NOT NULL)")
	
	#creates purchases table to store goods bought
	cursor.execute("CREATE TABLE IF NOT EXISTS purchases (product_sold TEXT, product_unit TEXT, quantity_sold INT NOT NULL)")


#defines a function to determine which operation the user wants to carry out		
def action():
	print("Enter 1: To insert into existing stock")
	print("Enter 2: To update stock price")
	print("Enter 3: To update stock quantity")
	print("Enter 4: To delete stock")
	print("Enter 5: To Retrieve stock")
	print("Enter 6: To determine the total worth of your stock")
	print("Enter 7: To insert sales")
	print("Enter 8: To enter goods purchased")
	print("Enter 9: To Delete the entire stock")
	print("Press 10: To Quit")

#Prompts the user for an input of an integer and handles Value Error exception
def menu():
	try:
		x = int(input("What to do want to do? Enter any of the options above... "))
	except ValueError:
		print("Oops the value you entered is wrong!!")
		return menu()
	else:
		return x


#Defines an Excpetion to tell the user to input only text for product name
class StringIntegerError(Exception):
	""" Only texts is required"""
	pass

#defines a function to insert product, unit of measure,quantity and price into stock_taking table
def Insert():
	Database()
	try:
#prompts the user for inputs
		p_name= input('Product name: ').lower()
		p_unit = input('Unit of product measure: ').lower()
		p_qty= int(input('Quantity: '))
		p_price = int(input('Price: '))
		
		if p_name.isdigit() == True:
			
			#raises the predefined StringIntegerError
			raise StringIntegerError
		elif type(p_qty) == str or type(p_price)  == str:

#raises ValueError Exception in case a non integer is entered
			raise ValueError
		sql="SELECT * from stock_taking;"
		cursor.execute(sql)
		record = cursor.fetchall()
		for row in record:
			if p_name in row[0] and p_unit in row[1]:

#raises sqlite3.IntegrityError
				raise sqlite3.IntegrityError
	except StringIntegerError:
		print("The input for the product name is invalid, text only is required for the product name!!")

	except ValueError:
		print("The input is invalid, please enter numbers")

#handles error in case there is duplicate of product and unit
	except sqlite3.IntegrityError:
		print("The product name and unit you entered is already in stock, Enter 3 to update the quantity of the product")

#Executes the syntax for inserting stock when there's no error
	else:
		cursor.execute("""
		INSERT INTO
		stock_taking(product, unit, quantity, price)
		VALUES (?,?,?,?)""", (p_name, p_unit, p_qty, p_price))
		conn.commit ()
		print("Product added into stock successfully")	
		return (p_qty, p_name, p_unit, p_price)
	

#defines a function to update the price of a product
def Update_price():
	Database()
#Handles ValueError exception if integer is not inputed
	try:
		p_name =  input("Enter  the product name ").lower()
		p_unit  =  input("Enter the unit of measurement ").lower()
		p_price = int(input("Enter new price "))

#prompts user for input of price and product name and Handles ValueError and StringIntegerError
		if type(p_price) == str:
			raise ValueError
		elif p_name.isdigit() == True:
			raise StringIntegerError
	except ValueError as e:
		print(f"The value you inputed is invalid. The error is {e}.")
	except StringIntegerError:
		print("The input is invalid, please enter texts only for the product name!!")
		
#Executes the syntax for updating price when there's no error		
	else:
		cursor.execute( "update stock_taking set price=? where product=? AND unit = ?;", (p_price, p_name, p_unit))
		conn.commit()		
		return p_name, p_unit, p_price

#defines the function to update quantity of goods
def Update_quantity():
	Database()
#Handles ValueError and StringIntegerError exception if integer is not inputed
	try:
		p_name=  input("Enter  the product name ").lower()
		p_quan = int(input("Enter new quantity "))
		p_unit = input("Enter the unit of measurement ").lower()
		if type(p_quan) == str:
			raise ValueError
		elif p_name.isdigit() == True:
			raise StringIntegerError
	except ValueError:
		print("The value you inputed is invalid!!")
	except StringIntegerError:
		print("Please enter text only for the product name!!")
	else:
#executes the update price syntax if there is no error
		cursor.execute( "update stock_taking set quantity = ? where product=? AND unit = ?;", (p_quan, p_name, p_unit))
		conn.commit()
		return p_name, p_unit, p_quan


#defines function to delete a product from stock available
def Delete():
	Database()
	try:
		p_name = input("Enter the product to delete: ").lower()
		p_unit = input("Enter the unit of measurement ").lower()
		qry="DELETE from stock_taking where product=? AND unit = ?;"
		sql="SELECT * from stock_taking;"
		if p_name.isdigit() == True:
			raise StringIntegerError
	except StringIntegerError:
		print("The input for the product is invalid!!")
	else:
		cursor.execute(sql)
		rec = cursor.fetchall()
		cursor.execute(sql)
		row = cursor.fetchone()
		for row in rec:
#checks if the product inputted for delete is in stock
			if p_name in row[0] and p_unit in row[1]:
			#executes the syntax
				cursor.execute(qry, (p_name, p_unit))
			#prints if inputted item is in stock
				print("product deleted successfully!!")
			elif p_name  not in row[0] and p_unit  not in row[1]:
				print("product is not in stock, wrong input!!")
		if row== None:
			print("Nothing to delete, the stock is empty")

	
#commits the changes to the database
	conn.commit()

#closes the database
	conn.close()
	
#defines a function to delete the entire stock
def Delete_all():
	Database()
	qry="DELETE from stock_taking;"

#executes the syntax qry
	cursor.execute(qry)

#commits changes to the database
	conn.commit()
#closes the database connection
	conn.close()
	print(" Entire record deleted successfully")

#defines function to retrieve the available stock
def Retrieve():
	Database()
	sql="SELECT * from stock_taking;"	
#Executes the syntax sql
	cursor.execute(sql)

#fetches the data in the stock_taking table
	record = cursor.fetchone()
	if record is None:
		print("The stock is empty")
	else:
		cursor.execute(sql)
		rec = cursor.fetchall()
		for row in rec:
		#creates a dictionary for items
			items= {"Product":row[0], 			"Unit of measure":row[1], "Quantity":row[2], "Price": row[3]}
			#prints each element of dictionary on separate lines
			print(json.dumps(items, indent=4))
		

#defines the function to determine the total worth of the available stock
def Total_worth():
	Database()
	try:
		sql = "SELECT SUM(price*quantity) AS total_price FROM stock_taking;"

#Executes the action of calculating the total price of stock available
		for row in cursor.execute(sql):
	
		#converts the total worth in tuple to an integer
			total = int(''.join(map(str, row)))
#prints the total worth of goods in stock
			print(f" The total worth of your stock is {total}")

#prints an error message when the stock is empty
	except ValueError:
		print("There is nothing in the  stock")
	else:
		return total

#Function defined to deduct quantiy of goods sold from the available stock quantity
def Deduct_sales(a):
	try:
		Database()
		sql = "UPDATE stock_taking SET quantity = quantity - ? WHERE product = ? AND unit = ?;"
#executes the action of deducting sales
		cursor.execute(sql, a)
#commits changes to the database
		conn.commit()

#closes the database connection
		conn.close()
	except ValueError:
		pass

#Function defined to enter goods sold into the sales table previously created
def Insert_sales( ):
	Database()
	try:
		p_name= input('Product name: ').lower()
		p_unit = input('Unit of product measure: ').lower()
		p_qty= int(input('Quantity: '))
		if p_name.isdigit() == True:
			raise StringIntegerError
		elif type(p_qty)  == str:
			raise ValueError
	except StringIntegerError:
		print("Enter all text please for the product name!!")
	except ValueError:
		print("The value you inputed is wrong, please enter a number")
	else:
		#Executes the syntax
		qry = """
			INSERT INTO
			sales(product_sold,product_unit, quantity_sold)
			VALUES (?,?,?)"""

		sql = conn.execute(qry, (p_name,p_unit, p_qty))
#commits the transaction to the database
		conn.commit()
		#closes the database connection
		conn.close()
		return (p_qty, p_name, p_unit)

#defines a function to add new purchase quantity to the current stock quantity when there is a new purchase
def Add_purchases(a):
	Database()
	try:
		sql = "UPDATE stock_taking SET quantity = quantity + ? WHERE product = ? AND unit = ?;"
#executes the action of adding purchases
		cursor.execute(sql, a)
#commits changes to the database
		conn.commit()

#closes the database connection
		conn.close()
	except ValueError:
		pass

#defines a function to allow the user enter new purchases
def Insert_purchases():
	Database()
	try:
		p_name= input('Product name: ').lower()
		p_unit = input('Unit of product measure: ').lower()
		p_qty= int(input('Quantity: '))

#Executes the syntax
		qry = """
		INSERT INTO
		purchases(product_sold,product_unit, quantity_sold)
		VALUES (?,?,?)"""

		if p_name.isdigit() == True:
			raise StringIntegerError
		elif type(p_qty)  == str:
			raise ValueError
	except StringIntegerError:
		print("Enter all text please for the product name!!")
	except ValueError:
		print("The value you inputed is wrong, please enter a number")
	else:
		conn.execute(qry, (p_name,p_unit, p_qty))
#commits the transaction to the database
		conn.commit()
#closes the database connection
		conn.close()
		return (p_qty, p_name, p_unit)

#defines function to check if the product entered into sales is in line with what is in stock
def Check_sales(a):
	Database()
	try:
		sql = "SELECT EXISTS(SELECT* from stock_taking WHERE quantity = ? OR product = ? AND unit = ?);"
		cursor.execute(sql, a)
#detrmines if the product entered into the sales table is available in stock
		if cursor.fetchall()== [(1,)]:
			print("The qujiantity sold has been successfully deducted from the quantity in stock!!")
		cursor.execute(sql, a)

#determines if the product to be updated is not in stock
		if cursor.fetchall() == [(0, )]:
			print("The product you entered is not in stock, enter 1 to insert it  into stock")

#Directs the user to the insert function if the product entered is not in stock
			new = input("Do you want to add the product to stock, yes/no ").lower()
			while new != 'yes' and new != 'no':
				new = input("Do you want to add the product to stock, yes/no ").lower()
			if new =="yes":
				Insert()
			elif new == "no":
				pass
	except ValueError:
		pass

#defines function to check if the product entered into purchases is in line with what is in stock
def Check_purchases(a):
	Database()
	try:
		sql = "SELECT EXISTS(SELECT* from stock_taking WHERE quantity != ? AND product = ? AND unit = ?);"
		cursor.execute(sql, a)#executes the syntax

#determines if the product to be updated is in stock
		if cursor.fetchall() == [(1, )]:
			print("The quantity purchased has been successfully added to the quantity in stock!!")
#executes the syntax with the execute function accepting an extra parameter
		cursor.execute(sql, a)
		
#determines if the product to be inserted in purchase table is not in stock
		if cursor.fetchall() == [(0, )]:
			print("The product you entered is not in stock")

#Directs the user to the insert function if the product entered is not in stock
			new = input("Do you want to add the product to stock, yes/no ").lower()
			while new != 'yes' and new != 'no':
				new = input("Do you want to add the product to stock, yes/no ").lower()
			if new =="yes":
				Insert()
			elif new == "no":
				pass
	except ValueError:
		pass


#defines function to check if the price of the product updated is in line with what is in stock
def Check_updprice(a):
	Database()
	try:
		sql = "SELECT EXISTS(SELECT* from stock_taking WHERE product = ? AND unit = ? AND price = ?);"
		cursor.execute(sql, a)

#determines if the product to be updated is not in stock
		if cursor.fetchall()== [(1,)]:
			print("The product you entered is in stock, update successful!!")
		cursor.execute(sql, a)
#determines if the product to be updated is not in stock
		if cursor.fetchall() == [(0, )]:
			print(" The product you entered is not in stock")
			
#Directs the user to the insert function if the product entered is not in stock
			new = input("Do you want to add the product to stock, yes/no ").lower()
			while new != 'yes' and new != 'no':
				new = input("Do you want to add the product to stock, yes/no ").lower()
			if new =="yes":
				Insert()
			elif new == "no":
				pass
	except ValueError:
		pass

	
#defines function to check if the quantity of the product updated is in line with what is in stock
def Check_updquan(a):
	Database()
	try:
		sql = "SELECT EXISTS(SELECT* from stock_taking WHERE product = ? AND unit = ? AND quantity = ?);"
		cursor.execute(sql, a)
#determines if the product to be updated is in stock or not
		if cursor.fetchall()== [(1,)]:
			print("The product you entered is in stock, update successful!!")
		cursor.execute(sql, a)
		if cursor.fetchall() == [(0, )]:
			print(" The product you entered is not in stock")

#determines if the user wants to input in product in stock if absent
			new = input("Do you want to add the product to stock, yes/no ").lower()
			while new != 'yes' and new != 'no':
				new = input("Do you want to add the product to stock, yes/no ").lower()
			if new =="yes":
				Insert()
			elif new == "no":
				pass
	except ValueError:
		pass

#calls the function action()
action()
#calls the function menu() and assigns it to a variable
run = menu()

#calls each function when the user inputs the intger 1 - 10
while True:
	if run == 1:
		Insert()
		run = menu()
	elif run == 2:
		row = Update_price()
		Check_updprice(row)
		run = menu()
	elif run == 3:
		row = Update_quantity()
		Check_updquan(row)
		run = menu()
	elif run == 4:
		Delete()
		run = menu()
	elif run == 5:
		Retrieve()
		run = menu()
	elif run == 6:
		Total_worth()
		run = menu()
	elif run == 7:
		row=Insert_sales()
		Deduct_sales(row)
		Check_sales(row)
		run = menu()
	elif run == 8:
		row= Insert_purchases()
		Add_purchases(row)
		Check_purchases(row)
		run = menu()
	elif run == 9:
		delt = input("Are you sure you want to delete the entire record?yes/no:  ").lower()
		while delt != 'yes' and delt != 'no':
			delt = input("Are you sure you want to delete the entire record?yes/no:  ").lower()
		if delt == 'yes':
			Delete_all()
		else:
			pass
		run = menu()
	elif run == 10:
		break	
#If a number above 10 is inputted, this is printed
	else:
		print("You have to enter a value between 1 and 10, try again!! ")
		run = menu()