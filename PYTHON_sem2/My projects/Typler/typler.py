from tkinter import *
from tkinter import messagebox
import pyttsx3

class Play:
    def __init__(self, main):
        self.main_win = main

        self.grt = Label(self.main_win, text="greet", font=("Arial", 13))
        self.grt.grid(row=0, column=2)

        self.lb = Label(self.main_win, text="Display", font=("Arial", 27))
        self.lb.grid(row=1, column=1)

        emoji_image = PhotoImage(file="emoji.png")
        self.main_win.emoji_image = emoji_image
        self.spk = Button(self.main_win, image=emoji_image, borderwidth=0, command=self.speak)
        self.spk.grid(row=1, column=1, sticky='es')

        self.disp = Text(self.main_win, height=1, width=23, font=("Arial", 21), state='disabled', borderwidth=0)
        self.disp.grid(row=2, column=1, pady=13)

        self.ext = Button(self.main_win, text="Exit", command=self.main_win.destroy, borderwidth=3, font=("Arial", 14))
        self.ext.grid(row=3, column=0, ipadx=27, ipady=13)

        self.enty = Entry(self.main_win, font=("Arial", 14))
        self.enty.grid(row=3, column=1)
        self.enty.bind("<KeyRelease>", self.update_display)

        self.ext = Button(self.main_win, text="Reset", command=self.chg, borderwidth=3, font=("Arial", 14))
        self.ext.grid(row=3, column=2, ipadx=27, ipady=13)

        self.disp.tag_configure('center', justify='center')

        # pyttsx3
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 133)
        self.engine.setProperty('volume', 1.0)
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[1].id)
        

    def update_display(self, event):
        text = self.enty.get()
        self.disp.config(state='normal')
        self.disp.delete(1.0, END)
        self.disp.insert(END, text)
        self.disp.tag_add('center', '1.0', 'end')  # Apply center tag to the entire content
        self.disp.config(state='disabled')

    def chg(self):
        self.enty.delete(0, END)
        self.disp.config(state='normal')
        self.disp.delete(1.0, END)
        self.disp.config(state='disabled')

    def speak(self):
        spk = self.lb.cget('text')
        self.engine.say(spk)
        self.engine.setProperty('voice', self.voices[1].id)
        self.engine.runAndWait()

root = Tk()
exe = Play(root)
root.mainloop()



        # self.text_widget = Text(self.main_win)
        # self.text_widget.grid(row=1, column=0)
        # self.text_widget.insert(END, "Wo", "green")
        # self.text_widget.insert(END, "rd", "red")
        
        # # Define tag configurations for colors
        # self.text_widget.tag_configure("green", foreground="green")
        # self.text_widget.tag_configure("red", foreground="red")
'''
engine = pyttsx3.init()
engine.setProperty('rate', 111)   
engine.setProperty('volume', 1.0)  
voices = engine.getProperty('voices')
engine.setProperty('pitch', 69) 

engine.setProperty('voice', voices[1].id)  
user_input = input("Enter text to speak: ")


engine.say(user_input)


engine.runAndWait()
'''