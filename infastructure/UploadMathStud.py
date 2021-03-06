#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 6.0
#  in conjunction with Tcl version 8.6
#    Jan 05, 2021 08:13:21 PM +0200  platform: Windows NT

import sys
import pymongo
sys.path.append('..')
import ntpath

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

import UploadMathStud_support
import Studentmainmenu
from data import getUser, connect_to_db_and_collection, connect_to_db
import base64
import datetime
from tkinter import messagebox, filedialog

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    UploadMathStud_support.set_Tk_var()
    top = AssigUplMath (root)
    UploadMathStud_support.init(root, top)
    root.mainloop()

w = None
def create_AssigUplMath(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_AssigUplMath(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    UploadMathStud_support.set_Tk_var()
    top = AssigUplMath (w)
    UploadMathStud_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_AssigUplMath():
    global w
    w.destroy()
    w = None

class AssigUplMath:
    def openmainmenu(self):
        root.destroy()
        Studentmainmenu.vp_start_gui()

    def download_file(self):
        mycol = connect_to_db_and_collection('EZSchooldb', 'MathAssignments')
        data = mycol.find_one({'Assignment_num': int(self.DwnlSpnBX.get())})

        file = filedialog.asksaveasfile(initialdir='/', title="בחר שם ומיקום להורדה", mode='wb',
            filetypes=[('PDF files', '*pdf'), ('RAR files', '*.rar'), ('ZIP files', '*zip')],
                                        defaultextension='.pdf',initialfile=data['file_name'])

        if file == None:
            return
        file.write(base64.b64decode(data['Assignment_file']))

    def upload_file(self):
        if self.newfile == None:
            tk.messagebox.showwarning("העלאה", "לא נבחר אף קובץ")
            return

        upload_date = datetime.datetime.now()
        collection1 = connect_to_db_and_collection('EZSchooldb', f'''Assignments{self.current_user['id']}''')
        collection2 = connect_to_db_and_collection('EZSchooldb', 'MathAssignments')
        encoded_string = base64.b64encode(self.newfile.read())
        filename = ntpath.basename(self.newfile.name)
        assign_num = int(self.UplSpnBX.get())
        data = {'upload_time': upload_date,'file_name': filename, 'Assignment_file': encoded_string, 'Assignment_num': assign_num, 'Subject': 'Math'}
        flag1 = 0
        flag2=0

        assign = collection2.find_one({'Assignment_num': assign_num})
        dut_time = datetime.datetime.strptime(assign['due_in'], '%m/%d/%y')
        if dut_time < upload_date:
            flag1 = 1
        for assign in collection1.find({}):
            if assign['Assignment_num'] == assign_num:
                flag2 = 1
                break;

        if flag1 == 1:
            tk.messagebox.showwarning("העלאה לא אפשרית", "תאריך הגשה עבר")
        elif flag2==1:
            collection1.delete_one({'Assigment_num': assign_num})
            collection1.insert_one(data)
            root.destroy()
            Studentmainmenu.vp_start_gui()
        else:
            collection1.insert_one(data)
            root.destroy()
            Studentmainmenu.vp_start_gui()

    def chooseFile(self):
        self.newfile = None
        self.newfile = filedialog.askopenfile(initialdir='/', title="תבחר קובץ להעלאה", mode='rb',
            filetypes=[('PDF files', '*pdf'), ('RAR files', '*.rar'), ('ZIP files', '*zip')])


    def __init__(self, top=None):
        self.current_user = getUser()
        self.values = list(range(1, connect_to_db_and_collection('EZSchooldb', 'MathAssignments').estimated_document_count() +1))
        self.newfile = None
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("600x450+701+209")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(1,  1)
        top.title("העלאה וצפייה במטלות")
        top.configure(background="#80ffff")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Downloadassigmentbtn = tk.Button(top)
        self.Downloadassigmentbtn.place(relx=0.167, rely=0.267, height=74
                , width=237)
        self.Downloadassigmentbtn.configure(activebackground="#ececec")
        self.Downloadassigmentbtn.configure(activeforeground="#000000")
        self.Downloadassigmentbtn.configure(background="#ff8000")
        self.Downloadassigmentbtn.configure(disabledforeground="#a3a3a3")
        self.Downloadassigmentbtn.configure(font="-family {Segoe UI} -size 14 -weight bold")
        self.Downloadassigmentbtn.configure(foreground="#000000")
        self.Downloadassigmentbtn.configure(highlightbackground="#d9d9d9")
        self.Downloadassigmentbtn.configure(highlightcolor="black")
        self.Downloadassigmentbtn.configure(pady="0")
        self.Downloadassigmentbtn.configure(text='''הורד מטלה''')

        self.AssigDwnL = tk.Label(top)
        self.AssigDwnL.place(relx=0.633, rely=0.289, height=31, width=174)
        self.AssigDwnL.configure(activebackground="#f9f9f9")
        self.AssigDwnL.configure(activeforeground="black")
        self.AssigDwnL.configure(background="#00ff80")
        self.AssigDwnL.configure(cursor="fleur")
        self.AssigDwnL.configure(disabledforeground="#a3a3a3")
        self.AssigDwnL.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.AssigDwnL.configure(foreground="#000000")
        self.AssigDwnL.configure(highlightbackground="#d9d9d9")
        self.AssigDwnL.configure(highlightcolor="black")
        self.AssigDwnL.configure(relief="ridge")
        self.AssigDwnL.configure(text='''לבחירת מס' מטלה להורדה''')

        self.DwnlSpnBX = tk.Spinbox(top, from_=1.0, to=100.0)
        self.DwnlSpnBX.place(relx=0.667, rely=0.378, relheight=0.042
                , relwidth=0.225)
        self.DwnlSpnBX.configure(activebackground="#f9f9f9")
        self.DwnlSpnBX.configure(background="white")
        self.DwnlSpnBX.configure(buttonbackground="#d9d9d9")
        self.DwnlSpnBX.configure(disabledforeground="#a3a3a3")
        self.DwnlSpnBX.configure(font="TkDefaultFont")
        self.DwnlSpnBX.configure(foreground="black")
        self.DwnlSpnBX.configure(highlightbackground="black")
        self.DwnlSpnBX.configure(highlightcolor="black")
        self.DwnlSpnBX.configure(insertbackground="black")
        self.DwnlSpnBX.configure(justify='center')
        self.DwnlSpnBX.configure(selectbackground="blue")
        self.DwnlSpnBX.configure(selectforeground="white")



        self.choosefilebtn = tk.Button(top)
        self.choosefilebtn.place(relx=0.167, rely=0.511, height=74, width=237)
        self.choosefilebtn.configure(activebackground="#ececec")
        self.choosefilebtn.configure(activeforeground="#000000")
        self.choosefilebtn.configure(background="#ffff00")
        self.choosefilebtn.configure(disabledforeground="#a3a3a3")
        self.choosefilebtn.configure(font="-family {Segoe UI} -size 14 -weight bold")
        self.choosefilebtn.configure(foreground="#000000")
        self.choosefilebtn.configure(highlightbackground="#d9d9d9")
        self.choosefilebtn.configure(highlightcolor="black")
        self.choosefilebtn.configure(pady="0")
        self.choosefilebtn.configure(text='''לבחירת קובץ פתרונות''')

        self.UplSpnBX = tk.Spinbox(top, from_=1.0, to=100.0)
        self.UplSpnBX.place(relx=0.667, rely=0.622, relheight=0.042
                , relwidth=0.225)
        self.UplSpnBX.configure(activebackground="#f9f9f9")
        self.UplSpnBX.configure(background="white")
        self.UplSpnBX.configure(buttonbackground="#d9d9d9")
        self.UplSpnBX.configure(disabledforeground="#a3a3a3")
        self.UplSpnBX.configure(font="TkDefaultFont")
        self.UplSpnBX.configure(foreground="black")
        self.UplSpnBX.configure(highlightbackground="black")
        self.UplSpnBX.configure(highlightcolor="black")
        self.UplSpnBX.configure(insertbackground="black")
        self.UplSpnBX.configure(justify='center')
        self.UplSpnBX.configure(selectbackground="blue")
        self.UplSpnBX.configure(selectforeground="white")


        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.633, rely=0.533, height=31, width=174)
        self.Label1.configure(background="#00ff80")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(relief="ridge")
        self.Label1.configure(text='''לבחירת מס' מטלה להעלאה''')

        self.UploadBtn = tk.Button(top)
        self.UploadBtn.place(relx=0.383, rely=0.778, height=64, width=237)
        self.UploadBtn.configure(activebackground="#ececec")
        self.UploadBtn.configure(activeforeground="#000000")
        self.UploadBtn.configure(background="#ff0000")
        self.UploadBtn.configure(disabledforeground="#a3a3a3")
        self.UploadBtn.configure(font="-family {Segoe UI} -size 14 -weight bold -underline 1")
        self.UploadBtn.configure(foreground="#000000")
        self.UploadBtn.configure(highlightbackground="#d9d9d9")
        self.UploadBtn.configure(highlightcolor="black")
        self.UploadBtn.configure(pady="0")
        self.UploadBtn.configure(text='''להעלאת מטלה''')

        self.MainMenubtn = tk.Button(top)
        self.MainMenubtn.place(relx=0.033, rely=0.778, height=84, width=137)
        self.MainMenubtn.configure(activebackground="#ececec")
        self.MainMenubtn.configure(activeforeground="#000000")
        self.MainMenubtn.configure(background="#ffffff")
        self.MainMenubtn.configure(disabledforeground="#a3a3a3")
        self.MainMenubtn.configure(font="-family {Segoe UI} -size 14 -weight bold")
        self.MainMenubtn.configure(foreground="#000000")
        self.MainMenubtn.configure(highlightbackground="#d9d9d9")
        self.MainMenubtn.configure(highlightcolor="black")
        self.MainMenubtn.configure(pady="0")
        self.MainMenubtn.configure(text='''תפריט ראשי''')
        self.MainMenubtn.configure(command=self.openmainmenu)

        self.titleL = tk.Label(top)
        self.titleL.place(relx=0.317, rely=0.067, height=41, width=244)
        self.titleL.configure(background="#0080ff")
        self.titleL.configure(disabledforeground="#a3a3a3")
        self.titleL.configure(font="-family {Segoe UI} -size 14 -weight bold -underline 1")
        self.titleL.configure(foreground="#000000")
        self.titleL.configure(relief="ridge")
        self.titleL.configure(text='''חשבון''')

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        if self.values == []:
            self.DwnlSpnBX.configure(state='disabled')
            self.UplSpnBX.configure(state='disabled')
            self.UploadBtn.configure(state='disabled')
            self.Downloadassigmentbtn.configure(state='disabled')
            self.choosefilebtn.configure(state='disabled')
        else:
            self.DwnlSpnBX.configure(value=self.values)
            self.UplSpnBX.configure(value=self.values)
            self.UploadBtn.configure(command=self.upload_file)
            self.Downloadassigmentbtn.configure(command=self.download_file)
            self.choosefilebtn.configure(command=self.chooseFile)

if __name__ == '__main__':
    vp_start_gui()





