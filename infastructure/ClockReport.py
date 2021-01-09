#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 6.0
#  in conjunction with Tcl version 8.6
#    Jan 03, 2021 05:01:41 PM +0200  platform: Windows NT

import sys

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

import ClockReport_support
import WorkClock
import ClockReport
import TransWorkClock

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    ClockReport_support.init(root, top)
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
    ClockReport_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def txt(self):
        f = open("Current_user.txt")
        id=f.readline()
        id=id[:9]
        f.close()
        name = "work"+" "+id+".txt"
        f = open(name)
        message=f.read()
        f.close()
        return (message)
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("994x696+152+0")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(1,  1)
        top.title("דוח שעות")
        top.configure(background="#ffff80")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.392, rely=0.043, height=48, width=189)
        self.Label1.configure(background="#ffff80")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Segoe UI} -size 12 -weight bold")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''דו"ח שעות''')

        self.Message1 = tk.Message(top)
        self.Message1.place(relx=0.091, rely=0.144, relheight=0.823
                , relwidth=0.818)
        self.Message1.configure(anchor='nw')
        self.Message1.configure(background="#ffffff")
        self.Message1.configure(foreground="#000000")
        self.Message1.configure(highlightbackground="#d9d9d9")
        self.Message1.configure(highlightcolor="black")
        self.Message1.configure(text=self.txt())
        self.Message1.configure(width=810)

if __name__ == '__main__':
    vp_start_gui()





