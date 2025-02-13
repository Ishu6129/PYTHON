from tkinter import *
from tkinter import messagebox
class greet:
    def __init__(self,main_win):
        
        self.main_win=main_win
        self.main_win.geometry('400x200')
        self.main_win.title("Sum of two")
        self.main_win.minsize(400,169)
        self.main_win.maxsize(400,169)
        # we can use justify(left/right/center) in label
        Label(self.main_win,text="Enter first number : ",font=29).grid(row=0,column=0,sticky=W,padx=20,pady=15)
        self.entry1=Entry(self.main_win)
        self.entry1.grid(row=0,column=1)
        Label(self.main_win,text="Enter second number : ",font=29).grid(row=1,column=0,sticky=W,padx=20,pady=15)
        self.entry2=Entry(self.main_win)
        self.entry2.grid(row=1,column=1,padx=20,pady=15)
        bt1=Button(self.main_win,text="Find",command=self.fnd,font=27)
        bt1.grid(row=2,column=0,columnspan=2,padx=20,pady=15)

    def fnd(self):
        try:
            d1=int(self.entry1.get())
            d2=int(self.entry2.get())
            messagebox.showinfo('Sum',f'Sum of {d1} and {d2} is : '+str(d1+d2))
        except ValueError:
            messagebox.showerror('Erro','Please enter number only')
        
root=Tk()
exe=greet(root)
root.mainloop()
