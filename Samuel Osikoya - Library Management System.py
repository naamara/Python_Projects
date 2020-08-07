import tkinter as tk
from tkinter import ttk
import random
from datetime import datetime 
import tkinter.messagebox

font = {'font': ('Times New Roman',12,'bold')}

class Library:
    def __init__(self, master):
        self.master = master
        self.master.title("Library System")
        self.master.geometry("1350x750+0+0")
        self.master.configure(background='grey')

        MainFrame = tk.Frame(self.master) 
        MainFrame.pack()

        


        self.Title = tk.StringVar()
        self.usertype = tk.StringVar()
        self.Firstname = tk.StringVar()
        self.Lastname = tk.StringVar()
        self.MatricStaffNo = tk.StringVar()
        self.Address = tk.StringVar()
        self.PhoneNumber = tk.StringVar()
        self.Email = tk.StringVar()
        self.Author = tk.StringVar()
        self.BookTitle = tk.StringVar()
        self.DateBorrowed = tk.StringVar() 
        self.DateDue = tk.StringVar()
        self.DaysOnLoan = tk.StringVar()
        self.DaysOnLoan = tk.StringVar()
        self.BookPrice = tk.StringVar()
        self.LateReturnFine = tk.StringVar()
        self.Overdue = tk.StringVar()

        
        def iexit():
            iexit = tk.messagebox.askyesno('Library Management System', 'Want to exit?')
            if iexit>0:
                window.destroy()
                return 
        def iReset():
            self.usertype.set('')
            self.Title.set('') 
            self.Firstname.set('') 
            self.Lastname.set('')  
            self.MatricStaffNo.set('') 
            self.Address.set('') 
            self.PhoneNumber.set('') 
            self.Email.set('') 
            self.Author.set('') 
            self.BookTitle.set('') 
            self.DateBorrowed.set('') 
            self.DateDue.set('')       
            self.DaysOnLoan.set('') 
            self.DaysOnLoan.set('') 
            self.BookPrice.set('') 
            self.LateReturnFine.set('') 
            self.Overdue.set('')
            

           


        def iDel():
            iReset()
            self.info_display.delete('1', tk.END)
            
        def iDisplayInfo():
            self.info_display.insert(tk.END, "\t" + self.MatricStaffNo.get()+ "\t\t" + self.Title.get() + "\t\t" + self.Firstname.get() + "\t\t" + self.Lastname.get() + "\t\t" + self.Address.get() + 
            "\t\t\t" + self.BookTitle.get() + "\t\t" + self.DateBorrowed.get() + "\t\t" + self.DaysOnLoan.get() + "\n")
            


        #Project Name Frame
        top_frame_with_name = tk.Frame(MainFrame, width=1350, bd = 20, padx = 10, relief=tk.GROOVE)
        top_frame_with_name.pack(side=tk.TOP)
        self.libTitle = tk.Label(top_frame_with_name, width=40, **font,text="FUOYE LIBRARY MANAGEMENT SYSTEM")
        self.libTitle.grid()

    
        #Tasks Frame(Exit, Reset etc.) = last frame
        OptionFrame = tk.Frame(MainFrame, width= 1350, height=70, bd = 20, padx = 20, pady=20, relief=tk.GROOVE )
        OptionFrame.pack(side=tk.BOTTOM)

        #Data Frame = user's info at thye Right
        DataFrame = tk.Frame(MainFrame, width= 1350, height=70, bd = 20, padx = 20, pady=20, relief=tk.GROOVE )
        DataFrame.pack(side=tk.BOTTOM)

        #User and Book Details Frame =  Second Major frame
        user_details_frame = tk.Frame(MainFrame, width= 1350, height=400, bd = 20, padx = 20, pady=20, relief=tk.GROOVE )
        user_details_frame.pack(side=tk.BOTTOM)

        #BookList Frame = right frame on second major frame
        Book_info_frame = tk.LabelFrame(user_details_frame, width = 500, height = 400, text='Book Details',**font, relief=tk.GROOVE )
        Book_info_frame.pack(side=tk.RIGHT)

        #For user info = left  frame on the second major frame
        User_info_frame = tk.LabelFrame(user_details_frame, width = 500, height= 400, text = 'User Info', **font, bd = 10, relief= tk.GROOVE)
        User_info_frame.pack(side=tk.LEFT)

    
        #Widgets
        #Title of Library User
        self.user_title = tk.Label(User_info_frame, **font, text="Title:",  )
        self.user_title.grid(row=0,)
        self.user_title_entry =ttk.Combobox(User_info_frame, **font,  textvariable= self.Title, state='readonly')
        self.user_title_entry['value']= ('', 'Mr', 'Mrs', 'Dr', 'Miss', 'Prof.')
        self.user_title_entry.current(0)
        self.user_title_entry.grid(row=0, column=1, sticky='W')

        #Type of User
        self.user_type = tk.Label(User_info_frame, **font, text="User Type:",  )
        self.user_type.grid(row=1,)
        self.user_type_entry =ttk.Combobox(User_info_frame, **font, textvariable=self.usertype )
        self.user_type_entry['value']= ('', 'Student', 'Lecturer', 'Admin Staff', 'Non-academic Staff')
        self.user_type_entry.current(0)
        self.user_type_entry.grid(row=1, column=1, sticky='W')
        

        #firstName of Library User
        self.user_firstName = tk.Label(User_info_frame, **font, text="Firstname:",  )
        self.user_firstName.grid(row=2)
        self.user_firstName_entry =tk.Entry(User_info_frame,textvariable=self.Firstname )
        self.user_firstName_entry.grid(row=2, column=1) 

        #lastName of lib user
         #firstName of Library User
        self.user_lastName = tk.Label(User_info_frame, **font, text="Lastname:",  )
        self.user_lastName.grid(row=3)
        self.user_lastName_entry =tk.Entry(User_info_frame, textvariable=self.Lastname)
        self.user_lastName_entry.grid(row=3, column=1) 


        #Matric/staff no
        self.user_MtrcOrStaNum = tk.Label(User_info_frame, **font, text="Matric/Staff No.:", padx=2, pady=2 )
        self.user_MtrcOrStaNum.grid(row=4)
        self.user_MtrcOrStaNum_entry =tk.Entry(User_info_frame,textvariable=self.MatricStaffNo )
        self.user_MtrcOrStaNum_entry.grid(row=4, column=1) 

        #User_address
        self.user_address = tk.Label(User_info_frame, **font, text="Address:",  padx=2, pady=2 )
        self.user_address.grid(row=5)
        self.user_address_entry =tk.Entry(User_info_frame,textvariable=self.Address )
        self.user_address_entry.grid(row=5, column=1) 

        #User contact number
        self.user_cntNum = tk.Label(User_info_frame, **font, text="Phone Number:",  padx=2, pady=2 )
        self.user_cntNum.grid(row=6)
        self.user_cntNum_entry =tk.Entry(User_info_frame, textvariable=self.PhoneNumber)
        self.user_cntNum_entry.grid(row=6, column=1) 

        #User's email
        self.user_mail = tk.Label(User_info_frame, **font, text="Email:",  padx=2, pady=2 )
        self.user_mail.grid(row=7)
        self.user_mail_entry =tk.Entry(User_info_frame, textvariable=self.Email)
        self.user_mail_entry.grid(row=7, column=1) 

        #Book Title
        self.bk_title = tk.Label(User_info_frame, **font, text="Book Title:",  padx=2, pady=2 )
        self.bk_title.grid(row=0, column=3)
        self.bk_title_entry =tk.Entry(User_info_frame, textvariable=self.BookTitle )
        self.bk_title_entry.grid(row=0, column=4) 

        #Author
        self.bk_author = tk.Label(User_info_frame, **font, text="Author:",  padx=2, pady=2 )
        self.bk_author.grid(row=1, column=3, )
        self.bk_author_entry =tk.Entry(User_info_frame, textvariable=self.Author)
        self.bk_author_entry.grid(row=1, column=4) 


         #Date Borrowed
        self.date_borrowed = tk.Label(User_info_frame, **font, text="Date Borrowed:", padx=2, pady=2,  )
        self.date_borrowed.grid(row=2, column=3, )
        self.date_borrowed_entry =tk.Entry(User_info_frame,textvariable=self.DateBorrowed, state='readonly' )
        self.date_borrowed_entry.grid(row=2, column=4) 

         #Date Due
        self.date_due= tk.Label(User_info_frame, **font, text="Date Due:",  padx=2, pady=2 )
        self.date_due.grid(row=3, column=3, )
        self.date_due_entry =tk.Entry(User_info_frame,textvariable=self.DateDue, state='readonly' )
        self.date_due_entry.grid(row=3, column=4)

        #Days on Loan
        self.days_loan = tk.Label(User_info_frame, **font, text="Days on Loan:",  padx=2, pady=2 )
        self.days_loan.grid(row=4, column=3, )
        self.days_loan_entry =tk.Entry(User_info_frame, textvariable=self.DaysOnLoan, state='readonly' )
        self.days_loan_entry.grid(row=4, column=4)

        #Fine/day
        self.fine = tk.Label(User_info_frame, **font, text="Late Return Fine:",  padx=2, pady=2 )
        self.fine.grid(row=5, column=3, )
        self.fine_entry =tk.Entry(User_info_frame,textvariable=self.LateReturnFine )
        self.fine_entry.grid(row=5, column=4)

        #Date Overdue
        self.overdue = tk.Label(User_info_frame, **font, text="Date Overdue:",  padx=2, pady=2 )
        self.overdue.grid(row=6, column=3, )
        self.overdue_entry =tk.Entry(User_info_frame, textvariable=self.Overdue)
        self.overdue_entry.grid(row=6, column=4)

        #Book Price
        self.fine = tk.Label(User_info_frame, **font, text="Book Price:",  padx=2, pady=2 )
        self.fine.grid(row=7, column=3, )
        self.fine_entry =tk.Entry(User_info_frame, width = 20, textvariable=self.BookPrice)
        self.fine_entry.grid(row=7, column=4) 



#Buttons 
        self.options_btn = tk.Button(OptionFrame, **font, text='Display Entries', width = 20, padx = 2, pady= 2, command=iDisplayInfo)
        self.options_btn.grid(row=0, column=0)

        self.options_btn = tk.Button(OptionFrame, **font, text='Delete', width = 20, padx = 2, pady= 2, command=iDel)
        self.options_btn.grid(row=0, column=1)

        self.options_btn_1 = tk.Button(OptionFrame, **font, text='Reset', width = 20, padx = 2, pady= 2, command=iReset)
        self.options_btn_1.grid(row=0, column=2)

        self.options_btn = tk.Button(OptionFrame, **font, text='Exit', width = 20, padx = 2, pady= 2, command = iexit)
        self.options_btn.grid(row=0, column=3)
        self.display_info= tk.Text(OptionFrame, width = 20, height = 4)
        
        
#Work on DataFrame
        self.DataFrame_label = tk.Label(DataFrame, **font, text='Staff/Matric No\tTitle\tFirstname\tLastname\t Address\t Book Title\t Date Borrowed \t Days on Loan\
            ', padx = 4, pady=4) 
        self.DataFrame_label.grid(row=0, column=0, sticky='w')  

        self.info_display = tk.Text(DataFrame, width = 120, height = 4, padx = 2, pady = 4, )
        self.info_display.grid(row=1, column = 0, sticky='EW', ipadx=3)

        self.receipt = tk.Text(Book_info_frame, width = 20, height = 30, )
        self.receipt.grid(row=0, column = 2)

           


# Booklist
        scrollbar = tk.Scrollbar(Book_info_frame,)
        scrollbar.grid(row=0,column=1, sticky='ns')

        Listofbooks = ['The Crucified Life', 'The Cost of Discipleship', 'The Divine Revelation of Hell','Understanding Divine Direction', 'Following God\'s Plan', 'Sermons Series', 'Believer\'s Authority',
        'The Purpose Drive Life', 'The Kneeling Christian', 'Discovering Your Potention', 'Gifted Hands',
        'Think Big', 'Starting Over', 'The Prison Saying of Samuel Rutherford', 'God\'s Generals: The Missionaries', 
        'Holiness', 'Touching The World Therough Prayer', 'Think Big', 'The Big Picture','The Fundamentals of Python',
        'Introduction to Machine Learning', 'Abiding in Christ', 'The Power of Prayer', 'Silent Labours',
        'The Greatest Mistake']

#To fill in the boxes with info about the book for borrowed books record
        def SelectedBks(bk):
            value = str(booklist.get(booklist.curselection()))
            w = value
            if w == 'The Crucified Life':
                self.BookTitle.set('The Crucified Life')
                self.Author.set('A.W.Tozer')
                import datetime
                d_1 = datetime.date.today()
                d2 = datetime.timedelta(days=14)
                d3 = d_1 + d2
                self.DateBorrowed.set(d_1)
                self.DateDue.set(d3)
                self.Overdue.set('No')
                self.DaysOnLoan.set('7')
                self.BookPrice.set('N900')
                self.LateReturnFine.set('N1000')

            if w == 'The Cost of Discipleship':
                self.BookTitle.set('The Cost of Discipleship')
                self.Author.set('Dietrich Bonhoeffer')
                import datetime
                d_1 = datetime.date.today()
                d2 = datetime.timedelta(days=14)
                d3 = d_1 + d2
                self.DateBorrowed.set(d_1)
                self.DateDue.set(d3)
                self.Overdue.set('No')
                self.DaysOnLoan.set('7')
                self.BookPrice.set('N800')
                self.LateReturnFine.set('N1000')

            if w == 'The Cost of Discipleship':
                self.BookTitle.set('The Cost of Discipleship')
                self.Author.set('Dietrich Bonhoeffer')
                import datetime
                d_1 = datetime.date.today()
                d2 = datetime.timedelta(days=14)
                d3 = d_1 + d2
                self.DateBorrowed.set(d_1)
                self.DateDue.set(d3)
                self.Overdue.set('No')
                self.DaysOnLoan.set('7')
                self.BookPrice.set('N800')
                self.LateReturnFine.set('N1000')

            if w == 'The Divine Revelation of Hell':
                self.BookTitle.set('The Divine Revelation of Hell')
                self.Author.set('Baxter')
                import datetime
                d_1 = datetime.date.today()
                d2 = datetime.timedelta(days=14)
                d3 = d_1 + d2
                self.DateBorrowed.set(d_1)
                self.DateDue.set(d3)
                self.Overdue.set('No')
                self.DaysOnLoan.set('7')
                self.BookPrice.set('N1800')
                self.LateReturnFine.set('N1000')

            if w == 'Understanding Divine Direction':
                self.BookTitle.set('Understanding Divine Direction')
                self.Author.set('Bishop Oyedepo')
                import datetime
                d_1 = datetime.date.today()
                d2 = datetime.timedelta(days=14)
                d3 = d_1 + d2
                self.DateBorrowed.set(d_1)
                self.DateDue.set(d3)
                self.Overdue.set('No')
                self.DaysOnLoan.set('7')
                self.BookPrice.set('N1200')
                self.LateReturnFine.set('N1000')

            if w == 'Following God\'s Plan':
                self.BookTitle.set('Following God\'s Plan')
                self.Author.set('Kenneth Hagin')
                import datetime
                d_1 = datetime.date.today()
                d2 = datetime.timedelta(days=14)
                d3 = d_1 + d2
                self.DateBorrowed.set(d_1)
                self.DateDue.set(d3)
                self.Overdue.set('No')
                self.DaysOnLoan.set('7')
                self.BookPrice.set('N700')
                self.LateReturnFine.set('N1000')

            if w == 'Silent Labours':
                self.BookTitle.set('Silent Labours')
                self.Author.set('Gbile Akanni')
                import datetime
                d_1 = datetime.date.today()
                d2 = datetime.timedelta(days=14)
                d3 = d_1 + d2
                self.DateBorrowed.set(d_1)
                self.DateDue.set(d3)
                self.Overdue.set('No')
                self.DaysOnLoan.set('7')
                self.BookPrice.set('N600')
                self.LateReturnFine.set('N1000')

            
            if w == 'Sermons Series':
                self.BookTitle.set('Sermons Series')
                self.Author.set('Baxter')
                import datetime
                d_1 = datetime.date.today()
                d2 = datetime.timedelta(days=14)
                d3 = d_1 + d2
                self.DateBorrowed.set(d_1)
                self.DateDue.set(d3)
                self.Overdue.set('No')
                self.DaysOnLoan.set('7')
                self.BookPrice.set('N2800')
                self.LateReturnFine.set('N1000')


            if w == 'Believer\'s Authority':
                self.BookTitle.set('Believer\'s Authority')
                self.Author.set('Gbile Akanni')
                import datetime
                d_1 = datetime.date.today()
                d2 = datetime.timedelta(days=14)
                d3 = d_1 + d2
                self.DateBorrowed.set(d_1)
                self.DateDue.set(d3)
                self.Overdue.set('No')
                self.DaysOnLoan.set('7')
                self.BookPrice.set('N1600')
                self.LateReturnFine.set('N1000')


            


   
        booklist = tk.Listbox(Book_info_frame, width = 20, height = 20, **font, )  
        booklist.bind('<<ListboxSelect>>', SelectedBks)    
        booklist.grid(row=0, column=0)
        scrollbar.config(command=booklist.yview)

        

        for items in Listofbooks:
            booklist.insert(tk.END, items)
       
       
    

window = tk.Tk() 
app = Library(window)
window.title(" Library Management System")
window.resizable(False, False)
window.mainloop()
           
        
'''
This project is heavily assisted by the vidoe tutorial of Capt. Oamen
on YouTube (). The project therefore is not my whole idea but I learnt a great deal with this project.

Permit me to appreciate Scholar Network Python Online BootCamp
that have enabled me to have advanced knowledge of python programming.
Special thanks to the whole community of developers.
Sam


'''