#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 6.0
#  in conjunction with Tcl versioin 8.6
#    Nov 29, 2020 07:01:59 PM +0200  platform: Windows NT
"""
---------------------!!!RUN THIS PAGE FOR DB CREATION AND TO START UP THE PROGRAM!!!---------------------
"""
import sys
import pymongo

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk

    py3 = False
except ImportError:
    import tkinter.ttk as ttk

    py3 = True
sys.path.append('..')
from tkinter import messagebox
import Login_Page_support
import Secretarymainmenu
import Studentmainmenu
import Teachermainmenu
from data import user_db_init, inventory_db_init,game_links_db_init,Schedule_db_init,ScheduleTeacher_db_init

user_db_init()
inventory_db_init()
game_links_db_init()
Schedule_db_init()
ScheduleTeacher_db_init()
client = pymongo.MongoClient()
mydb = client['EZSchooldb']

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Login_Page(root)
    Login_Page_support.init(root, top)
    root.mainloop()


w = None


def create_Login_Page(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Login_Page(root, *args, **kwargs)' .'''
    global w, w_win, root
    # rt = root
    root = rt
    w = tk.Toplevel(root)
    top = Login_Page(w)
    Login_Page_support.init(w, top, *args, **kwargs)
    return (w, top)


def destroy_Login_Page():
    global w
    w.destroy()
    w = None


class Login_Page:
    def login(self):
        f = open("Current_user.txt", "w")
        f.seek(0)
        f.truncate()
        user = self.ID__Entry.get()
        pws = self.Password_Entry.get()
        global mydb
        userobj = mydb['Users'].find_one({'id': user})
        if userobj == None:
            tk.messagebox.showwarning('Login Page', 'The Id or Password is incorrect')

        elif pws == userobj['password']:
            tk.messagebox.showinfo('Login Page', f'''Welcome {userobj['name']}''')

            f.write(userobj['id']+"\n"+userobj['name'])
            f.close()
            if userobj['Usertype'] == 1:
                root.destroy()
                Secretarymainmenu.vp_start_gui()
            elif userobj['Usertype'] == 2:
                root.destroy()
                Teachermainmenu.vp_start_gui()
            elif userobj['Usertype'] == 3:
                root.destroy()
                Studentmainmenu.vp_start_gui()
        else:
            tk.messagebox.showwarning('Login Page', 'The Id or Password is incorrect')

    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'

        top.geometry("600x525+660+210")
        top.minsize(148, 1)
        top.maxsize(1924, 1055)
        top.resizable(1, 1)
        top.title("Login_Page")
        top.configure(background="#ccfdd5")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Login_Button = tk.Button(top)
        self.Login_Button.place(relx=0.283, rely=0.577, height=93, width=256)
        self.Login_Button.configure(activebackground="#ececec")
        self.Login_Button.configure(activeforeground="#000000")
        self.Login_Button.configure(background="#93ff93")
        self.Login_Button.configure(cursor="hand2")
        self.Login_Button.configure(disabledforeground="#a3a3a3")
        self.Login_Button.configure(foreground="#000000")
        self.Login_Button.configure(highlightbackground="#d9d9d9")
        self.Login_Button.configure(highlightcolor="black")
        self.Login_Button.configure(pady="0")
        self.Login_Button.configure(text='''Login''')
        self.Login_Button.configure(command=self.login)
        root.bind('<Return>', lambda x: self.login())
        
        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.217, rely=0.267, height=30, width=82)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#ccfdd5")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''ID''')

        self.ID__Entry = tk.Entry(top)
        self.ID__Entry.place(relx=0.383, rely=0.267, height=34, relwidth=0.273)
        self.ID__Entry.configure(background="white")
        self.ID__Entry.configure(disabledforeground="#a3a3a3")
        self.ID__Entry.configure(font="TkFixedFont")
        self.ID__Entry.configure(foreground="#000000")
        self.ID__Entry.configure(highlightbackground="#d9d9d9")
        self.ID__Entry.configure(highlightcolor="black")
        self.ID__Entry.configure(insertbackground="black")
        self.ID__Entry.configure(selectbackground="blue")
        self.ID__Entry.configure(selectforeground="white")

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.2, rely=0.423, height=42, width=102)
        self.Label2.configure(activebackground="#ccfdd5")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#ccfdd5")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Password''')

        self.Password_Entry = tk.Entry(top)
        self.Password_Entry.place(relx=0.383, rely=0.423, height=34, relwidth=0.273)
        self.Password_Entry.configure(background="white")
        self.Password_Entry.configure(disabledforeground="#a3a3a3")
        self.Password_Entry.configure(font="TkFixedFont")
        self.Password_Entry.configure(foreground="#000000")
        self.Password_Entry.configure(highlightbackground="#d9d9d9")
        self.Password_Entry.configure(highlightcolor="black")
        self.Password_Entry.configure(insertbackground="black")
        self.Password_Entry.configure(selectbackground="blue")
        self.Password_Entry.configure(selectforeground="white")
        self.Password_Entry.configure(show="*")

        self.Message1 = tk.Message(top)
        self.Message1.place(relx=0.5, rely=0.114, relheight=0.057
                            , relwidth=0.677)
        self.Message1.configure(background="#ccfdd5")
        self.Message1.configure(foreground="#000000")
        self.Message1.configure(highlightbackground="#d9d9d9")
        self.Message1.configure(highlightcolor="black")
        self.Message1.configure(text=''':נא להכניס פרטי משתמש''')
        self.Message1.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.Message1.configure(width=406)


if __name__ == '__main__':
    vp_start_gui()
