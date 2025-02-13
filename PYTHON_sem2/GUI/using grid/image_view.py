from tkinter import *
from PIL import ImageTk, Image
import os
class img:
    def __init__(self, main_win):
        self.main_win = main_win
        self.l = []
        for file_name in os.listdir(r'D:\group7'):
            file_path=os.path.join(r'D:\group7',file_name)
            if os.path.isfile(file_path) and (file_path.lower()[-4:] in ['.jpg','.png','gif']):
                try:
                    print(file_path)
                    image=Image.open(file_path).resize((1369,469))
                    self.l.append(image)
                except:
                    pass
        self.image_index = 0
        im = ImageTk.PhotoImage(self.l[self.image_index])
        self.lb = Label(self.main_win, image=im)
        self.lb.image = im
        self.lb.grid(row=0, column=0, columnspan=2)

        b2 = Button(self.main_win, text="आगे", command=self.nex)
        b2.grid(row=1, column=1,ipadx=47)
        b1 = Button(self.main_win, text="पीछे", command=self.previous)
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
