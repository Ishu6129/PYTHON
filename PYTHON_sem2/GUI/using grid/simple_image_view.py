from tkinter import *
from PIL import ImageTk, Image

class img:
    def __init__(self, main_win):
        self.main_win = main_win
        self.main_win.maxsize(900,600)
        i1 = Image.open(r'C:\Users\ishua\Pictures\Screenshots\Screenshot 2024-02-05 194020.png').resize((900, 400))
        i2 = Image.open(r'C:\Users\ishua\Pictures\Screenshots\Screenshot 2024-02-05 194036.png').resize((900, 400))
        i3 = Image.open(r'C:\Users\ishua\Pictures\Screenshots\Screenshot 2024-02-05 194048.png').resize((900, 400))
        i4 = Image.open(r'C:\Users\ishua\Pictures\Screenshots\Screenshot 2024-02-05 194109.png').resize((900, 400))
        i5 = Image.open(r'C:\Users\ishua\Pictures\Screenshots\Screenshot 2024-02-05 194128.png').resize((900, 400))
        self.l = [i1, i2, i3, i4, i5]
        self.image_index = 0

        im = ImageTk.PhotoImage(self.l[self.image_index])
        self.lb = Label(self.main_win, image=im)
        self.lb.image = im
        self.lb.grid(row=0, column=0, columnspan=2)

        b2 = Button(self.main_win, text="Next", command=self.nex)
        b2.grid(row=1, column=1,ipadx=47)
        b1 = Button(self.main_win, text="Previous", command=self.previous)
        b1.grid(row=1, column=0,ipadx=47)

    def previous(self):
        if self.image_index > 0:
            self.image_index -= 1
            self.update_image()
        else:
            self.image_index =len(self.l)-1
            self.update_image()

    def nex(self):
        if self.image_index < len(self.l) - 1:
            self.image_index += 1
            self.update_image()
        else:
            self.image_index =0
            self.update_image()


    def update_image(self):
        im = ImageTk.PhotoImage(self.l[self.image_index])
        self.lb.config(image=im)
        self.lb.image = im

root = Tk()
exe = img(root)
root.mainloop()
