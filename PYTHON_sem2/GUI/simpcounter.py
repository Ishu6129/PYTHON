from tkinter import *
root=Tk()
root.geometry('200x150')
root.title("Counter")
root.minsize(100,50)

def inc():
    data=lb1.cget("text")+1
    lb1.config(text=data)
    if lb1.cget("text")%2==0:
        lb1.config(fg="red")
    else:
        lb1.config(fg="green")
def dec():
    c=lb1.cget("text")
    if c!=0:
        lb1.config(text=c-1)
    if lb1.cget("text")%2==0:
        lb1.config(fg="red")
    else:
        lb1.config(fg="green")
        

Label(root,text="Counter Application\n",font=29).pack()

lb1=Label(root,text=0,font=33)

lb1.pack()         #necessary for displaying content

bt1=Button(root,text="👆",command=inc,font=27)
bt1.pack(side=LEFT,padx=6,pady=6,ipadx=30)

bt2=Button(root,text="👇",command=dec,font=27)
bt2.pack(side=RIGHT,pady=6,ipadx=30)

root.mainloop()
