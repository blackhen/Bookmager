''' Bookmager V1 '''
from Tkinter import *
import webbrowser
import sqlite3
import os

                            #New Bookmark
def new_bookmark():
    """ Create New Bookmark """
    new_bk = New_bookmark_page()
#------------------------------------------------------------------------------------------------
                            #Choose Bookmark
def choose_bm():
    """ link bookmark to save bookmark in that file """
    choose_book = Choose_bookmark()
#------------------------------------------------------------------------------------------------
                            #Open Web
def open_web():
    web = seach_entry.get()
    if 'www.' in web:
        webbrowser.open(web)
    else:
        web = 'https://www.google.co.th/?gws_rd=ssl#q=' + web
        webbrowser.open(web)
#------------------------------------------------------------------------------------------------
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
#------------------------------------------------------------------------------------------------    
                            #Read Data
def OnRigthMouseClick(event):
    """ This event will run if right mouse was clicked """
    items = listbox.curselection()[0] #print index of data in listbox
    x = Open_web(data[items][0])
    x.open_web()
#------------------------------------------------------------------------------------------------
                            #HELP PAGE
def help_page():
    """ Help page """
    help_page = Window("Help")
    help_frame = Frame(help_page.windows, text="Help User")
    help_frame.pack()
    help_label = Label(help_page.windows, text='%s' % open('developer.txt', 'r'))
    help_page.make_win()
#------------------------------------------------------------------------------------------------
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
#------------------------------------------------------------------------------------------------
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
        home_mn.add_command(label="New File", command=new_bookmark)
        home_mn.add_command(label="Choose your bookmark", command=choose_bm)
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
#------------------------------------------------------------------------------------------------
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
#------------------------------------------------------------------------------------------------        
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
        self.check.windows.destroy()
        self.fisrt_creat =  New_bookmark_page()
        
    def choose_no(self):
        """ open the main window """
        self.check.windows.destroy()
#------------------------------------------------------------------------------------------------
class New_bookmark_page(Window):
        def __init__(self):
            self.first_bk = Window("Create Your Bookmark file")
            self.name_label = Label(self.first_bk.windows, text='please Insert your bookmark name')
            self.name_label.pack()
            self.name_entry = Entry(self.first_bk.windows)
            self.name_entry.pack()
            self.creat_but = Button(self.first_bk.windows, text="Create File", command=self.new_bookmark)
            self.creat_but.pack(fill=X)
            self.cancel_but = Button(self.first_bk.windows, text="Cancel", command=self.choose_cancel)
            self.cancel_but.pack(fill=X)
            self.first_bk.make_win()
        def new_bookmark(self):
            """ """
            self.bookmark_name = self.name_entry.get()
            global con
            global cur
            con = sqlite3.connect("%s.db" % self.bookmark_name)
            cur = con.cursor()
            cur.execute('create table bookmark (url text)')
            self.first_bk.windows.destroy()
        def choose_cancel(self):
            self.first_bk.windows.destroy()
#------------------------------------------------------------------------------------------------
class Choose_bookmark(Window):
    """ """
    def __init__(self):
        """ """
        self.cb = Window("Choose your bookmark")
        self.name_label = Label(self.cb.windows, text='please Insert your bookmark name')
        self.name_label.pack()

        #listbox
        i = 0
        self.data = {}
        for file_n in os.listdir(cwd):
            self.data[i] = file_n
            i += 1
            print self.data
        self.scrollbar = Scrollbar(self.cb.windows)
        self.listbox = Listbox(self.cb.windows,\
                          yscrollcommand=self.scrollbar.set,\
                          width=50, selectmode=EXTENDED)
        self.listbox.config(selectbackground='orange')
        for i in self.data:
            self.listbox.insert(END, self.data[i])
        self.listbox.pack(side=LEFT, fill=BOTH)
        self.scrollbar.pack(sid=LEFT, fill=Y)
        self.scrollbar.config(command=self.listbox.yview)
        self.listbox.bind("<Double-Button-1>", self.double_click)
        '''
        self.name_entry = Entry(self.cb.windows)
        self.name_entry.pack()
        self.choose_but = Button(self.cb.windows, text="Choose File", command=self.choose_bookmark)
        self.choose_but.pack(fill=X)
        self.cancel_but = Button(self.cb.windows, text="Cancel", command=self.choose_cancel)
        self.cancel_but.pack(fill=X)'''
        self.cb.make_win()
    def choose_bookmark(self):
        """ open wanted bookmark """
        self.book_name = self.name_entry.get()
        global con, cur
        con = sqlite3.connect("%s.db" % self.book_name)
        cur = con.cursor()
    def double_click(self, event):
        """ """
        self.items = self.listbox.curselection()[0] #print index of data in listbox
        print self.data[self.items]
        global con, cur
        con = sqlite3.connect("%s" % self.data[self.items])
        cur = con.cursor()
#------------------------------------------------------------------------------------------------
cwd = os.getcwd()
con = sqlite3.connect("bookmark.db")
cur = con.cursor()

run = Check_first()
root = Main_window('Bookmager')
