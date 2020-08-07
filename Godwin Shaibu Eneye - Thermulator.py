# To begin, we must import tkinter for the GUI


from tkinter import *

root = Tk()
root.title("S+N Calculator Project/Temperature Converter")

e = Entry(root, width=35, borderwidth=10,bg="green")
e.grid(row=0, column=0, columnspan=10, padx=10, pady=10)

#e.insert(0, "")
# This function are set as the working principle of the calculator

def button_click(number):
	#e.delete(0, END)
	current = e.get()
	e.delete(0, END)
	e.insert(0, str(current) + str(number))

def button_clear():
	e.delete(0, END)

def button_add():
	first_number = e.get()
	global f_num
	global math
	math = "addition"
	f_num = int(first_number)
	e.delete(0, END)
#equal button need to be assigned to different operation for it to work
def button_equal():
	second_number = e.get()
	e.delete(0, END)
	
	if math == "addition":
		e.insert(0, f_num + int(second_number))

	if math == "subtraction":
		e.insert(0, f_num - int(second_number))

	if math == "multiplication":
		e.insert(0, f_num * int(second_number))

	if math == "division":
		e.insert(0, f_num / int(second_number))

	if math == "square":
		e.insert(0, f_num **2)

	if math == "square root":
		e.insert(0, f_num **0.5)
		
	if math == "cube":
		e.insert(0, f_num **3)
		
	if math == "cube root":
		e.insert(0, f_num **(1/3))	
		
	if math == "°C_to_°F":
		e.insert(0, f_num*9/5+32)
		
	if math == "°C_to_°K":
		e.insert(0, f_num +273)
		
	if math == "°F_to_°K":
		e.insert(0,((f_num-32)*5/9)+273.15)
		
def button_subtract():
	first_number = e.get()
	global f_num
	global math
	math = "subtraction"
	f_num = int(first_number)
	e.delete(0, END)

def button_multiply():
	first_number = e.get()
	global f_num
	global math
	math = "multiplication"
	f_num = int(first_number)
	e.delete(0, END)

def button_divide():
	first_number = e.get()
	global f_num
	global math
	math = "division"
	f_num = int(first_number)
	e.delete(0, END)

def square():
	first_number = e.get()
	global f_num
	global math
	math = "square"
	f_num = int(first_number)
	e.delete(0, END)
	
def square_root():
	first_number = e.get()
	global f_num
	global math
	math = "square root"
	f_num = int(first_number)
	e.delete(0, END)

def cube():
	first_number = e.get()
	global f_num
	global math
	math = "cube"
	f_num = int(first_number)
	e.delete(0, END)

def cube_root():
	first_number = e.get()
	global f_num
	global math
	math = "cube root"
	f_num = int(first_number)
	e.delete(0, END)
	# Temperature converter section
def C_to_F():
	first_number = e.get()
	global f_num
	global math
	math = "°C_to_°F"
	f_num = int(first_number)
	e.delete(0, END)
	
def C_to_K():
	first_number = e.get()
	global f_num
	global math
	math = "°C_to_°K"
	f_num = int(first_number)
	e.delete(0, END)	
	
def F_to_K():
	first_number = e.get()
	global f_num
	global math
	math = "°F_to_°K"
	f_num = int(first_number)
	e.delete(0, END)
		
# Creation of buttons for input action fictional for both calculator and converter.

button_1 = Button(root, text="1", padx=40, pady=20,bg='sky blue', command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20,bg='sky blue', command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20,bg='sky blue', command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20,bg='sky blue', command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20,bg='sky blue', command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20,bg='sky blue', command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20,bg='sky blue', command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20,bg='sky blue', command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20,bg='sky blue', command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20,bg='sky blue', command=lambda: button_click(0))
button_add = Button(root, text="+", padx=39, pady=20,bg='royal blue',fg='white',command=button_add)
button_equal = Button(root, text="=", padx=100, pady=20,bg='red', command=button_equal)
button_clear = Button(root, text="Clear", padx=80, pady=20,bg='gold', command=button_clear)

button_subtract = Button(root, text="-", padx=41, pady=20,bg='royal blue',fg='white', command=button_subtract)
button_multiply = Button(root, text="*", padx=40, pady=20,bg='royal blue',fg='white', command=button_multiply)
button_divide= Button(root, text="/", padx=41, pady=20,bg='royal blue',fg='white', command=button_divide)
square = Button(root, text="x²", padx=41, pady=20,bg='royal blue',fg='white', command=square)
cube = Button(root, text="x³", padx=41, pady=20,bg='royal blue',fg='white', command=cube)
square_root = Button(root, text="√x", padx=41, pady=20,bg='royal blue',fg='white', command=square_root)
cube_root = Button(root, text="³√x", padx=41, pady=20,bg='royal blue',fg='white', command=cube_root)
C_to_F= Button(root, text="°C - °F", padx=20, pady=20,bg='maroon',fg='white', command=C_to_F)
C_to_K= Button(root, text="°C - °K", padx=20, pady=20,bg='maroon',fg='white', command=C_to_K)
F_to_K= Button(root, text="°F - °K", padx=20, pady=20,bg='maroon',fg='white', command=F_to_K)

# Put the buttons on the screen using the grid system for better arrangements.

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
square.grid(row=1, column=3)
cube.grid(row=2, column=3)
square_root.grid(row=3, column=3)
cube_root.grid(row=4, column=3)


button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)

button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

C_to_F.grid(row=8, column=0)
C_to_K.grid(row=8, column=1)
F_to_K.grid(row=8, column=2)








root.mainloop()
#closing the window with a loop statement.