from tkinter import *
from tkinter import messagebox
class Calculator:
    def __init__(self,main_win):
        self.main_win=main_win
        self.main_win.title("Calculator")
        self.main_win.minsize(245,337)
        self.main_win.maxsize(245,337)

        self.eq=StringVar()

        self.entry=Entry(self.main_win,textvariable=self.eq,state="disabled",font=13,justify="right").grid(row=0,column=0,columnspan=5,ipadx=24,ipady=7,pady=5)

        Button(self.main_win,text="C",command=self.clr,height=2,width=5,font=13,activebackground="#f00000").grid(row=1,column=0,padx=3,pady=4)
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
            res=str(eval(exp))
            self.eq.set(res)
            exp=res
        except ValueError:
            self.eq.set("Exception")
            exp=""
        except SyntaxError:
            self.eq.set("Syntax_Error")
            exp=""
        except ZeroDivisionError:
            self.eq.set("Division_by_zero_error")
            exp=""
    def bck(self):
        global exp
        exp=exp[0:-1]
        self.eq.set(exp.replace("*","x"))
    def clr(self):
        global exp
        exp=""
        self.eq.set("")
exp=""
root=Tk()
exe=Calculator(root)
root.mainloop()
