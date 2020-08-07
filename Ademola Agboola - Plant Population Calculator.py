'''A program that calculates plant population giving spaces between and within the plant with the landarea'''
'''The print function print the welcome message'''
print("I am here to tell you your plant population")
'''this function calculate the hectare, it accepts 3 arguments; space1, space2 and landarea and the result is put into inbuilt integer function to return the value in integer'''
def hectare(space1, space2, landarea):
	value = int((landarea*10000)/(space1/100*space2/100))
	'''The return keyword terminates the function after execution, it returns the plant population and the formatted method is used to show the land size in ha and the corresponding plant population'''
	return (f"The plant population in {landarea}ha is {value}") 
	'''this function calculate the acre, it accepts 3 arguments; space1, space2 and landarea and the result is put into inbuilt integer function to return the value in integer'''
def acre(space1,space2,landarea):
    value = int((landarea*4000)/(space1/100*space2/100))
    '''The return keyword terminates the function after execution, it returns the plant population and the formatted method is used to show the land size in acre and the corresponding plant population'''
    return (f"The plant population in {landarea}acr is {value}")
    '''this function calculate the plot, it accepts 3 arguments; space1, space2 and landarea and the result is put into inbuilt integer function to return the value in integer'''   
def plot(space1,space2,landarea):
    value = int((landarea*666)/(space1/100*space2/100))
    return (f"The plant population in {landarea}plt is {value}")
    '''The function below is to check if the user is done with his/her operation or not'''
def check_if_user_is_done():
	
	'''this hold the result of the function ,it is given a default value of True to know wether the user is done or not it prevent the program from looping forever'''
	ok_to_finish = True
	
	'''this variable is used to indicate wether the user made a valid entry i.e "y" or "n"/'''
	user_input_accepted = False
	while not user_input_accepted:
		'''this obtain input from the user either of the 2 options must be provide'''
		user_input=input("Are you done(y/n): ") 		#this set the user_input accepted variable to True otherwise the code will print out measgae that the only acceptable message is a "y" or "n"
		if user_input =="y":
			user_input_accepted = True
		elif user_input == "n":
			ok_to_finish = False
			user_input_accepted = True
		else:
			print("Response must be (y/n),please try again")
	return ok_to_finish


'''The function below determine the operation to perform, it allows you to select operation needed to be done'''
def get_operation_choice():
	'''This will return True if and only if user_selection contains one of the strings '1','2','3' '''
	input_ok = False
	while not input_ok:
		print("Menu Options are:")
		print("\t1.Hectare")
		print("\t2.Acre")
		print("\t3.Plot")
		print("---------------")
		user_selection=input("please make a selection: ")
		if user_selection in("1","2","3"):
			input_ok = True
		else:
			print("invalid input (must be 1-3)")
	print("---------------")
	return user_selection
#the functions below obtain inputs
def get_integer_input(message):
#this will return True if and only ifuser_selection contains one of the strings '1','2','3' 
	value_as_string = input(message) 
  #the while statement ensures that the user input must be an integer , the isnumeric method is invoked on the uers input to know if the user's input is an integer if it returns false then the print function below will invoke else it moves to the next line and convert the string integers from the input function to an integer.  
	while not value_as_string.isnumeric():
		print("the input must be in figure")
		value_as_string =input(message)
	return int(value_as_string)
'''the function below is used to reference the get_integer_input above,it inherits the attributes of the get_integer function'''
def get_inputs_from_user():
 #this represent the spacing within the column which is equivalent to the space1 parametre in the hectare,acre and plot function defined earlier.	
    num1 = get_integer_input("input the spacing within the column in cm: ")
 #this represent the spacing within the row which is equivalent to the space2 parametre in the hectare,acre and plot function defined earlier. 
    num2 = get_integer_input("input the spacing within the row in cm: ")
 #this represent the landarea  parametre in the hectare,acre and plot function defined earlier.
    num3 = get_integer_input("input the land size: ")
    return  num1, num2, num3
done = False
while not done:
    result = 0
    menu_choice = get_operation_choice() 
 
    '''Determine the operation to perform'''
 
 #this unpack the variable num1,num2 and num3 from the get_integer_input function
    num1, num2,num3 = get_inputs_from_user()
 
 #the if statement is s conditional on the operation selected from 1-3 and will approriate function such as hectare, acre and plot  as shown below  
    if menu_choice == "1":
        result = hectare(num1,num2,num3)
    elif menu_choice == "2":
        result = acre(num1,num2,num3)
    elif menu_choice == "3":
        result = plot(num1,num2,num3)
    print("Result:", result)
    print("===============")
    done = check_if_user_is_done()
    
print("Thank you")
