''' Bookmager '''
from Tkinter import *
from webbrowser import *
import sqlite3
root = Tk()
menubar = Menu(root)
var = StringVar()
var.set("Please insert your URL")

#sql
con = sqlite3.connect('bookmark.db')
cur = con.cursor()

#create table (run at first time only but now isn't complete) if have tst.db on Desktop please go nextline to comment
#cur.execute('create table bookmark (url text)')

#Toplevel1
def toplv():
    top = Toplevel().title("Toplevel")

#OpenWEB
def open_web():
    web = seach_entry.get()
    if 'www.' in web:
        open(web)
    else:
        web = 'https://www.google.co.th/?gws_rd=ssl#q=' + web
        open(web)
def add_book():
    web = seach_entry.get()
    if 'www.' in web:
        cur.execute("insert into bookmark values ('%s')" % web)
    else:
        web = 'https://www.google.co.th/?gws_rd=ssl#q=' + web
        cur.execute("insert into bookmark values ('%s')" % web)
    con.commit()
    

def read_data():
    for  row in cur.execute('SELECT * FROM bookmark'):
        print row
    print '=========================='
    
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
seach_book = Button(seach_frame, text = "Add Bookmark", command=add_book, bg="white",\
                      fg = "black")
seach_book.pack(fill = "both", expand=1)

#Read Bookmark Button
read_book = Button(seach_frame, text = "Read Bookmark", command=read_data, bg="white",\
                      fg = "black")
read_book.pack(fill = "both", expand=1)

root.mainloop()
