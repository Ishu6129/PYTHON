
from tkinter import *
from tkinter import messagebox
class Calculator:
    def __init__(self,main_win):
        self.main_win=main_win
        self.main_win.title("........")
        self.l1=Label(self.main_win,text="")
        self.l1.grid(row=0,column=0)
        Button(self.main_win,text="1",command=lambda:self.ad("1"),height=2,width=5,font=13,activebackground="#f00000").grid(row=1,column=0,padx=3,pady=4)
        Button(self.main_win,text="0",command=lambda:self.ad("0"),height=2,width=5,font=13,activebackground="#f00000").grid(row=1,column=1,padx=3,pady=4)
        Button(self.main_win,text="exit",command=self.ex,height=2,width=5,font=13,activebackground="#f00000").grid(row=1,column=2,padx=3,pady=4)
    def ex(self):
        ques=messagebox.askquestion("Exit","Do you want to exit")
        if ques=="no":
            pass
        else:
            self.main_win.destroy()
    def ad(self,dig):
        self.l1.config(text=(self.l1.cget("text")+dig))
ex=""
root=Tk()
exe=Calculator(root)
root.mainloop()
