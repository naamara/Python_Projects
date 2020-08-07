"""This program will allow you to collect data of all the guests in the hotel. It is called HOTEL MANAGEMENT SYSTEM"""
#importing all the necessary python library to help the program work effectively.
from tkinter import *
from tkinter import ttk
import random
import tkinter.messagebox
from datetime import datetime
#Declaring a class called Hotel with __init__ defined within the class.
class Hotel():
    def __init__(self, root):
        self.root = root 
        self.root.title("Hotel Management System")
        self.root.geometry("1350x75+0+0")
        self.root.config(background = "Powder blue")
        """Frame creation for the program. the program have 4 frame, the topframe, the bottomframe, leftframe and the rightframe. 
        The  topframe is in the mainframe, the leftframe is in the topframe, the rightframe is in the topframe while the bottomframe is in the mainframe"""
        MainFrame = Frame(self.root)
        MainFrame.grid()
        TopFrame = Frame(MainFrame, bd = 14, width = 1350, height = 550, padx = 20, relief = RIDGE, bg = "cadet blue")
        TopFrame.pack(side = TOP)

        LeftFrame = Frame(TopFrame, bd = 10, width = 450, height = 550, padx = 2, relief = RIDGE, bg = "powder blue")
        LeftFrame.pack(side = LEFT)

        RightFrame = Frame(TopFrame, bd = 10, width = 820, height = 550, padx = 2, relief = RIDGE, bg = "cadet blue")
        RightFrame.pack(side = RIGHT)

        BottomFrame = Frame(MainFrame, bd = 10, width = 1350, height = 150, padx = 20, relief = RIDGE, bg = "powder blue")
        BottomFrame.pack(side = BOTTOM)
    #================================
#definition of commands that will help the buttons
        def iExit():
            iExit = tkinter.messagebox.askyesno("Hotel Management Systems", "Confirm you want to exit")
            if iExit > 0:
                root.destroy()
            return

        def Receipt():
            self.txtReceipt.insert(END, CustomerRef.get() + "\t" + Firstname.get() +  "\t" + Surname.get() + "\t" + Address.get() + "\t" + PhoneNo.get() + "\t" + Email.get() + "\t" + Nationality.get() + "\t" + Gender.get() + "\t" + CInDate.get() + "\t" + COutDate.get() + "\t" + TotalDays.get() + "\t" + SubTotal.get() + "\t" + TotalCost.get() + "\n")

        def Reset():
            CustomerRef.set("")
            Firstname.set("")
            Surname.set("")
            Address.set("")
            PhoneNo.set("")
            Email.set("")	
            Nationality.set("")
            DOB.set("")
            IDType.set("")
            Gender.set("")
            CInDate.set("")	
            COutDate.set("")
            Meal.set("")
            RoomType.set("")
            RoomNo.set("")
            RoomExtNo.set("")
            TotalDays.set("")
            SubTotal.set("")
            TotalCost.set("")
            self.txtReceipt.delete("1.0", END)

        def TotalCostandDate():
            if self.txtEmail.get().endswith('@gmail.com') and self.txtPhoneNo.get().isnumeric() and len(self.txtPhoneNo.get())==11 and datetime.strptime(self.txtDOB.get(),'%d/%m/%Y'):
                #calculaton of total number of days stayed in the hotel
                InDate = CInDate.get()
                OutDate = COutDate.get()
                InDate = datetime.strptime(InDate, "%d/%m/%Y")
                OutDate = datetime.strptime(OutDate, "%d/%m/%Y")
                TotalDays.set(abs((OutDate - InDate).days))
                #calculation of the meal prices (sub-total and total)
                if (Meal.get() == "Breakfast" and RoomType.get() == "Single"):
                    q1 = float(17)
                    q2 = float(34)
                    q3 = float(TotalDays.get())
                    q4 = float(q1 + q2)
                    q5 = float(q3 * q4)
                    ST = "$" + str("%.2f"%(q5))
                    TT = "$" + str("%.2f"%(q5 + ((q5)*0.09)))
                    SubTotal.set(ST)
                    TotalCost.set(TT)
                elif (Meal.get() == "Breakfast" and RoomType.get() == "Double"):
                    q1 = float(35)
                    q2 = float(43)
                    q3 = float(TotalDays.get())
                    q4 = float(q1 + q2)
                    q5 = float(q3 * q4)
                    ST = "$" + str("%.2f"%(q5))
                    TT = "$" + str("%.2f"%(q5 + ((q5)*0.09)))
                    SubTotal.set(ST)
                    TotalCost.set(TT)
                elif (Meal.get() == "Breakfast" and RoomType.get() == "Family"):
                    q1 = float(45)
                    q2 = float(63)
                    q3 = float(TotalDays.get())
                    q4 = float(q1 + q2)
                    q5 = float(q3 * q4)
                    ST = "$" + str("%.2f"%(q5))
                    TT = "$" + str("%.2f"%(q5 + ((q5)*0.09)))
                    SubTotal.set(ST)
                    TotalCost.set(TT)

                if (Meal.get() == "Lunch" and RoomType.get() == "Single"):
                    q1 = float(29)
                    q2 = float(37)
                    q3 = float(TotalDays.get())
                    q4 = float(q1 + q2)
                    q5 = float(q3 * q4)
                    ST = "$" + str("%.2f"%(q5))
                    TT = "$" + str("%.2f"%(q5 + ((q5)*0.09)))
                    SubTotal.set(ST)
                    TotalCost.set(TT)
                elif (Meal.get() == "Lunch" and RoomType.get() == "Double"):
                    q1 = float(37)
                    q2 = float(43)
                    q3 = float(TotalDays.get())
                    q4 = float(q1 + q2)
                    q5 = float(q3 * q4)
                    ST = "$" + str("%.2f"%(q5))
                    TT = "$" + str("%.2f"%(q5 + ((q5)*0.09)))
                    SubTotal.set(ST)
                    TotalCost.set(TT)
                elif (Meal.get() == "Lunch" and RoomType.get() == "Family"):
                    q1 = float(46)
                    q2 = float(63)
                    q3 = float(TotalDays.get())
                    q4 = float(q1 + q2)
                    q5 = float(q3 * q4)
                    ST = "$" + str("%.2f"%(q5))
                    TT = "$" + str("%.2f"%(q5 + ((q5)*0.09)))
                    SubTotal.set(ST)
                    TotalCost.set(TT)

                if (Meal.get() == "Dinner" and RoomType.get() == "Single"):
                    q1 = float(28)
                    q2 = float(37)
                    q3 = float(TotalDays.get())
                    q4 = float(q1 + q2)
                    q5 = float(q3 * q4)
                    ST = "$" + str("%.2f"%(q5))
                    TT = "$" + str("%.2f"%(q5 + ((q5)*0.09)))
                    SubTotal.set(ST)
                    TotalCost.set(TT)
                elif (Meal.get() == "Dinner" and RoomType.get() == "Double"):
                    q1 = float(30)
                    q2 = float(43)
                    q3 = float(TotalDays.get())
                    q4 = float(q1 + q2)
                    q5 = float(q3 * q4)
                    ST = "$" + str("%.2f"%(q5))
                    TT = "$" + str("%.2f"%(q5 + ((q5)*0.09)))
                    SubTotal.set(ST)
                    TotalCost.set(TT)
                elif (Meal.get() == "Dinner" and RoomType.get() == "Family"):
                    q1 = float(43)
                    q2 = float(63)
                    q3 = float(TotalDays.get())
                    q4 = float(q1 + q2)
                    q5 = float(q3 * q4)
                    ST = "$" + str("%.2f"%(q5))
                    TT = "$" + str("%.2f"%(q5 + ((q5)*0.09)))
                    SubTotal.set(ST)
                    TotalCost.set(TT)
            else:
                tkinter.messagebox.showwarning('','incorrect detils')

        def booking():
            if Firstname.get() == 'Firstname' or Surname.get() == 'Surname' or PhoneNo.get() == 'Phone No *' or Email.get() == 'Email' or Address.get() == "Address" or CInDate.get() == 'Check In Date' or COutDate.get() == 'Check Out Date' or CustomerRef.get() == 'Customer Ref' or RoomNo.get() == 'Room No' or DOB.get() == "Date of Birth" or RoomType.get() == "Room Type":
                messagebox.showinfo('Incomplete','Fill All the Fields marked by *')
            elif Firstname.get() == '' or Surname.get() == '' or PhoneNo.get() == '' or Email.get() == '' or Address.get() == "" or CInDate.get() == '' or COutDate.get() == '' or CustomerRef.get() == '' or RoomNo.get() == '' or DOB.get() == "" or RoomType.get() == "":
                messagebox.showinfo('Incomplete','Fill All the Fields marked by *')

                #calling of the functions variables.
        CustomerRef = StringVar()
        Firstname = StringVar()
        Surname = StringVar()
        Address = StringVar()
        PhoneNo = StringVar()
        Email = StringVar()	
        Nationality = StringVar()
        DOB = StringVar()
        IDType = StringVar()
        Gender = StringVar()
        CInDate= StringVar()	
        COutDate = StringVar()
        Meal = StringVar()
        RoomType = StringVar()
        RoomNo = StringVar()
        RoomExtNo = StringVar()
        TotalDays = StringVar()
        SubTotal = StringVar()
        TotalCost = StringVar()

#================================

        def uniqueid():
        	rand_var = random.randint(100000, 999999)
        	return "Ref: " + str(rand_var)
        
        self.lblCustomer_Ref = Label(LeftFrame, font = ("Time New Roman", 12, "bold"), text = "Customer Ref: ", padx = 2, bg = "powder blue")
        self.lblCustomer_Ref.grid(row = 0, column = 0, sticky = W)
        self.txtCustomer_Ref = Entry(LeftFrame, font = ("Time New Roman", 12, "bold"), textvariable = CustomerRef, width = 20)
        self.txtCustomer_Ref.grid(row = 0, column = 1, pady = 3, padx = 20), self.txtCustomer_Ref.insert(END, uniqueid())


        self.lblFirstname = Label(LeftFrame, font = ("Time New Roman", 12, "bold"), text = "Firstname", padx = 2, bg = "powder blue")
        self.lblFirstname.grid(row = 1, column = 0, sticky = W)
        self.txtFirstname = Entry(LeftFrame, font = ("Time New Roman", 12, "bold"), textvariable = Firstname, width = 20)
        self.txtFirstname.grid(row = 1, column = 1, pady = 3, padx = 20)

        self.lblSurname = Label(LeftFrame, font = ("Time New Roman", 12, "bold"), text = "Surname", padx = 2, bg = "powder blue")
        self.lblSurname.grid(row = 2, column = 0, sticky = W)
        self.txtSurname = Entry(LeftFrame, font = ("Time New Roman", 12, "bold"), textvariable = Surname, width = 20)
        self.txtSurname.grid(row = 2, column = 1, pady = 3, padx = 20)

        self.lblAddress = Label(LeftFrame, font = ("Time New Roman", 12, "bold"), text = "Address", padx = 2, bg = "powder blue")
        self.lblAddress.grid(row = 3, column = 0, sticky = W)
        self.txtAddress = Entry(LeftFrame, font = ("Time New Roman", 12, "bold"), textvariable = Address, width = 20)
        self.txtAddress.grid(row = 3, column = 1, pady = 3, padx = 20)

        self.lblPhoneNo = Label(LeftFrame, font = ("Time New Roman", 12, "bold"), text = "Phone No: ", padx = 2, bg = "powder blue")
        self.lblPhoneNo.grid(row = 4, column = 0, sticky = W)
        self.txtPhoneNo = Entry(LeftFrame, font = ("Time New Roman", 12, "bold"), textvariable = PhoneNo, width = 20)
        self.txtPhoneNo.grid(row = 4, column = 1, pady = 3, padx = 20)

        self.lblEmail = Label(LeftFrame, font = ("Time New Roman", 12, "bold"), text = "Email", padx = 2, bg = "powder blue")
        self.lblEmail.grid(row = 5, column = 0, sticky = W)
        self.txtEmail = Entry(LeftFrame, font = ("Time New Roman", 12, "bold"), textvariable = Email, width = 20)
        self.txtEmail.grid(row = 5, column = 1, pady = 3, padx = 20)

        self.lblNationality = Label(LeftFrame, font = ("Time New Roman", 12, "bold"), text = "Nationality", padx = 2, bg = "powder blue")
        self.lblNationality.grid(row = 6, column = 0, sticky = W)	
        self.cboNationality = ttk.Combobox(LeftFrame, textvariable = Nationality, state = "readonly", font = ("Time New Roman", 12, "bold"), width = 18)
        self.cboNationality["value"] = ("", "Nigeria", "Ghana", "Cameroon", "Zambia", "America", "British", "Kenya", "London")
        self.cboNationality.current(0)
        self.cboNationality.grid(row = 6, column = 1, pady = 3, padx = 20)

        self.lblDOB = Label(LeftFrame, font = ("Time New Roman", 12, "bold"), text = "Date of Birth", padx = 2, bg = "powder blue")
        self.lblDOB.grid(row = 7, column = 0, sticky = W)
        self.txtDOB = Entry(LeftFrame, font = ("Time New Roman", 12, "bold"), textvariable = DOB, width = 20)
        self.txtDOB.grid(row = 7, column = 1, pady = 3, padx = 20)

        self.lblIDType = Label(LeftFrame, font = ("Time New Roman", 12, "bold"), text = "Type of ID", padx = 2, bg = "powder blue")
        self.lblIDType.grid(row = 8, column = 0, sticky = W)	
        self.cboIDType = ttk.Combobox(LeftFrame, textvariable = IDType, state = "readonly", font = ("Time New Roman", 12, "bold"), width = 18)
        self.cboIDType["value"] = ("", "Drivers lincense", "National ID", "Int. Passport", "Student ID", "Voters Card")
        self.cboIDType.current(0)
        self.cboIDType.grid(row = 8, column = 1, pady = 3, padx = 20)

        self.lblGender = Label(LeftFrame, font = ("Time New Roman", 12, "bold"), text = "Gender", padx = 2, bg = "powder blue")
        self.lblGender.grid(row = 9, column = 0, sticky = W)	
        self.cboGender = ttk.Combobox(LeftFrame, textvariable = Gender, state = "readonly", font = ("Time New Roman", 12, "bold"), width = 18)
        self.cboGender["value"] = ("", "Male", "Female")
        self.cboGender.current(0)
        self.cboGender.grid(row = 9, column = 1, pady = 3, padx = 20)

        self.lblCInDate= Label(LeftFrame, font = ("Time New Roman", 12, "bold"), text = "Check In Date", padx = 2, bg = "powder blue")
        self.lblCInDate.grid(row = 10, column = 0, sticky = W)
        self.txtCInDate = Entry(LeftFrame, font = ("Time New Roman", 12, "bold"), textvariable = CInDate, width = 20)
        self.txtCInDate.grid(row = 10, column = 1, pady = 3, padx = 20)

        self.lblCOutDate = Label(LeftFrame, font = ("Time New Roman", 12, "bold"), text = "Check Out Date", padx = 2, bg = "powder blue")
        self.lblCOutDate.grid(row = 13, column = 0, sticky = W)
        self.txtCOutDate = Entry(LeftFrame, font = ("Time New Roman", 12, "bold"), textvariable = COutDate, width = 20)
        self.txtCOutDate.grid(row = 13, column = 1, pady = 3, padx = 20)

        self.lblMeal = Label(LeftFrame, font = ("Time New Roman", 12, "bold"), text = "Meal", padx = 2, bg = "powder blue")
        self.lblMeal.grid(row = 14, column = 0, sticky = W)	
        self.cboMeal = ttk.Combobox(LeftFrame, textvariable = Meal, state = "readonly", font = ("Time New Roman", 12, "bold"), width = 18)
        self.cboMeal["value"] = ("", "Breakfast", "Lunch", "Dinner")
        self.cboMeal.current(0)
        self.cboMeal.grid(row = 14, column = 1, pady = 3, padx = 20)

        self.lblRoomType = Label(LeftFrame, font = ("Time New Roman", 12, "bold"), text = "Room Type", padx = 2, bg = "powder blue")
        self.lblRoomType.grid(row = 15, column = 0, sticky = W)	
        self.cboRoomType = ttk.Combobox(LeftFrame, textvariable = RoomType, state = "readonly", font = ("Time New Roman", 12, "bold"), width = 18)
        self.cboRoomType["value"] = ("", "Single", "Double", "Family")
        self.cboRoomType.current(0)
        self.cboRoomType.grid(row = 15, column = 1, pady = 3, padx = 20)


        self.lblRoomNo = Label(LeftFrame, font = ("Time New Roman", 12, "bold"), text = "Room No", padx = 2, bg = "powder blue")
        self.lblRoomNo.grid(row = 16, column = 0, sticky = W)	
        self.cboRoomNo = ttk.Combobox(LeftFrame, textvariable = RoomNo, state = "readonly", font = ("Time New Roman", 12, "bold"), width = 18)
        self.cboRoomNo["value"] = ("", "001", "002", "003", "004", "005", "006")
        self.cboRoomNo.current(0)
        self.cboRoomNo.grid(row = 16, column = 1, pady = 3, padx = 20)

#=============Receipt=============
#declaration of the printable details.
        self.lblLabel = Label(RightFrame, font = ("Time New Roman", 10, "bold"), text = "Customer Ref \tFirstname \tSurname \tAddress \tPhone No \tNationality \tCheck In Date \tCheck Out Date", pady = 10, bg = "cadet blue")
        self.lblLabel.grid(row = 0, column = 0, columnspan = 17)

        self.txtReceipt = Text(RightFrame, font = ("Time New Roman", 11, "bold"), height = 15, width = 108)
        self.txtReceipt.grid(row = 1, column = 0, columnspan = 2, pady = 5, padx = 2)		#==========Receipt================
        #declaration of receipt details
        self.lblDays = Label(RightFrame, font = ("Time New Roman", 14, "bold"), text = "No. of Days", bd = 7, bg = "cadet blue", fg = "black",)
        self.lblDays.grid(row = 2, column = 0, sticky = W)
        self.txtDays = Entry(RightFrame, font = ("Time New Roman", 14, "bold"), textvariable = TotalDays, bd = 7, bg = "white", width = 67, justify = LEFT)
        self.txtDays.grid(row =2, column = 1)


        self.lblSubTotal = Label(RightFrame, font = ("Time New Roman", 14, "bold"), text = "Sub. Total Cost", bd = 7, bg = "cadet blue", fg = "black",)
        self.lblSubTotal.grid(row = 3, column = 0, sticky = W)
        self.txtSubTotal = Entry(RightFrame, font = ("Time New Roman", 14, "bold"), textvariable = SubTotal, bd = 7, bg = "white", width = 67, justify = LEFT)
        self.txtSubTotal.grid(row =3, column = 1)

        self.lblTotalCost = Label(RightFrame, font = ("Time New Roman", 14, "bold"), text = "Total Cost", bd = 7, bg = "cadet blue", fg = "black",)
        self.lblTotalCost.grid(row = 4, column = 0, sticky = W)
        self.txtTotalCost = Entry(RightFrame, font = ("Time New Roman", 14, "bold"), textvariable = TotalCost, bd = 7, bg = "white", width = 67, justify = LEFT)
        self.txtTotalCost.grid(row =4, column = 1)


#================================	#declaration of the button programs	
        self.btnTotal = Button(BottomFrame, padx = 16, pady = 1, bd = 4, fg = "black", font = ("Time New Roman", 16, "bold"), width = 21, height = 2, bg = "powder blue", text = "Total", command = TotalCostandDate).grid(row = 0, column = 4, padx = 4)

        self.btnReceipt = Button(BottomFrame, padx = 16, pady = 1, bd = 4, fg = "black", font = ("Time New Roman", 16, "bold"), width = 21, height = 2, bg = "powder blue", text = "Receipt", command = Receipt).grid(row = 0, column = 5, padx = 4)

        self.btnReset = Button(BottomFrame, padx = 16, pady = 1, bd = 4, fg = "black", font = ("Time New Roman", 16, "bold"), width = 21, height = 2, bg = "powder blue", text = "Reset", command = Reset).grid(row = 0, column = 6, padx = 4)

        self.btnExit = Button(BottomFrame, padx = 16, pady = 1, bd = 4, fg = "black", font = ("Time New Roman", 16, "bold"), width = 21, height = 2, bg = "powder blue", text = "Exit", command = iExit).grid(row = 0, column = 7, padx = 4)


if __name__ == "__main__":
    root = Tk()
    application = Hotel(root)
    root.mainloop()
