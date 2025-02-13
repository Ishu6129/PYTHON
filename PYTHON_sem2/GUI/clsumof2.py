from tkinter import *
from tkinter import messagebox
class greet:
    def __init__(self,main_win):
        
        self.main_win=main_win
        self.main_win.geometry('200x150')
        self.main_win.title("Sum of two")
        self.main_win.minsize(200,150)
        self.main_win.maxsize(200,150)
        Label(self.main_win,text="Enter first number : ",font=29).pack()
        self.entry1=Entry(self.main_win)
        self.entry1.pack()
        Label(self.main_win,text="Enter second number : ",font=29).pack()
        self.entry2=Entry(self.main_win)
        self.entry2.pack()
        bt1=Button(self.main_win,text="Find",command=self.fnd,font=27)
        bt1.pack()
        self.disp=Label(self.main_win,text='')
        self.disp.pack()

    def fnd(self):
        try:
            d1=int(self.entry1.get())
            d2=int(self.entry2.get())
            messagebox.showinfo('Sum',f'Sum of {d1} and {d2} is  '+str(d1+d2))
        except ValueError:
            messagebox.showerror('Erro','Please enter number only')
        
root=Tk()
exe=greet(root)
root.mainloop()
