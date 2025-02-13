from tkinter import *

class counter:
    def __init__(self,main_win):
        
        self.main_win=main_win
        self.main_win.geometry('200x150')
        self.main_win.title("Counter")
        self.main_win.minsize(200,150)
        self.main_win.maxsize(200,150)
        
        self.var=IntVar(value=0)
        
        Label(root,text="Counter Application\n",font=29).pack()
        self.lb1=Label(self.main_win,textvariable=self.var,font=33)
        self.lb1.pack()
        
        bt1=Button(self.main_win,text="👆",command=self.inc,font=27)
        bt1.pack(side=LEFT,padx=6,pady=6,ipadx=30)
        
        bt2=Button(self.main_win,text="👇",command=self.dec,font=27)
        bt2.pack(side=RIGHT,pady=6,ipadx=30)
    def inc(self):
        self.var.set(self.var.get()+1)
        if self.var.get()%2==0:
            self.lb1.config(fg="red")
        else:
            self.lb1.config(fg="green")

    def dec(self):
        if self.var.get()!=0:
            self.var.set(self.var.get()-1)
        if self.var.get()%2==0:
            self.lb1.config(fg="red")
        else:
            self.lb1.config(fg="green")
root=Tk()
exe=counter(root)
root.mainloop()
