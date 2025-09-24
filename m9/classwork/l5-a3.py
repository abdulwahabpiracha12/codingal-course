# Import nessecary libararies
from tkinter import *

# Setting up Main Window
root = Tk()
root.geometry("400x300")
root.title("main")

# Functon to open New (Top Level) Window
def topwin():
    # Setting up Top Window
    top = Toplevel()
    top.geometry("180x100")
    top.title("toplevel")
    # Adding a label widget to Top Window
    l2 = Label(top, text = "This is toplevel window")
    l2.pack()

    top.mainloop()

# Adding a label and button widget to Root (Main) Windw
l = Label(root, text = "This is root window")
btn = Button(root, text = "Click here to open another window", command = topwin)

# Arranging widgets
l.pack()
btn.pack()

root.mainloop()