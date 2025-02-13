from tkinter import *
class greet:
    def __init__(self,main_win):
        
        self.main_win=main_win
        self.main_win.geometry('200x150')
        self.main_win.title("Greeting")
        self.main_win.minsize(200,150)
        self.main_win.maxsize(200,150)
        
        
        Label(self.main_win,text="Enter your name\n",font=29).pack()


        self.entry=Entry(self.main_win)
        
        self.entry.pack()
        
        bt1=Button(self.main_win,text="Greet",command=self.action,font=27)
        bt1.pack()
        
    
        self.disp=Label(self.main_win,text='')
        self.disp.pack()
        
        bt2=Button(self.main_win,text="exit",command=self.main_win.destroy,font=27)
        bt2.pack()
        
    def action(self):
        data=self.entry.get()
        self.disp.config(text='hello , '+data)
        self.entry.delete(0,END)
        
root=Tk()
exe=greet(root)
root.mainloop()
