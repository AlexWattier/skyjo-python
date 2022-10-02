from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from controller.Controller import Controller

root = Tk()
canvas = Canvas(root, width=100, height=600)
canvas.pack()


def main(event):
    cont: Controller = Controller(1)
    if event.widget.cget('image') == 'pyimage1':
        messagebox.showinfo('First', 'You clicked the first image')
    elif event.widget.cget('image') == 'pyimage2':
        messagebox.showinfo('Second', 'You clicked the second image')
    elif event.widget.cget('image') == 'pyimage3':
        messagebox.showinfo('Third', 'You clicked the third image')

img_file = Image.open("resource/cardb.png")
img_file = img_file.resize((100, 150))
img = ImageTk.PhotoImage(img_file)
b1 = Button(canvas, image=img)
b1.pack()
b1.bind('<Button-1>', )

img_file1 = Image.open("resource/cardr.png")
img_file1 = img_file1.resize((100, 150))
img1 = ImageTk.PhotoImage(img_file1)
b2 = Button(canvas, image=img1)
b2.pack()
b2.bind('<Button-1>', main)

img_file2 = Image.open("resource/cardr.png")
img_file2 = img_file2.resize((100, 150))
img2 = ImageTk.PhotoImage(img_file2)
b3 = Button(canvas, image=img2)
b3.pack()
b3.bind('<Button-1>', main)

root.mainloop()