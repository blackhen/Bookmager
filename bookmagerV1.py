''' Bookmager V1 '''
from Tkinter import *
import webbrowser, sqlite3, os
cwd = os.getcwd()
con = sqlite3.connect('default.db')
cur = con.cursor()
##
##                            #New Bookmark
def new_bookmark():
    """ Create New Bookmark """
    new_bk = New_bookmark_page()
##------------------------------------------------------------------------------------------------
                            #Choose Bookmark
def choose_bm():
    """ link bookmark to save bookmark in that file """
    choose_book = Choose_bookmark()

##----------------------------------------------------------------------------------------        
                            #Menubar
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
        home_mn.add_command(label="New", command=new_bookmark)
        home_mn.add_command(label="Open", command=choose_bm)
        home_mn.add_command(label="Exit", command=self.windows.destroy)
        menubar.add_cascade(label="Home", menu=home_mn)
        self.windows.config(menu=menubar)
        mainloop()
##------------------------------------------------------------------------------------------------

#Re Data
def read_data_re():
        '''refresh_data'''
        listbox.delete(0, END)
        i = 0
        global data
        data = {}
        for row in cur.execute('SELECT * FROM bookmark'):
            data[i] = row[1]+' '*(15-len(row[1]))+row[0]
            i += 1
            print data  
        for i in data:
            listbox.insert(END, data[i])
##------------------------------------------------------------------------------------------------

    
##choose
class Choose_bookmark(Window):
    """Open Database"""
    def __init__(self):
        """Main"""
        self.cb = Window("Open")
        #listbox
        num = 0 #key
        self.data = {}
        for file_n in os.listdir(cwd):
            if file_n.endswith('.db'):
                self.data[num] = file_n
                num += 1
        print self.data
        self.scrollbar = Scrollbar(self.cb.windows)
        self.listbox = Listbox(self.cb.windows,\
                          yscrollcommand=self.scrollbar.set,\
                          width=50, selectmode=EXTENDED)
        self.listbox.config(selectbackground='orange')
        for num in self.data:
            self.listbox.insert(END, self.data[num])
        self.listbox.pack(side=LEFT, fill=BOTH)
        self.scrollbar.pack(sid=LEFT, fill=Y)
        self.scrollbar.config(command=self.listbox.yview)
        self.listbox.bind("<Double-Button-1>", self.double_click)
        self.change_but = Button(self.cb.windows, text="Open", command=self.choose_bookmark, bg='#FFBF00')
        self.change_but.pack(fill=X)
        self.cancel_but = Button(self.cb.windows, text="Cancel", command=self.choose_cancel, bg='#FFBF00')
        self.cancel_but.pack(fill=X)
        self.delete_but = Button(self.cb.windows, text="Delete", command=self.choose_delete, bg='#FFBF00')
        self.delete_but.pack(fill=X)
        self.cb.make_win()
        
    def choose_delete(self):
        '''Delete Database'''
        self.items = int(self.listbox.curselection()[0]) #print index of data in listbox
        print self.data[self.items]
        os.remove(self.data[self.items])
        self.choose_re()
    
    def choose_re(self):
        '''Refreash Listbox'''
        self.listbox.delete(0, END)
        i = 0
        num = 0
        self.data = {}
        for file_n in os.listdir(cwd):
            if file_n.endswith('.db'):
                self.data[num] = file_n
                num += 1
        print self.data
        for num in self.data:
            self.listbox.insert(END, self.data[num])
        
    def choose_bookmark(self):
        """ open wanted bookmark """
        self.items = int(self.listbox.curselection()[0]) #print index of data in listbox
        print self.data[self.items]
        global con
        global cur
        con = sqlite3.connect('%s' %self.data[self.items])
        cur = con.cursor()
        read_data_re()
        listbox.delete(0, END)
        i = 0
        global data
        data = {}
        for row in cur.execute('SELECT * FROM bookmark'):
            data[i] = row[1]+' '*(15-len(row[1]))+row[0]
            i += 1
            print data  
        for i in data:
            listbox.insert(END, data[i])
        self.cb.windows.destroy()
        
    def double_click(self, event):
        """DoubleClick to open database"""
        self.items = int(self.listbox.curselection()[0]) #print index of data in listbox
        print self.data[self.items], cwd, "'"+self.data[self.items]+"'"
        global con
        global cur
        con = sqlite3.connect('%s' %self.data[self.items])
        cur = con.cursor()
        print cur.execute('select name from sqlite_master where type="table"').fetchall()
        listbox.delete(0, END)
        i = 0
        global data
        data = {}
        for row in cur.execute('SELECT * FROM bookmark'):
            data[i] = row[1]+' '*(15-len(row[1]))+row[0]
            i += 1
            print data  
        for i in data:
            listbox.insert(END, data[i])
        
        
    def choose_cancel(self):
        '''Exit OPen'''
        self.cb.windows.destroy()
        
##------------------------------------------------------------------------------------------------
##Main
class Main_window(Window):
    """ Main programme window """
    def __init__(self, title):
        """ Main window's structure """
        self.w = Window("Bookmager")
        #SEACH FRAME
        self.seach_frame = LabelFrame(self.w.windows, bg='White', text="Edit", padx=5, pady=5)
        self.seach_frame.pack(side=LEFT, padx=10, pady=10)
        #url ENTRY
        urldefault = StringVar()
        namedefault = StringVar()
        keyworddefault = StringVar()
        self.seach_entry = Entry(self.seach_frame, textvariable=urldefault)
        self.seach_entry.pack()
        urldefault.set("URL")
        #name ENTRY
        self.name_entry = Entry(self.seach_frame, textvariable=namedefault)
        self.name_entry.pack()
        namedefault.set("NAME")

        #Add Bookmark Button
        self.seach_book = Button(self.seach_frame,\
                                 text = "Add Bookmark", command=self.add_book,\
                                 fg = "black", bg='#FFBF00')
        self.seach_book.pack(fill = "both", expand=1)
        #Delete
        self.delete = Button(self.seach_frame,\
                                 text = "Delete", command=self.delete,\
                                 fg = "black", bg='#FFBF00')
        self.delete.pack(fill = "both", expand=1)

        #SEARCH FRAME
        self.search_frame = LabelFrame(self.w.windows, bg='White', text="Search", padx=5, pady=5)
        self.search_frame.pack(side=RIGHT, padx=10, pady=10)
        
        #SEARCH BUTTON
        self.search_entry = Entry(self.search_frame, textvariable=keyworddefault)
        self.search_entry.pack()
        keyworddefault.set("Keyword")        
        self.search_but = Button(self.search_frame, text = "Search Bookmark",\
                                command=self.search_book,\
                                  fg = "black", bg='#FFBF00')
        self.search_but.pack(fill = "both", expand=1)

        #OPEN Button
        self.open_but = Button(self.search_frame, text = "OPEN URL",\
                                command=self.op_web,\
                                  fg = "black", bg='#FFBF00')
        self.open_but.pack(fill=X, expand=1, side='left')
        
        self.read_data()
        self.w.make_win()

    #search bookmark
    def search_book(self):
        '''Search bookmark'''
        keyword = self.search_entry.get()
        print keyword
        listbox.delete(0, END)
        i = 0
        global data
        data = {}
        for row in cur.execute('SELECT * FROM bookmark'):
            print row
            if keyword in (row[0] or row[1]):
                print 'yes'
                data[i] = row[1]+' '*(15-len(row[1]))+row[0]
                i += 1
                print data  
        for i in data:
            listbox.insert(END, data[i])
        
    #list bookmark
    def read_data(self):
        '''ListBox'''
        scrollbar = Scrollbar(self.w.windows)
        global listbox
        listbox = Listbox(self.w.windows,\
                          yscrollcommand=scrollbar.set,\
                          width=60, selectmode=EXTENDED)
        listbox.config(selectbackground='orange')
        
        i = 0
        global data
        data = {}
        for row in cur.execute('SELECT * FROM bookmark'):
            data[i] = row[1]+' '*7+row[0]
            i += 1
            print data
       
        for i in data:
            listbox.insert(END, data[i])
        listbox.pack(side=LEFT)
        scrollbar.pack(sid=RIGHT, fill=Y)
        scrollbar.config(command=listbox.yview)
        listbox.bind("<Double-Button-1>", self.double_open_url)

    #Delete URL
    def delete(self):
        '''Delete bookmark'''
        global cur, con
        items = int(listbox.curselection()[0]) #print index of data in listbox
        name_data = data[items].split()[0]
        url_data = data[items].split()[1]
        cur.execute("DELETE FROM bookmark WHERE name = '%s'" %name_data)
        read_data_re()
        con.commit()

    #Re Data   
    def read_data_re(self):
        '''Refreash Data'''
        listbox.delete(0, END)
        i = 0
        global data
        data = {}
        for row in cur.execute('SELECT * FROM bookmark'):
            data[i] = row[1]+' '*(15-len(row[1]))+row[0]
            i += 1
            print data  
        for i in data:
            listbox.insert(END, data[i])

    #Open URL       
    def op_web(self):
        """ Open website """
        self.items = int(listbox.curselection()[0]) #print index of data in listbox
        print self.items
        print data[self.items].split()[1]
        webbrowser.open(data[self.items].split()[1])

    #Add Bookmark       
    def add_book(self):
        """ Push URL to database file """
        web = self.seach_entry.get()
        name = self.name_entry.get()
        cur.execute("insert into bookmark values ('"+web+"', '"+name+"')")
        read_data_re()
        con.commit()

    #doubleclick to open
    def double_open_url(self, event):
        '''doubleclick to open'''
        self.items = int(listbox.curselection()[0]) #print index of data in listbox
        print data[self.items].split()[1]
        webbrowser.open(data[self.items].split()[1])
        
##------------------------------------------------------------------------------------------------
        
class New_bookmark_page(Window):
        def __init__(self):
            '''main'''
            self.first_bk = Window("Create Your Bookmark file")
            self.name_label = Label(self.first_bk.windows, text='please Insert your bookmark name')
            self.name_label.pack()
            self.name_entry = Entry(self.first_bk.windows)
            self.name_entry.pack()
            self.creat_but = Button(self.first_bk.windows, text="Create File", command=self.new_bookmark, bg='#FFBF00')
            self.creat_but.pack(fill=X)
            self.cancel_but = Button(self.first_bk.windows, text="Cancel", command=self.choose_cancel, bg='#FFBF00')
            self.cancel_but.pack(fill=X)
            self.first_bk.make_win()
            
        def new_bookmark(self):
            """Button Add"""
            self.bookmark_name = self.name_entry.get()
            global con
            global cur
            con = sqlite3.connect("%s.db" % self.bookmark_name)
            con.execute('''CREATE TABLE bookmark (url text, name text)''')
            cur = con.cursor()
            read_data_re()
            self.first_bk.windows.destroy()
            
        def choose_cancel(self):
            '''Button Exit'''
            self.first_bk.windows.destroy()
            

##------------------------------------------------------------------------------------------------

#If You Build First File database
##con.execute('''CREATE TABLE bookmark
##             (url text, name text)''')

root = Main_window('Bookmager')

