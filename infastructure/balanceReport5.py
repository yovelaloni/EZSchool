#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 6.0
#  in conjunction with Tcl version 8.6
#    Jan 02, 2021 03:25:46 PM +0200  platform: Windows NT

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

import balanceReport5_support
sys.path.append('..')
from data import user_db_init
user_db_init()
client = pymongo.MongoClient()
mydb = client['EZSchooldb']
Users=mydb['Users']

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    balanceReport5_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    balanceReport5_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def txtreport(self):
        global mydb
        txt =""
        balance="Tuition"
        for i in range (2,62):
            balance = "Tuition"
            userobj = mydb['Users'].find_one({'stuNum': i})
            if userobj['class']==5:
                balance+=userobj['id']
                txt+=userobj['id']+"            "+userobj['name']+"               "+str(userobj[balance])+"\n"
        return txt
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("1536x801")
        top.minsize(120, 1)
        top.maxsize(1540, 845)
        top.resizable(1,  1)
        top.title("דוח יתרות כיתה ה")
        top.configure(background="#d9d9d9")

        self.printreport = tk.Message(top)
        self.printreport.place(relx=0.104, rely=0.05, relheight=0.85
                , relwidth=0.783)
        self.printreport.configure(anchor='ne')
        self.printreport.configure(background="#d9d9d9")
        self.printreport.configure(font="-family {Segoe UI} -size 14")
        self.printreport.configure(foreground="#000000")
        self.printreport.configure(highlightbackground="#d9d9d9")
        self.printreport.configure(highlightcolor="black")
        self.printreport.configure(text=self.txtreport())
        self.printreport.configure(width=470)

if __name__ == '__main__':
    vp_start_gui()




