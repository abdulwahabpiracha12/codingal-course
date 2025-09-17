# Import necessary libararies
from tkinter import *
from PIL import Image, ImageTk

# Setting up Main Window
root = Tk()
root.title('image')
root.geometry('500x500')

# setting up Main Window
upload = Image.open("img.jpg")


image = ImageTk.PhotoImage(upload)


label = Label(root, image=image, height=450, width=400)
label.place(x=50, y=0)
label12 = Label(root, text="This is how you add an image in Tkinter Window")
label12.place(x=50, y=420)


root.mainloop()
