from tkinter import *
import math
import parser
import tkinter.messagebox

root=tkinter.Tk()
root.tiltle="My Python Calculator"
root.configure(background="white")
root.resizable(width=False,height=False)
root.geometry("480x560+0+0")

calculator=tkinter.Frame(root)
calculator.grid()
#functions of calculator
class Calculator():
    def __init__(self):
        self.total=0
        self.expression=""
        self.input_value=True
        self.check_sum=False
        self.op=""
        self.result=False
        
    def numberEntry(self,num):
        self.result=False
        firstnum=Display.get()
        secondnum=str(num)
        if self.input_value:
            self.current=secondnum
            self.input_value=False
        else:
            if secondnum==".":
               if secondnum in firstnum:
                   return
            self.current=firstnum+secondnum
        self.display(self.current)
    def display(self,value):
        Display.delete(0,tkinter.END)
        Display.insert(0,value)
    def Total(self):
        self.result=True
        self.current=float(self.current)
        if self.check_sum==True:
            self.function()
        else:
              self.total=float(Display.get())    
    def function(self):
        if self.op=="add":
           self.total += self.current
        if self.op=="sub":
           self.total -= self.current
        if self.op=="multi":
           self.total *= self.current
        if self.op=="divide":
           self.total /= self.current 
        self.input_value=True
        self.check_sum=False
        self.display(self.total)
        
    def operation(self,op):
        self.current=float(self.current)
        if self.check_sum:
            self.function()
        elif not self.result:
            self.total=self.current
            self.input_value=True
        self.check_sum=True
        self.op=op
        self.result=False
    def Delete(self):
        self.result=False
        self.current="0"
        self.display(0)
        self.input_value=True
        
    def AllClear(self):
        self.Delete()
        self.total=0
        
    def factorial(self):
        self.result=False
        self.current=math.factorial(float(Display.get()))
        self.display(self.current)
        
    def square(self):
        self.result=False
        self.current=math.sqrt(float(Display.get()))
        self.display(self.current)
  
     
        
    
        
added_value=Calculator()        


#screen widget
Display=tkinter.Entry(calculator,font=("Times Roman",20,"bold"),bg="white",bd=30,
                      width=28,justify=tkinter.RIGHT)
#position of calculator screen
Display.grid(row=0,column=0,columnspan=4,pady=1)
Display.insert(0,"0")

#making number buttons
numbers="123456789"
i=0
btn=[]
for j in range(2,5):
    for k in range(3):
        btn.append(tkinter.Button(calculator,width=6,height=2,font=("Times Roman",20,"bold"),
                                  bg="white",bd=4,text=numbers[i]))
        btn[i].grid(row=j,column=k,pady=1)
        btn[i]["command"]=lambda x=numbers[i]:added_value.numberEntry(x)
        i+=1
#making the function buttons 
btnDelete=tkinter.Button(calculator,text="DEL",width=6,height=2,font=("Times Roman",20,"bold"),
                         bd=4,bg="grey",
                         command=added_value.Delete).grid(row=1,column=0,pady=1)        
btnAllCL=tkinter.Button(calculator,text="AC",width=6,height=2,font=("Times Roman",20,"bold"),
                         bd=4,bg="grey",
                         command=added_value.AllClear).grid(row=1,column=1,pady=1)
btnSqr=tkinter.Button(calculator,text="√",width=6,height=2,font=("Times Roman",20,"bold"),
                         bd=4,bg="grey",
                         command=added_value.square).grid(row=1,column=2,pady=1)   
btnAdd=tkinter.Button(calculator,text="+",width=6,height=2,font=("Times Roman",20,"bold"),
                         bd=4,bg="grey",
                         command=lambda:added_value.operation("add")).grid(row=1,column=3,pady=1)                
btnSub=tkinter.Button(calculator,text="-",width=6,height=2,font=("Times Roman",20,"bold"),
                         bd=4,bg="grey",
                         command=lambda:added_value.operation("sub")).grid(row=2,column=3,pady=1)   
btnMult=tkinter.Button(calculator,text="*",width=6,height=2,font=("Times Roman",20,"bold"),
                         bd=4,bg="grey",
                         command=lambda:added_value.operation("multi")).grid(row=3,column=3,pady=1)   
btnDiv=tkinter.Button(calculator,text=chr(247),width=6,height=2,font=("Times Roman",20,"bold"),
                         bd=4,bg="grey",
                         command=lambda:added_value.operation("divide")).grid(row=4,column=3,pady=3) 
btnZ=tkinter.Button(calculator,text="0",width=6,height=2,font=("Times Roman",20,"bold"),bd=4,bg="white",
                         command=lambda:added_value.numberEntry(0)).grid(row=5,column=0,pady=3) 
btnDot=tkinter.Button(calculator,text=".",width=6,height=2,font=("Times Roman",20,"bold"),
                         bd=4,bg="grey",
                         command=lambda:added_value.numberEntry(".")).grid(row=5,column=1,pady=3) 
btnfactorial=tkinter.Button(calculator,text="!",width=6,height=2,font=("Times Roman",20,"bold"),
                         bd=4,bg="grey",
                         command=added_value.factorial).grid(row=5,column=2,pady=3)
btnEQ=tkinter.Button(calculator,text="=",width=6,height=2,font=("Times Roman",20,"bold"),
                         bd=4,bg="grey",
                         command=added_value.Total).grid(row=5,column=3,pady=3)           
#function of exit
def iexit():
    iexit=tkinter.messagebox.askyesno("My Python Calculator","Do you want to exit calculator?")
    if iexit>0:
        root.destroy()
        return
#size of the calculator    
def standard():
    root.resizable(width=False,height=False)
    root.geometry("480x560+0+0")
menubar=tkinter.Menu(calculator)

filemenu=tkinter.Menu(menubar,tearoff=0)
menubar.add_cascade(label="File",menu=filemenu)
filemenu.add_command(label="Standard")
filemenu.add_separator()
filemenu.add_command(label="Exit",command=iexit)

root.config(menu=menubar)
root.mainloop()
