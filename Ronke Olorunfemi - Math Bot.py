from math import sin, cos, tan, asin, acos, atan, degrees, radians
import cmath
from statistics import mean, mode, median, variance, stdev
from sys import exit
status, status1, status2, status3= False, False, False, False
stat, stat1, stat2, stat3, stat4, stat5 = False, False, False, False, False, False
view, view1, view2, view3 = False, False, False, False 
user = False 
close = False 
trig, trig1, trig2 = False, False, False
print("_ "*27)

print("Hello! Welcome to math bot".upper().center(50, "*"))

print()

print("\t  I can solve mathematical problems on the following topics".upper().center(50, "*"))
print("_ "*27)
print()

def equation():
	global status1, status2, status3
	

	print()
	
	print("\t  Equation".center(50)) 
	
	print()
	print("The only available subtopic under Equation is;")
	print()
	print("\t Quadratic Equation.")
	print()
	
	print("Enter only the values of a, b, c")
	print()

	#this is to make sure that the values of a, b, c is either an integer or float. 
	while status1 == False:
		try:
			a = float(input("Enter a: "))
			
			if type(a) == float:
				status1 = True
			else:
				raise ValueError 
		except ValueError:
			print()
			
			print("Invalid input", "Kindly re-enter a.", sep = "\n")
			
			print()
	
	while status2 == False:
		try:
			b = float(input("Enter b: ")) 
			
			if type(b) == float:
				status2 = True
			else:
				raise ValueError
		except ValueError:
			print()
			print("invalid input", "kindly re-enter b.", sep = "\n")
			print()
			
	while status3 == False:
		try :
			c = float(input("Enter c: "))
				 
			if type(c) == float:
				status3 = True
			else:
				raise ValueError 
		except ValueError:
			print()
			print("invalid input", "kindly re-enter c.", sep = "\n")
			print()
			
	
	#calculating the descriminant
	d = (b**2 ) - (4*a*c)
	
	#checking out the two solutions of quadratic equation. 
	solution1 = (-b-cmath.sqrt(d))/(2*a)
	solution2 = (-b+cmath.sqrt(d))/(2*a)
	print("Solutions to the equation are {0} and {1}".format(solution1, solution2))
	print("_ "*27)
	
def topics():
	global status 
	global view, view1, view2, view3
	global user
	global stat
	
	print ("1.Equation", "2.Statistics", "3.Trigonometry", "4.Exit" , sep = "\n")
	print("_ "*27)
	print()
	
		# this is to check if the user will like to view the overview of the topics or not			
	while user is False and view is False:
		try:
			
			print("Would you love an overview of the topics above?".title())
			
			print() 
			user_input = input("Enter  'yes' or 'no' please: ").lower()
			if user_input.isalpha() == False or user_input not in (" 'no' or 'yes' "):
				print ()
				print("Invalid input!", "Enter  'yes', 'no' please.",sep = "\n")
			elif user_input == "yes" :
				print ("Kindly proceed!") 
				
			
				user = True
			elif user_input == "no":
			
				view = True
			else:
				raise ValueError 
		except ValueError:
			print()
			

	while view is  False:
		try:
			print()
			over_view = int(input("Enter 1 or 2 or 3   to choose your overview topic: "))
			 
		
			if over_view ==1:
				view = True
				print()
				print("\t Overview of Quadratic Equation".center(50)) 
				print("In  algebra, a quadratic equation(from the Latin quadratus for 'square') is any equation that can be rearranged in standard form as where x represents an unknown, and a, b and c represents an unknown numbers, where  a is not equal to zero, if a = 0,then the equation is linear and not quadratic.", "The standard form of Quadratic Equation is : ax\N{Superscript Two} + bx + c = 0", sep = "\n")
				
				print("_ "*27)
				
				
			elif over_view ==2:
			     view = True
			     print()
			     print("\t Overview of Statistics".center(50))
			     print("The information that gives a quick and simple description of the data. It can include mean, mode, variance e.t.c.")
			     print("_ "*27)
			     
			elif over_view ==3:
				view = True
				print()
				print("\t Overview of Trigonometry".center(50))
				
				print("Trigonometry studies relationships between side lengths and angles of triangles, sin, cos and tan are basically just functions that relate an angle with ratio of two sides in a right triangle.","asin(x). This function returns the inverse of the sine, which is also known as arc sine of a complex number, the range is - 1 to 1, acos(x) returns the cosine inverse of parameter x, the range is - 1 to +1.", sep = "\n")
				print("_ "*27)
			
				
			else:
				raise ValueError 
		except ValueError :
			print()
			print("invalid input!")
			
		# this  gives  invocation to each topic	
	while status is False:
		try:
			print()
			
			
			choice = int(input("Choose your topic and 4 to exit: "))
			if choice == 1:
				status = True
				equation()
			elif choice == 2:
				status = True 
				statistics()
			elif choice == 3:
				trigonometry()
			

			elif choice == 4:
				print()
				print("You just exited the program", "Goodbye!", sep = "\n")
				
				
				
				exit() #this will closed the program automatically. 
			
			     
			     
			else:
				raise ValueError
		except ValueError:
			print()
			
			print("Invalid input!")
			
	# Function definition for statistics 		
def statistics():
	global stat, stat1, stat2, stat3, stat4, stat5, stat6, stat7
	global status
	
	
	print()
	print("\t  Statistics".center(50)) 
	
	print()
	
	print("The available sub topics under statistics are :", "1.Mean", "2.Mode", "3.Median", "4.Variance and", "5.Standard deviation", "6.main menu", "7.Exit", sep = "\n") 
	print()
	print("_ "*27)
	
	#
	
	while stat is False:
		try:
			print()
			 
			statistics = int(input("choose your choice: ")) 
			print()
			 
	
			if statistics == 1:
				stat1 = True
			
				
				#calculating mean
				print("You are about to calculate mean")
				
				print()
				mean_values = input("Enter your comma-separated sequence of numbers: ")
				user_input_values = mean_values.split(",")
				int_input_list = [int(element) for element in user_input_values]
				answer = mean(int_input_list)
				print(f"Your mean result is {answer}")
				stat = True 
				status = True 
				print("_ "*27)
				 
				
				
			elif statistics == 2:
				
			      #mode calculation, a number must appear at least two times in the sequence. 
			      
			      print("You are about to calculate mode")
			      stat2 = True
			      print()
			      status = True
			      mode_values = input("Enter your comma-separated sequence of numbers: ")
			      user_input_values = mode_values.split(",")
			      int_input_list = [int(element) for element in user_input_values]
			      answer = mode(int_input_list)
			      print(f"Your mode result is {answer}")
			      print("_ "*27)
			      stat = True 
			      
			      
			elif statistics == 3:
				stat3 = True
				 
				
				#median calculation
				print("You are about to calculate median")
				print()
				
				median_values = input("Enter your comma-separated sequence of numbers: ")
				user_input_values = median_values.split(",")
				int_input_list = [int(element) for element in user_input_values]
				answer = median(int_input_list)
				print(f"Your median result is {answer}")
				
				status = True
				print("_ "*27)
				stat = True 
			 
			 
				
			elif statistics == 4:
				stat4 = 4
				
				#variance calculation
				print("You are about to calculate variance")
				print()
				status = True
				variance_values = input("Enter your comma-separated sequence of numbers: ")
				user_input_values = variance_values.split(",")
				int_input_list = [int(element) for element in user_input_values]
				answer = variance(int_input_list)
				print(f"Your variance result is {answer}")
				print("_ "*27)
				stat = True 
				
				
			elif statistics == 5:
				# calc of stdev
			    print(" You are about to calculate standard deviation")
			    stat5 = True
			    
			    print()
			    status = True
			    stdev_values = input("Enter your comma-separated sequence of numbers: ")
			    user_input_values = stdev_values.split(",")
			    int_input_list = [int(element) for element in user_input_values]
			    answer = stdev(int_input_list)
			    print(f"Your stdev result is {answer}")
			    print("_ "*27)
			    stat = True
			    		
			elif statistics == 6:
				stat6 = True
				print()
				
				topics()
				stat = True 
				
				status = False 
				 
			
			    
			elif statistics == 7:
				stat7 = True
				print()
			
				print("You just exited the program", "Goodbye!", sep = "\n")
				exit()
				print("_ "*27)
				
				
				      
			else:
				raise ValueError
		except ValueError:
			print()
			print("Invalid input!")
			
	# function definition for trigonometry		
def trigonometry():
	global trig, trig2, trig3, trig4, trig5, trig6,trig7, trig8, trig9
	global status
	
	print()
	print("\t  Trigonometry". center(50)) 
	
	print()
	
	print("The available sub topics under trigonometry are :", "1.sine", "2.cosine", "3.tangent", "4.arc sine ", "5.arc cos" , "6.arc tangent", "7.degree", "8.radians", "9.main menu", "10.exit" , sep = "\n") 
	print()
	print("_ "*27)
	
	
	
	while trig is False and status is False:
		try:
			print()
			trigonometry = int(input(" choose your choice: ")) 
			print() 
			if trigonometry == 1:
				trig1 =True
				
				#calculating sine
				sine_value = int(input("Enter a value in degrees : "))
				#this convert sine value into radians
				rad_in_sine = radians(sine_value)
				print()
				answer = round(sin(rad_in_sine), 4)
				print()
				print(f"sin {sine_value}\N{Superscript Zero} = {answer}")
				status = True
				
				print("_ "*27)
			
				
				#calc of cos
				
				trig = True
			elif trigonometry == 2:
				trig2 = True
				cos_value = int(input("Enter a value in degrees: "))
				
				#this convert cos value into radians. 
				rad_in_cos = radians(cos_value)
				print()
				
				answer = round(cos(rad_in_cos))
				print(f"cos  {cos_value}\N{Superscript Zero} = {answer}")
				
				
					
				status = True
				print("_ "*27) 
				
				
			elif trigonometry == 3:
				#calc of Tan
				trig3 = True
				tan_value = int(input("Enter a value in degrees : "))
				
				#this convert tan value into radians 
				rad_in_tan = radians(tan_value)
				print()
				
				answer = round(tan(rad_in_tan))
				print(f"tan  {tan_value}\N{Superscript Zero} = {answer}")
				
				
				print()
				status = True
				print("_ "*27) 
				
				
			elif trigonometry == 4:
				#calc of arc sine
				trig4 = True
				arcsine_value = float(input("Enter a value: "))
				print()
				
				answer = asin(arcsine_value)
				print(f"Your arc sine result is {answer}")
				status = True
				print("_ "*27)
				
				
				
			elif trigonometry == 5:
				
				#calculating  arc cos
				trig5 = True
				arc_cos_value = float(input("Enter a value: "))
				print()
				answer = acos(arc_cos_value)
				print(f"Your arc cos result is {answer}")
				status = True
				print("_ "*27)
				
				
			elif trigonometry == 6:
				
				#calculation of arc tan
				trig6 = True
				arc_tan_value = float(input("Enter a value: "))
				print()
				answer = atan(arc_tan_value)
				print(f"Your arc tan result is {answer}")
				status = True
				print("_ "*27)
				
				 
			elif trigonometry == 7:
				
				#calculation of degrees
				trig7 = True
				print()
				print("This convert radians value to degrees")
				print()
				
				degrees_value = float(input("Enter a radians value: "))
				print()
				answer = round(degrees(degrees_value))
				print()
				
				
				
				print(f"Your degrees result is {answer}\N{Superscript Zero} ")
				
				status = True
				print("_ "*27)
				
				
			elif trigonometry == 8:
				trig8 = True
				print()
				
				print("This convert value in degrees to radians")
				print()
				radians_value = float(input("Enter a value in degrees: "))
				print()
				answer = radians(radians_value)
				print()
				
			
				print(f"Your radians result is {answer}")
				
				status = True
				print("_ "*27)
				
			elif trigonometry ==9:
				trig9 = True 
				
				print()
				topics()
				status = True
				
				
			elif trigonometry == 10:
				print()
				print("You just exited the program", "Goodbye!", sep = "\n")
				exit()
				print("_ "*27)
				
			else:
				raise ValueError
		except ValueError:
			print()
			print("Invalid input!")
			
#Function call
topics()
