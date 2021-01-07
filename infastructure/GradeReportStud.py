#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 6.0
#  in conjunction with Tcl version 8.6
#    Jan 07, 2021 08:03:17 AM +0200  platform: Windows NT

import sys
import pymongo
sys.path.append('..')

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

import GradeReportStud_support
from data import getUser, connect_to_db_and_collection

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = GradeReportStud (root)
    GradeReportStud_support.init(root, top)
    root.mainloop()

w = None
def create_GradeReportStud(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_GradeReportStud(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = GradeReportStud (w)
    GradeReportStud_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_GradeReportStud():
    global w
    w.destroy()
    w = None

class GradeReportStud:
    def insertonesubject(self,studcollec, assigncollec,theindex):
        for assignment in assigncollec.find({}):
            flag=0
            for studassign in studcollec.find({'grade': {'$exists': True}}):
                if studassign['Assignment_num'] == assignment['Assignment_num'] and studassign['Subject'] == 'Math':
                    self.GradeTree.insert(theindex, 'end', text="", values=(assignment['Assignment_num'],studassign['grade'] ))
                    flag=1
                    break
            if flag==0:
                self.GradeTree.insert(theindex, 'end', text="", values=(assignment['Assignment_num'], 0))


    def InsertGrades(self):
        studentassign = connect_to_db_and_collection('EZSchooldb', f'''Assignments{self.current_user['id']}''')
        mathassign = connect_to_db_and_collection('EZSchooldb', f'''MathAssignments''')
        historyassign = connect_to_db_and_collection('EZSchooldb', f'''HistoryAssignments''')
        hebrewassign =  connect_to_db_and_collection('EZSchooldb', f'''HebrewAssignments''')
        tanachassign = connect_to_db_and_collection('EZSchooldb', f'''TanachAssignments''')
        math1 = self.GradeTree.insert("", 1, 1, text='חשבון')
        hebrew1 = self.GradeTree.insert("", 2, 2, text='עברית')
        history1 = self.GradeTree.insert("", 3, 3, text='היסטוריה')
        tanach1 = self.GradeTree.insert("", 4, 4, text='''תנ"ך''')
        self.insertonesubject(studentassign, mathassign, math1)
        self.insertonesubject(studentassign, historyassign, history1)
        self.insertonesubject(studentassign, hebrewassign, hebrew1)
        self.insertonesubject(studentassign, tanachassign, tanach1)



    def __init__(self, top=None):
        self.current_user = getUser()


        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("600x450+633+236")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(1,  1)
        top.title("דוח ציונים")
        top.configure(background="#80ffff")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.NameL = tk.Label(top)
        self.NameL.place(relx=0.517, rely=0.067, height=41, width=214)
        self.NameL.configure(activebackground="#f9f9f9")
        self.NameL.configure(activeforeground="black")
        self.NameL.configure(background="#00ff40")
        self.NameL.configure(disabledforeground="#a3a3a3")
        self.NameL.configure(font="-family {Segoe UI} -size 14 -weight bold")
        self.NameL.configure(foreground="#000000")
        self.NameL.configure(highlightbackground="#d9d9d9")
        self.NameL.configure(highlightcolor="black")
        self.NameL.configure(relief="ridge")
        self.NameL.configure(text=f'''{self.current_user['name']}''')

        self.IdL = tk.Label(top)
        self.IdL.place(relx=0.517, rely=0.2, height=41, width=214)
        self.IdL.configure(activebackground="#f9f9f9")
        self.IdL.configure(activeforeground="black")
        self.IdL.configure(background="#00ff40")
        self.IdL.configure(disabledforeground="#a3a3a3")
        self.IdL.configure(font="-family {Segoe UI} -size 14 -weight bold")
        self.IdL.configure(foreground="#000000")
        self.IdL.configure(highlightbackground="#d9d9d9")
        self.IdL.configure(highlightcolor="black")
        self.IdL.configure(relief="ridge")
        self.IdL.configure(text=f'''{self.current_user['id']}''')

        self.GradeTree = ttk.Treeview(top)
        self.GradeTree["columns"] = ("one", "two")
        self.GradeTree.column("#0", width=100, minwidth=100, stretch=tk.NO)
        self.GradeTree.column("one", width=100, minwidth=100, stretch=tk.NO)
        self.GradeTree.column("two", width=150, minwidth=150, stretch=tk.NO)
        self.GradeTree.heading("#0", text="מקצוע", anchor=tk.W)
        self.GradeTree.heading("one", text="מטלה מס'", anchor=tk.W)
        self.GradeTree.heading("two", text="ציון", anchor=tk.W)
        self.GradeTree.place(relx=0.2, rely=0.4)

        self.InsertGrades()

if __name__ == '__main__':
    vp_start_gui()




