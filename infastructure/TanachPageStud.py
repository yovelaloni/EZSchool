#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 6.0
#  in conjunction with Tcl version 8.6
#    Jan 05, 2021 04:44:54 PM +0200  platform: Windows NT

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

import TanachPageStud_support
import Studentmainmenu

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = TanachPageStud (root)
    TanachPageStud_support.init(root, top)
    root.mainloop()

w = None
def create_TanachPageStud(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_TanachPageStud(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = TanachPageStud (w)
    TanachPageStud_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_TanachPageStud():
    global w
    w.destroy()
    w = None

class TanachPageStud:
    def openMainmenue(self):
        root.destroy()
        Studentmainmenu.vp_start_gui()

    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("600x450+635+218")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(1,  1)
        top.title('''תנ"ך''')
        top.configure(background="#80ffff")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.TanachL = tk.Label(top)
        self.TanachL.place(relx=0.35, rely=0.067, height=41, width=174)
        self.TanachL.configure(activebackground="#000000")
        self.TanachL.configure(activeforeground="white")
        self.TanachL.configure(activeforeground="black")
        self.TanachL.configure(background="#ffb591")
        self.TanachL.configure(disabledforeground="#a3a3a3")
        self.TanachL.configure(font="-family {Segoe UI} -size 14 -weight bold -underline")
        self.TanachL.configure(foreground="#000000")
        self.TanachL.configure(highlightbackground="#d9d9d9")
        self.TanachL.configure(highlightcolor="black")
        self.TanachL.configure(relief="ridge")
        self.TanachL.configure(text='''תנ"ך''')

        self.MainMenuebtn = tk.Button(top)
        self.MainMenuebtn.place(relx=0.05, rely=0.844, height=54, width=127)
        self.MainMenuebtn.configure(activebackground="#ececec")
        self.MainMenuebtn.configure(activeforeground="#000000")
        self.MainMenuebtn.configure(background="#ffffff")
        self.MainMenuebtn.configure(disabledforeground="#a3a3a3")
        self.MainMenuebtn.configure(font="-family {Segoe UI} -size 14 -weight bold")
        self.MainMenuebtn.configure(foreground="#000000")
        self.MainMenuebtn.configure(highlightbackground="#d9d9d9")
        self.MainMenuebtn.configure(highlightcolor="black")
        self.MainMenuebtn.configure(pady="0")
        self.MainMenuebtn.configure(text='''תפריט ראשי''')
        self.MainMenuebtn.configure(command=self.openMainmenue)

        self.UploadAssBtn = tk.Button(top)
        self.UploadAssBtn.place(relx=0.517, rely=0.244, height=54, width=227)
        self.UploadAssBtn.configure(activebackground="#ececec")
        self.UploadAssBtn.configure(activeforeground="#000000")
        self.UploadAssBtn.configure(background="#00ff80")
        self.UploadAssBtn.configure(disabledforeground="#a3a3a3")
        self.UploadAssBtn.configure(font="-family {Segoe UI} -size 12 -weight bold")
        self.UploadAssBtn.configure(foreground="#000000")
        self.UploadAssBtn.configure(highlightbackground="#d9d9d9")
        self.UploadAssBtn.configure(highlightcolor="black")
        self.UploadAssBtn.configure(pady="0")
        self.UploadAssBtn.configure(text='''העלאת שיעורי בית''')

        self.watchMatirialBtn = tk.Button(top)
        self.watchMatirialBtn.place(relx=0.517, rely=0.422, height=54, width=227)

        self.watchMatirialBtn.configure(activebackground="#ececec")
        self.watchMatirialBtn.configure(activeforeground="#000000")
        self.watchMatirialBtn.configure(background="#00ff80")
        self.watchMatirialBtn.configure(disabledforeground="#a3a3a3")
        self.watchMatirialBtn.configure(font="-family {Segoe UI} -size 12 -weight bold")
        self.watchMatirialBtn.configure(foreground="#000000")
        self.watchMatirialBtn.configure(highlightbackground="#d9d9d9")
        self.watchMatirialBtn.configure(highlightcolor="black")
        self.watchMatirialBtn.configure(pady="0")
        self.watchMatirialBtn.configure(text='''צפייה בחומרי לימוד''')

        self.GetFeedbackbtn = tk.Button(top)
        self.GetFeedbackbtn.place(relx=0.517, rely=0.6, height=54, width=227)
        self.GetFeedbackbtn.configure(activebackground="#ececec")
        self.GetFeedbackbtn.configure(activeforeground="#000000")
        self.GetFeedbackbtn.configure(background="#00ff80")
        self.GetFeedbackbtn.configure(disabledforeground="#a3a3a3")
        self.GetFeedbackbtn.configure(font="-family {Segoe UI} -size 12 -weight bold")
        self.GetFeedbackbtn.configure(foreground="#000000")
        self.GetFeedbackbtn.configure(highlightbackground="#d9d9d9")
        self.GetFeedbackbtn.configure(highlightcolor="black")
        self.GetFeedbackbtn.configure(pady="0")
        self.GetFeedbackbtn.configure(text='''קבלת משוב על שיעורי בית''')

if __name__ == '__main__':
    vp_start_gui()





