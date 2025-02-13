from tkinter import *
from tkinter import messagebox
import mymod
class greet:
    def __init__(self,main_win):
        
        self.main_win=main_win
        self.main_win.geometry('200x150')
        self.main_win.title("Greeting")
        self.main_win.minsize(200,150)
        self.main_win.maxsize(200,150)
        Label(self.main_win,text="Enter Number to check : ",font=29).pack()
        self.entry1=Entry(self.main_win)
        self.entry1.pack()
        bt1=Button(self.main_win,text="Check",command=self.chk,font=27)
        bt1.pack()

        self.disp=Label(self.main_win,text='')
        self.disp.pack()

    def chk(self):
        try:
            d=int(self.entry1.get())
            self.disp.config(text=f'\n{d} is '+mymod.prime(d))
            messagebox.showinfo('Prime/Not Prime',f'{d} is '+mymod.prime(d))
        except ValueError:
            messagebox.showerror('Erro','Please enter number only')
        
root=Tk()
exe=greet(root)
root.mainloop()
