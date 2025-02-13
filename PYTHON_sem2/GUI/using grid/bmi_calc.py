from tkinter import *
from tkinter import messagebox
class bmi:
    def __init__(self,main_win):
        self.main_win=main_win
        self.main_win.geometry('400x200')
        self.main_win.title("BMI Calculator")
        self.main_win.minsize(400,200)
        self.main_win.maxsize(400,200)
        # we can use justify(left/right/center) in label
        Label(self.main_win,text="Enter weight in kg : ",font=29).grid(row=0,column=0,sticky=W,padx=20,pady=15)
        self.entry1=Entry(self.main_win)
        self.entry1.grid(row=0,column=1)
        Label(self.main_win,text="Enter height in meter : ",font=29).grid(row=1,column=0,sticky=W,padx=20,pady=15)
        self.entry2=Entry(self.main_win)
        self.entry2.grid(row=1,column=1,padx=20,pady=15)
        bt1=Button(self.main_win,text="Find",command=self.fnd,font=27)
        bt1.grid(row=2,column=0,columnspan=2,padx=20,pady=15)
        self.lbout=Label(self.main_win,text="",justify='center')
        self.lbout.grid(row=3,column=0,columnspan=2)


    def fnd(self):
        try:
            d1=float(self.entry1.get())
            d2=float(self.entry2.get())
            self.lbout.config(text=str(d1/(d2**2)))
            messagebox.showinfo('BMI',"Your BMI is "+str(d1/(d2**2)))
        except ValueError:
            messagebox.showerror('Erro','Please enter number only')  
root=Tk()
exe=bmi(root)
root.mainloop()
