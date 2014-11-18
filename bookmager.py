''' Bookmager '''
from Tkinter import *
from webbrowser import *
from sqlite3 import *

root = Tk()

#Toplevel1
def toplv():
    top = Toplevel().title("Toplevel")

def open_web():
    web = seach_entry.get()
    open(web)

#creat menubar
menubar = Menu(root)

# Home menu
homemenu = Menu(menubar, tearoff=0)
homemenu.add_command(label="New Wondows", command=toplv)
homemenu.add_command(label="Open")
homemenu.add_command(label="Save")
homemenu.add_separator()
homemenu.add_command(label="Exit", command=root.destroy)
menubar.add_cascade(label="Home", menu=homemenu)
root.config(menu=menubar)

#Seach
    #Frame
seach_frame = LabelFrame(root, text="Seach", padx=5, pady=5)
seach_frame.pack(padx=10, pady=10)
    #Entry
seach_entry = Entry(seach_frame)
seach_entry.grid(row=0, column=0)
    #Seach Button
seach_but = Button(seach_frame, text = "Seach", command=open_web, bg="white",\
              fg = "black")
seach_but.grid(row=1, column=0)
    #Add Bookmark Button
add_b_but = Button(seach_frame, text = "Add Bookmark", command=None, bg="white",\
              fg = "black")
add_b_but.grid(row=1, column=1)

root.mainloop()
