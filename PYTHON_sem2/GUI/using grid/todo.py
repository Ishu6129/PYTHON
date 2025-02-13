from tkinter import *
from tkinter import messagebox
class bmi:
    def __init__(self,main_win):
        
        self.main_win=main_win
        self.main_win.geometry('203x230')
        self.main_win.title("Todo List")
        self.entry=Entry(main_win)
        self.entry.grid(row=0,column=0,padx=7,pady=5)
        self.addbt=Button(main_win,text="Add",command=self.additm)
        self.addbt.grid(row=0,column=1,ipadx=13)
        self.lbox=Listbox(self.main_win,width=20)
        self.lbox.grid(row=1,column=0,columnspan=2,ipadx=39)
        self.dltbt=Button(main_win,text="Delete",command=self.delitm)
        self.dltbt.grid(row=3,column=0,ipadx=13,pady=7)
        self.dltall=Button(main_win,text="Delete All",command=self.delallitm)
        self.dltall.grid(row=3,column=1,pady=7)
        

    def additm(self):
        data=self.entry.get()
        self.lbox.insert(END,data)
        self.entry.delete(0,END)
    def delitm(self):
        ind=self.lbox.curselection()
        self.lbox.delete(ind)
    def delallitm(self):
        sunot=messagebox.askquestion("Warnning","Want to empty Your to do list")
        if sunot=="yes":
            self.lbox.delete(0,END)
root=Tk()
exe=bmi(root)
root.mainloop()
