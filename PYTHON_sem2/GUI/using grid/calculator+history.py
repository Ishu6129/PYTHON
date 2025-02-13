from tkinter import *
from tkinter import messagebox
class Calculator:
    def __init__(self,main_win):
        self.main_win1=main_win
        self.main_win1.title("Calculator")
        self.main_win1.minsize(245,337)
        self.main_win1.maxsize(245,337)
        self.main_win=Frame(self.main_win1)
        self.main_win.grid(row=0,column=0)
        
        self.hmain_win=Frame(self.main_win1)
        self.hmain_win.grid(row=0,column=0)

        self.eq=StringVar()
        self.entry=Entry(self.main_win,textvariable=self.eq,state= "disabled",font=13,justify="right").grid(row=0,column=0,columnspan=5,ipadx=24,ipady=7,pady=5)

        self.b1=Button(self.main_win,text="C / H",height=2,width=5,font=13,activebackground="#f00000")
        self.b1.bind("<Button-1>",lambda event:self.clr(event))
        self.b1.bind("<Button-3>",lambda event:self.hview(event))
        self.b1.grid(row=1,column=0,padx=3,pady=4)
        Button(self.main_win,text="(",command=lambda:self.bpress("("),height=2,width=5,font=13,activebackground="#a9a9a9").grid(row=1,column=1,padx=3,pady=4)
        Button(self.main_win,text=")",command=lambda:self.bpress(")"),height=2,width=5,font=13,activebackground="#a9a9a9").grid(row=1,column=2,padx=3,pady=4)
        Button(self.main_win,text="◀",command=self.bck,height=2,width=5,font=13,activebackground="#a9a9a9").grid(row=1,column=3,padx=3,pady=4)

        Button(self.main_win,text="7",command=lambda:self.bpress("7"),height=2,width=5,font=13,activebackground="#a9a9a9").grid(row=2,column=0,padx=3,pady=4)
        Button(self.main_win,text="8",command=lambda:self.bpress("8"),height=2,width=5,font=13,activebackground="#a9a9a9").grid(row=2,column=1,padx=3,pady=4)
        Button(self.main_win,text="9",command=lambda:self.bpress("9"),height=2,width=5,font=13,activebackground="#a9a9a9").grid(row=2,column=2,padx=3,pady=4)
        Button(self.main_win,text="/",command=lambda:self.bpress("/"),height=2,width=5,font=13,activebackground="#a9a9a9").grid(row=2,column=3,padx=3,pady=4)

        Button(self.main_win,text="4",command=lambda:self.bpress("4"),height=2,width=5,font=13,activebackground="#a9a9a9").grid(row=3,column=0,padx=3,pady=4)
        Button(self.main_win,text="5",command=lambda:self.bpress("5"),height=2,width=5,font=13,activebackground="#a9a9a9").grid(row=3,column=1,padx=3,pady=4)
        Button(self.main_win,text="6",command=lambda:self.bpress("6"),height=2,width=5,font=13,activebackground="#a9a9a9").grid(row=3,column=2,padx=3,pady=4)
        Button(self.main_win,text="x",command=lambda:self.bpress("*"),height=2,width=5,font=13,activebackground="#a9a9a9").grid(row=3,column=3,padx=3,pady=4)

        Button(self.main_win,text="1",command=lambda:self.bpress("1"),height=2,width=5,font=13,activebackground="#a9a9a9").grid(row=4,column=0,padx=3,pady=4)
        Button(self.main_win,text="2",command=lambda:self.bpress("2"),height=2,width=5,font=13,activebackground="#a9a9a9").grid(row=4,column=1,padx=3,pady=4)
        Button(self.main_win,text="3",command=lambda:self.bpress("3"),height=2,width=5,font=13,activebackground="#a9a9a9").grid(row=4,column=2,padx=3,pady=4)
        Button(self.main_win,text="-",command=lambda:self.bpress("-"),height=2,width=5,font=13,activebackground="#a9a9a9").grid(row=4,column=3,padx=3,pady=4)

        Button(self.main_win,text=".",command=lambda:self.bpress("."),height=2,width=5,font=13,activebackground="#a9a9a9").grid(row=5,column=0,padx=3,pady=4)
        Button(self.main_win,text="0",command=lambda:self.bpress("0"),height=2,width=5,font=13,activebackground="#a9a9a9").grid(row=5,column=1,padx=3,pady=4)
        Button(self.main_win,text="=",command=self.eql,height=2,width=5,font=13,activebackground="#a9a9a9").grid(row=5,column=2,padx=3,pady=4)
        Button(self.main_win,text="+",command=lambda:self.bpress("+"),height=2,width=5,font=13,activebackground="#a9a9a9").grid(row=5,column=3,padx=3,pady=4)
        
        # History Part
        self.lb=Listbox(self.hmain_win)
        self.lb.grid(row=0,column=0,columnspan=5,ipady=60,ipadx=40,padx=20)
        Button(self.hmain_win,text="Back",command=self.mnview).grid(row=1,column=1,ipadx=13,pady=10)
        Button(self.hmain_win,text="Delete History",command=self.delt).grid(row=1,column=3)
        self.main_win.tkraise()

    def bpress(self,btn):
        global exp
        if exp=="" and btn not in "/*-+)":
            exp=exp+btn
            self.eq.set(exp.replace("*","x"))
        elif exp!="":
            if btn not in "/*-+()":
                exp=exp+btn
                self.eq.set(exp.replace("*","x"))
            elif btn in "/*-+.()" and exp[-1] not in "/*-+.()":
                exp=exp+btn
                self.eq.set(exp.replace("*","x"))
    def eql(self):
        global exp
        try:
            self.lb.insert(END,exp.replace("*","x")+" = "+str(eval(exp)))
            res=str(eval(exp))
            self.eq.set(res)
            exp=res
        except ValueError:
            self.eq.set("Exception")
            exp=""
        except ZeroDivisionError:
            self.eq.set("Division_by_zero_error")
            exp=""
        except SyntaxError:
            self.eq.set("Syntax_Error")
            exp=""
    def bck(self):
        global exp
        exp=exp[0:-1]
        self.eq.set(exp.replace("*","x"))
    def clr(self,event):
        global exp
        exp=""
        self.eq.set("")
    def delt(self):
        if self.lb.size() != 0:
            desc=messagebox.askquestion("History","Want to delete History")
            if desc=="yes":
                self.lb.delete(0,END)
    def mnview(self):
        self.main_win.tkraise()
    def hview(self,event):
        self.hmain_win.tkraise()
exp=""
root=Tk()
exe=Calculator(root)
root.mainloop()
