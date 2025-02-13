from tkinter import *
from tkinter import messagebox
import random
class tictactoe:
    def __init__(self,root): 

        # 1V1 Window
        
        self.in_1_v_1=Frame(root)
        self.in_1_v_1.grid(row=0,column=0,padx=20,ipady=135,pady=40)

        Label(self.in_1_v_1,text="Player 1 : ",font=29).grid(row=0,column=0,padx=20,pady=15)
        self.player_1=Entry(self.in_1_v_1)
        Label(self.in_1_v_1,text="Player 2 : ",font=29).grid(row=1,column=0,padx=20,pady=15)
        self.player_2=Entry(self.in_1_v_1)
        self.ext=Button(self.in_1_v_1,text="Exit",command=root.destroy,font=27)
        self.strt=Button(self.in_1_v_1,text="Start",command=self.start,font=27)

        self.player_1.grid(row=0,column=1)
        self.player_2.grid(row=1,column=1,padx=20,pady=15)
        self.ext.grid(row=2,column=0)
        self.strt.grid(row=2,column=1)

        #Main TicTacToe Window
                
        self.main=Frame(root)
        self.main.grid(row=0,column=0,padx=20)
        self.in_1_v_1.tkraise()
        self.sign=["⭕","❌"]
        self.temp_sign=["⭕","❌"]
        self.s1=self.temp_sign[random.randint(0,1)]
        self.temp_sign.remove(self.s1)
        self.s2=self.temp_sign[0]
        self.l=Label(self.main,text="Tic-Tac-Toe",font=13)
        self.si=self.s1
        self.temp_si=self.si
        self.c=1
        self.b1 = Button(self.main, text="", font=69, bg='white', height=5, width=9,command=lambda:self.btnclk(self.b1,0))
        self.b2 = Button(self.main, text="", font=69, bg='white', height=5, width=9,command=lambda:self.btnclk(self.b2,1))
        self.b3 = Button(self.main, text="", font=69, bg='white', height=5, width=9,command=lambda:self.btnclk(self.b3,2))
        self.b4 = Button(self.main, text="", font=69, bg='white', height=5, width=9,command=lambda:self.btnclk(self.b4,3))
        self.b5 = Button(self.main, text="", font=69, bg='white', height=5, width=9,command=lambda:self.btnclk(self.b5,4))
        self.b6 = Button(self.main, text="", font=69, bg='white', height=5, width=9,command=lambda:self.btnclk(self.b6,5))
        self.b7 = Button(self.main, text="", font=69, bg='white', height=5, width=9,command=lambda:self.btnclk(self.b7,6))
        self.b8 = Button(self.main, text="", font=69, bg='white', height=5, width=9,command=lambda:self.btnclk(self.b8,7))
        self.b9 = Button(self.main, text="", font=69, bg='white', height=5, width=9,command=lambda:self.btnclk(self.b9,8))
        self.chance = Label(self.main, text="",font=13)

        self.l.grid(row=0,column=1,pady=20)
        self.b1.grid(row=1, column=0)
        self.b2.grid(row=1, column=1)
        self.b3.grid(row=1, column=2)
        self.b4.grid(row=2, column=0)
        self.b5.grid(row=2, column=1)
        self.b6.grid(row=2, column=2)
        self.b7.grid(row=3, column=0)
        self.b8.grid(row=3, column=1)
        self.b9.grid(row=3, column=2)
        self.chance.grid(row=4, column=0,columnspan=3,ipadx=60,pady=7)

        self.b_v = [self.b1.cget("text"), self.b2.cget("text"), self.b3.cget("text"), self.b4.cget("text"),\
                     self.b5.cget("text"), self.b6.cget("text"), self.b7.cget("text"), self.b8.cget("text"), self.b9.cget("text")]
        self.b_l=[self.b1,self.b2,self.b3,self.b4,self.b5,self.b6,self.b7,self.b8,self.b9]
        
    def rst(self):
        self.l.config(text="Tic-Tac-Toe",fg="black")
        for i in self.b_l:
            i.config(text="")
        self.b_v = [self.b1.cget("text"), self.b2.cget("text"), self.b3.cget("text"), self.b4.cget("text"),\
                     self.b5.cget("text"), self.b6.cget("text"), self.b7.cget("text"), self.b8.cget("text"), self.b9.cget("text")]
        self.si=self.temp_si
    def btnclk(self,bp,b_index):
        s=bp.cget("text")
        if s=="":
            if self.c==0:
                self.si=self.s2
                self.chance.config(text="Turn : "+self.a)
                self.c=1
                self.p=self.player_2.get()
                if self.p=="":
                    self.p="player 2"

            elif self.c==1:
                self.si=self.s1
                self.chance.config(text="Turn : "+self.b)
                self.c=0
                self.p=self.player_1.get()
                if self.p=="":
                    self.p="player 1"
            bp.config(text=self.si,fg="red")
            self.b_v[b_index]=self.si
            si=self.si
            
            if (self.b_v[0]==self.b_v[1]==self.b_v[2]==si)  or (self.b_v[0]==self.b_v[3]==self.b_v[6]==si) or \
                (self.b_v[2]==self.b_v[5]==self.b_v[8]==si) or (self.b_v[3]==self.b_v[4]==self.b_v[5]==si) or \
                (self.b_v[6]==self.b_v[7]==self.b_v[8]==si) or (self.b_v[0]==self.b_v[4]==self.b_v[8]==si) or \
                (self.b_v[2]==self.b_v[4]==self.b_v[6]==si) or (self.b_v[1]==self.b_v[4]==self.b_v[7]==si) :
                self.chance.config(text="")
                self.l.config(text=self.p+" win",fg="Blue")
                messagebox.showinfo("win",self.p+" win")
                a=messagebox.askquestion("Continue","Want to continue")
                if a=="no":
                    root.destroy()
                self.rst()
                if self.c==1:
                    self.chance.config(text="Turn : "+self.a)
                else:
                    self.chance.config(text="Turn : "+self.b)

            c=0
            for i in self.b_v:
                if i in self.sign:
                    c=c+1
            if c==9:
                self.chance.config(text="")
                self.l.config(text="Try Again",fg="red")
                messagebox.showinfo("Better Luck Next Time","It's a Tie")
                a=messagebox.askquestion("Continue","Want to continue")
                if a=="no":
                    root.destroy()
                self.rst()
                if self.c==1:
                    self.chance.config(text="Turn : "+self.a)
                else:
                    self.chance.config(text="Turn : "+self.b)
            
    def start(self):
        self.main.tkraise()
        self.a=self.player_1.get().strip().title()
        self.b=self.player_2.get().strip().title()
        if self.a=="":
            self.a="Player 1"
        if self.b=="":
            self.b="Player 2"
        messagebox.showinfo("Remember",f'{self.a} {self.s1}\n{self.b} {self.s2}')
        self.y=self.player_1.get().strip().title()
        if self.y=="":
            self.y="player 1"
        self.chance.config(text="Turn : "+self.y)
root = Tk()
exe=tictactoe(root)
root.mainloop()
