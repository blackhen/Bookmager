''' Bookmager V1 '''
from Tkinter import *
import webbrowser
import sqlite3

class Open_web(object):
    """ """
    def __init__(self, url):
        self.u = url
    def open_web(self):
        web = self.u
        if 'www.' in web:
            webbrowser.open(web)
        else:
            web = 'https://www.google.co.th/?gws_rd=ssl#q='
        webbrowser.open(web)
        
                            #Top Level
def toplv():
    top = Toplevel().title("Toplevel")

                            #New Bookmark
def new_bookmark():
    con = sqlite3.connect("'%s'.db" % raw_input())    

                            #Open Web
def open_web():
    web = seach_entry.get()
    if 'www.' in web:
        webbrowser.open(web)
    else:
        web = 'https://www.google.co.th/?gws_rd=ssl#q=' + web
        webbrowser.open(web)

                            #Add Book
def add_book():
    """ Push URL to database file """
    web = seach_entry.get()
    if 'www.' in web:
        cur.execute("insert into bookmark values ('%s')" % web)
    else:
        web = 'https://www.google.co.th/?gws_rd=ssl#q=' + web
        cur.execute("insert into bookmark values ('%s')" % web)
    con.commit()
    
                            #Read Data
def OnRigthMouseClick(event):
    """ This event will run if right mouse was clicked """
    items = listbox.curselection()[0] #print index of data in listbox
    x = Open_web(data[items][0])
    x.open_web()
    

                            #HELP PAGE
def help_page():
    """ Help page """
    help_page = Window("Help")
    help_page.make_win()
                            #WINDOW
class Window(Tk):
    """ Programme's window class """
    def __init__(self, title):
        """"""
        self.windows = Tk()
        self.windows.title(title)
        self.windows.config(bg='ORANGE')
        self.windows.wm_iconbitmap('bookmager.ico')

    def make_win(self):
        """ Create programme windows """
        #MENUBAR
        menubar = Menu(self.windows)
        home_mn = Menu(menubar, tearoff=0)
        help_mn = Menu(menubar, tearoff=0)
            #HOME MENU
        home_mn.add_command(label="New File")
        home_mn.add_command(label="Open Bookmark", command=self.read_data)
        home_mn.add_command(label="Export")
        home_mn.add_separator()
        home_mn.add_command(label="Exit", command=self.windows.destroy)
        menubar.add_cascade(label="Home", menu=home_mn)
        self.windows.config(menu=menubar)
            #HELP MENU
        help_mn.add_command(label="Help", command=help_page)
        menubar.add_cascade(label="Help", menu=help_mn)
        mainloop()

    def read_data(self):
        """ Get data from database file to listbox """
        read_page = Window("Bookmark List")
        i = 0
        global data
        data = {}
        for row in cur.execute('SELECT * FROM bookmark'):
            data[i] = row
            i += 1
            print data

        scrollbar = Scrollbar(read_page.windows)
        global listbox
        listbox = Listbox(read_page.windows,\
                          yscrollcommand=scrollbar.set,\
                          width=50, selectmode=EXTENDED)
        listbox.config(selectbackground='orange')
        for i in data:
            listbox.insert(END, data[i])
        listbox.pack(side=LEFT, fill=BOTH)
        scrollbar.pack(sid=LEFT, fill=Y)
        scrollbar.config(command=listbox.yview)
        listbox.bind("<Double-Button-1>", OnRigthMouseClick)

class Main_window(Window):
    """ Main programme window """
    def __init__(self, title):
        """ Main window's structure """
        self.w = Window("Bookmager")
        #SEACH FRAME
        self.seach_frame = LabelFrame(self.w.windows, bg='White', text="Seach", padx=5, pady=5)
        self.seach_frame.pack(padx=10, pady=10)
        #SEACH ENTRY
        self.seach_entry = Entry(self.seach_frame)
        self.seach_entry.pack()
        #SEACH BUTTON
        self.seach_but = Button(self.seach_frame, text = "Seach",\
                                command=self.op_web,\
                                  fg = "black", bg='#FFBF00')
        self.seach_but.pack(fill = "both", expand=1)
        #Add Bookmark Button
        self.seach_book = Button(self.seach_frame,\
                                 text = "Add Bookmark", command=self.add_book,\
                                 fg = "black", bg='#FFBF00')
        self.seach_book.pack(fill = "both", expand=1)
        #Read Bookmark Button
        self.read_book = Button(self.seach_frame,\
                                text = "Read Bookmark", command=self.w.read_data,\
                                  fg = "black", bg='#FFBF00')
        self.read_book.pack(fill = "both", expand=1)
        self.w.make_win()
    def op_web(self):
        """ Open website """
        web = self.seach_entry.get()
        if 'www.' in web:
            webbrowser.open(web)
        else:
            web = 'https://www.google.co.th/?gws_rd=ssl#q=' + web
            webbrowser.open(web)
    def add_book(self):
        """ Push URL to database file """
        web = self.seach_entry.get()
        if 'www.' in web:
            cur.execute("insert into bookmark values ('%s')" % web)
        else:
            web = 'https://www.google.co.th/?gws_rd=ssl#q=' + web
            cur.execute("insert into bookmark values ('%s')" % web)
        con.commit()
        
value = 1
class Check_first(Window):
    """ if first open, it will make a database's table """
    def __init__(self):
        """ Check First's structure """
        self.check = Window("Make Database Table")
        self.label1 = Label(text="First Run?", bg='Orange')
        self.label1.pack(fill=X)
        self.yes = Button(self.check.windows, text="Yes",\
                          command=self.choose_yes, bg='#FFBF00')
        self.yes.pack(fill=X)
        self.no = Button(self.check.windows, text="No",\
                         command=self.choose_no, bg='#FFBF00')
        self.no.pack(fill=X)
        mainloop()
    def choose_yes(self):
        """ Create database table before open the main window """
        cur.execute('create table bookmark (url text)')
        self.check.windows.destroy()

    def choose_no(self):
        """ open the main window """
        self.check.windows.destroy()
        
con = sqlite3.connect("bookmark.db")
cur = con.cursor()

run = Check_first()
root = Main_window('Bookmager')
