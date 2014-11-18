''' Bookmager '''
from Tkinter import *
from webbrowser import *
from sqlite3 import *

root = Tk()
menubar = Menu(root)

#Toplevel1
def toplv():
    top = Toplevel().title("Toplevel")

#OpenWEB
def open_web():
    web = 'https://www.google.co.th/?gws_rd=ssl#q=' + seach_entry.get()
    open(web)

class Make_menu(Menu):
    def __init__(self):
        self.menu = Menu(menubar, tearoff=0)
    def make_menu(self):
        self.menu.add_command(label="New Wondows", command=toplv)
        self.menu.add_command(label="Open")
        self.menu.add_command(label="Save")
        self.menu.add_separator()
        self.menu.add_command(label="Exit", command=root.destroy)
        menubar.add_cascade(label="Home", menu=self.menu)
        root.config(menu=menubar)


home = Make_menu().make_menu()

#Seach
var = StringVar()
var.set("Please insert your URL")
    #Frame
seach_frame = LabelFrame(root, text="Seach", padx=5, pady=5)
seach_frame.pack(padx=10, pady=10)
    #Entry
seach_entry = Entry(seach_frame, textvariable=var)
seach_entry.pack()
    #Seach Button
seach_but = Button(seach_frame, text = "Seach", command=open_web, bg="white",\
              fg = "black")
seach_but.pack(fill = "both", expand=1)
    #Add Bookmark Button
add_b_but = Button(seach_frame, text = "Add Bookmark", command=None, bg="white",\
              fg = "black")
add_b_but.pack(fill = "both", expand=1)

root.mainloop()
