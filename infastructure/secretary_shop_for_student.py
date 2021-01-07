#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 5.6
#  in conjunction with Tcl version 8.6
#    Jan 07, 2021 10:25:45 PM +0200  platform: Windows NT

import sys
import pymongo
sys.path.append("..")
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

import secretary_shop_for_student_support
from data import connect_to_db_and_collection, findUser, user_db_init, inventory_db_init, GetChosenUser
user_db_init()
inventory_db_init()
client = pymongo.MongoClient()

mydb = client['EZSchooldb']
userobj=None
import Secretarymainmenu
import secretary_shop_for_student
import Payment_Shop_Secretary

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = student_shop (root)
    secretary_shop_for_student_support.init(root, top)
    root.mainloop()

w = None
def create_student_shop(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_student_shop(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = student_shop (w)
    secretary_shop_for_student_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_student_shop():
    global w
    w.destroy()
    w = None

class student_shop:
    def MainMenu(self):
        root.destroy()
        Secretarymainmenu.vp_start_gui()

    def Inventory_item_stock(self, name):
        inventory_collec = connect_to_db_and_collection('EZSchooldb', 'Inventory')
        theobj = inventory_collec.find_one({'item_name': name})
        return theobj['units_available']

    def back(self):
        root.destroy()
        Secretarymainmenu.vp_start_gui()


    def Update_Cart(self):
        self.cart_list = {'עיפרון HB2': int(self.pencil.get()), 'עט שחור 0.5': int(self.pen.get())
            , 'דפי משבצות A4 (חבילה 72)': int(self.math.get()),
                     'מרקרים': int(self.markers.get()),
                     'דפי שורות A4 (חבילה 72)': int(self.stripes.get()),
                     'קלסר שחור': int(self.binder.get()),'total price':self.total.get()}

        inventory_collec = connect_to_db_and_collection('EZSchooldb', 'Inventory')
        theobj = inventory_collec.find_one({'item_name': 'עיפרון HB2'})
        entered = self.pencil_entry.get()
        flag = 1
        sum = 0

        if entered == "":
            entered = "0"
        if flag:
            for c in entered:
                if c < '0' or c > '9':
                    flag = 0
                    tk.messagebox.showwarning('Store', 'כמות לא תקינה- חייב להכיל ספרות בלבד')

        if flag:
            entered = int(entered)
            if entered > theobj['units_available']:
                tk.messagebox.showwarning("Store", "אין כמות זו במלאי, אנא הכנס כמות אחרת")
                flag = 0

        if flag:
            sum = sum + theobj['price'] * entered
            self.pencil.set(entered)
            self.cart_list[theobj['item_name']] = entered
        else:
            sum = sum + theobj['price']*int(self.pencil.get())

        theobj = inventory_collec.find_one({'item_name': 'עט שחור 0.5'})
        entered = self.black_pen_entry.get()
        flag = 1

        if entered == "":
            entered = "0"
        if flag:
            for c in entered:
                if c < '0' or c > '9':
                    flag = 0
                    tk.messagebox.showwarning('Store', 'כמות לא תקינה- חייב להכיל ספרות בלבד')

        if flag:
            entered = int(entered)
            if entered > theobj['units_available']:
                tk.messagebox.showwarning("Store", "אין כמות זו במלאי, אנא הכנס כמות אחרת")
                flag = 0

        if flag:
            sum = sum + theobj['price'] * entered
            self.pen.set(entered)
            self.cart_list[theobj['item_name']] = entered
        else:
            sum = sum + theobj['price']*int(self.pen.get())

        theobj = inventory_collec.find_one({'item_name': 'דפי משבצות A4 (חבילה 72)'})
        entered = self.math_paper_entry.get()
        flag = 1

        if entered == "":
            entered = "0"
        if flag:
            for c in entered:
                if c < '0' or c > '9':
                    flag = 0
                    tk.messagebox.showwarning('Store', 'כמות לא תקינה- חייב להכיל ספרות בלבד')

        if flag:
            entered = int(entered)
            if entered > theobj['units_available']:
                tk.messagebox.showwarning("Store", "אין כמות זו במלאי, אנא הכנס כמות אחרת")
                flag = 0

        if flag:
            sum = sum + theobj['price'] * entered
            self.math.set(entered)
            self.cart_list[theobj['item_name']] = entered
        else:
            sum = sum + theobj['price']*int(self.math.get())

        theobj = inventory_collec.find_one({'item_name': 'מרקרים'})
        entered = self.markers_entry.get()
        flag = 1

        if entered == "":
            entered = "0"
        if flag:
            for c in entered:
                if c < '0' or c > '9':
                    flag = 0
                    tk.messagebox.showwarning('Store', 'כמות לא תקינה- חייב להכיל ספרות בלבד')

        if flag:
            entered = int(entered)
            if entered > theobj['units_available']:
                tk.messagebox.showwarning("Store", "אין כמות זו במלאי, אנא הכנס כמות אחרת")
                flag = 0

        if flag:
            sum = sum + theobj['price'] * entered
            self.markers.set(entered)
            self.cart_list[theobj['item_name']] = entered
        else:
            sum = sum + theobj['price'] * int(self.markers.get())

        theobj = inventory_collec.find_one({'item_name': 'דפי שורות A4 (חבילה 72)'})
        entered = self.stripe_paper_entry.get()
        flag = 1

        if entered == "":
            entered = "0"
        if flag:
            for c in entered:
                if c < '0' or c > '9':
                    flag = 0
                    tk.messagebox.showwarning('Store', 'כמות לא תקינה- חייב להכיל ספרות בלבד')

        if flag:
            entered = int(entered)
            if entered > theobj['units_available']:
                tk.messagebox.showwarning("Store", "אין כמות זו במלאי, אנא הכנס כמות אחרת")
                flag = 0

        if flag:
            sum = sum + theobj['price'] * entered
            self.stripes.set(entered)
            self.cart_list[theobj['item_name']] = entered
        else:
            sum = sum + theobj['price']*int(self.stripes.get())

        theobj = inventory_collec.find_one({'item_name': 'קלסר שחור'})
        entered = self.binder_entry.get()
        flag = 1

        if entered == "":
            entered = "0"
        if flag:
            for c in entered:
                if c < '0' or c > '9':
                    flag = 0
                    tk.messagebox.showwarning('Store', 'כמות לא תקינה- חייב להכיל ספרות בלבד')

        if flag:
            entered = int(entered)
            if entered > theobj['units_available']:
                tk.messagebox.showwarning("Store", "אין כמות זו במלאי, אנא הכנס כמות אחרת")
                flag = 0

        if flag:
            sum = sum + theobj['price'] * entered
            self.binder.set(entered)
            self.cart_list[theobj['item_name']] = entered
        else:
            sum = sum + theobj['price']*int(self.binder.get())

        self.total.set(sum)
        self.cart_list['total price'] = sum
        my_collec=connect_to_db_and_collection('EZSchooldb','Users')
        my_collec.update_one({'id':self.current_user['id']},{'$set':{'cart':self.cart_list}})

    def Go_To_Payment(self):
        if self.cart_list==None or self.cart_list['total price']==0:
            tk.messagebox.showwarning("Store","עגלה ריקה")
        else:
            root.destroy()
            Payment_Shop_Secretary.vp_start_gui()

    def __init__(self, top=None):
        self.cart_list=None
        self.pencil = tk.StringVar(value='0')
        self.pen = tk.StringVar(value='0')
        self.math = tk.StringVar(value='0')
        self.markers = tk.StringVar(value='0')
        self.stripes = tk.StringVar(value='0')
        self.binder = tk.StringVar(value='0')
        self.total =tk.StringVar(value='0')
        self.current_user=GetChosenUser()

        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("1131x761+391+128")
        top.minsize(148, 1)
        top.maxsize(1924, 1055)
        top.resizable(1,  1)
        top.title("חנות תלמיד")
        top.configure(background="#7cacf3")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")
        self.Message1 = tk.Message(top)
        self.Message1.place(relx=0.451, rely=0.026, relheight=0.038
                            , relwidth=0.104)
        self.Message1.configure(background="#7cacf3")
        self.Message1.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.Message1.configure(foreground="#000000")
        self.Message1.configure(highlightbackground="#d9d9d9")
        self.Message1.configure(highlightcolor="black")
        self.Message1.configure(text='''כמות במלאי''')
        self.Message1.configure(width=118)

        self.Message2 = tk.Message(top)
        self.Message2.place(relx=0.301, rely=0.026, relheight=0.038
                            , relwidth=0.095)
        self.Message2.configure(background="#7cacf3")
        self.Message2.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.Message2.configure(foreground="#000000")
        self.Message2.configure(highlightbackground="#d9d9d9")
        self.Message2.configure(highlightcolor="black")
        self.Message2.configure(text='''בחירת כמות''')
        self.Message2.configure(width=106)

        self.pencil_entry = tk.Entry(top)
        self.pencil_entry.place(relx=0.3, rely=0.105, height=34, relwidth=0.101)
        self.pencil_entry.configure(background="white")
        self.pencil_entry.configure(disabledforeground="#a3a3a3")
        self.pencil_entry.configure(font="TkFixedFont")
        self.pencil_entry.configure(foreground="#000000")
        self.pencil_entry.configure(highlightbackground="#d9d9d9")
        self.pencil_entry.configure(highlightcolor="black")
        self.pencil_entry.configure(insertbackground="black")
        self.pencil_entry.configure(selectbackground="blue")
        self.pencil_entry.configure(selectforeground="white")

        self.pencil_stock = tk.Button(top)
        self.pencil_stock.place(relx=0.469, rely=0.092, height=43, width=76)
        self.pencil_stock.configure(activebackground="#ececec")
        self.pencil_stock.configure(activeforeground="#000000")
        self.pencil_stock.configure(background="#d3bdd9")
        self.pencil_stock.configure(disabledforeground="#a3a3a3")
        self.pencil_stock.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.pencil_stock.configure(foreground="#000000")
        self.pencil_stock.configure(highlightbackground="#d9d9d9")
        self.pencil_stock.configure(highlightcolor="black")
        self.pencil_stock.configure(pady="0")
        self.pencil_stock.configure(text=self.Inventory_item_stock('עיפרון HB2'))

        self.update_cart = tk.Button(top)
        self.update_cart.place(relx=0.08, rely=0.71, height=63, width=186)
        self.update_cart.configure(activebackground="#ececec")
        self.update_cart.configure(activeforeground="#000000")
        self.update_cart.configure(background="#2d79ec")
        self.update_cart.configure(cursor="hand2")
        self.update_cart.configure(disabledforeground="#a3a3a3")
        self.update_cart.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.update_cart.configure(foreground="#000000")
        self.update_cart.configure(highlightbackground="#d9d9d9")
        self.update_cart.configure(highlightcolor="black")
        self.update_cart.configure(pady="0")
        self.update_cart.configure(text='''עדכון עגלה''')
        self.update_cart.configure(command=self.Update_Cart)

        self.black_pen_entry = tk.Entry(top)
        self.black_pen_entry.place(relx=0.301, rely=0.223, height=34
                                   , relwidth=0.101)
        self.black_pen_entry.configure(background="white")
        self.black_pen_entry.configure(disabledforeground="#a3a3a3")
        self.black_pen_entry.configure(font="TkFixedFont")
        self.black_pen_entry.configure(foreground="#000000")
        self.black_pen_entry.configure(highlightbackground="#d9d9d9")
        self.black_pen_entry.configure(highlightcolor="black")
        self.black_pen_entry.configure(insertbackground="black")
        self.black_pen_entry.configure(selectbackground="blue")
        self.black_pen_entry.configure(selectforeground="white")

        self.math_paper_entry = tk.Entry(top)
        self.math_paper_entry.place(relx=0.301, rely=0.342, height=34
                                    , relwidth=0.101)
        self.math_paper_entry.configure(background="white")
        self.math_paper_entry.configure(disabledforeground="#a3a3a3")
        self.math_paper_entry.configure(font="TkFixedFont")
        self.math_paper_entry.configure(foreground="#000000")
        self.math_paper_entry.configure(highlightbackground="#d9d9d9")
        self.math_paper_entry.configure(highlightcolor="black")
        self.math_paper_entry.configure(insertbackground="black")
        self.math_paper_entry.configure(selectbackground="blue")
        self.math_paper_entry.configure(selectforeground="white")

        self.markers_entry = tk.Entry(top)
        self.markers_entry.place(relx=0.301, rely=0.46, height=34
                                 , relwidth=0.101)
        self.markers_entry.configure(background="white")
        self.markers_entry.configure(disabledforeground="#a3a3a3")
        self.markers_entry.configure(font="TkFixedFont")
        self.markers_entry.configure(foreground="#000000")
        self.markers_entry.configure(highlightbackground="#d9d9d9")
        self.markers_entry.configure(highlightcolor="black")
        self.markers_entry.configure(insertbackground="black")
        self.markers_entry.configure(selectbackground="blue")
        self.markers_entry.configure(selectforeground="white")

        self.stripe_paper_entry = tk.Entry(top)
        self.stripe_paper_entry.place(relx=0.301, rely=0.578, height=34
                                      , relwidth=0.101)
        self.stripe_paper_entry.configure(background="white")
        self.stripe_paper_entry.configure(disabledforeground="#a3a3a3")
        self.stripe_paper_entry.configure(font="TkFixedFont")
        self.stripe_paper_entry.configure(foreground="#000000")
        self.stripe_paper_entry.configure(highlightbackground="#d9d9d9")
        self.stripe_paper_entry.configure(highlightcolor="black")
        self.stripe_paper_entry.configure(insertbackground="black")
        self.stripe_paper_entry.configure(selectbackground="blue")
        self.stripe_paper_entry.configure(selectforeground="white")

        self.binder_entry = tk.Entry(top)
        self.binder_entry.place(relx=0.301, rely=0.696, height=34
                                , relwidth=0.101)
        self.binder_entry.configure(background="white")
        self.binder_entry.configure(disabledforeground="#a3a3a3")
        self.binder_entry.configure(font="TkFixedFont")
        self.binder_entry.configure(foreground="#000000")
        self.binder_entry.configure(highlightbackground="#d9d9d9")
        self.binder_entry.configure(highlightcolor="black")
        self.binder_entry.configure(insertbackground="black")
        self.binder_entry.configure(selectbackground="blue")
        self.binder_entry.configure(selectforeground="white")

        self.black_pen_stock = tk.Button(top)
        self.black_pen_stock.place(relx=0.469, rely=0.21, height=43, width=76)
        self.black_pen_stock.configure(activebackground="#ececec")
        self.black_pen_stock.configure(activeforeground="#000000")
        self.black_pen_stock.configure(background="#d3bdd9")
        self.black_pen_stock.configure(disabledforeground="#a3a3a3")
        self.black_pen_stock.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.black_pen_stock.configure(foreground="#000000")
        self.black_pen_stock.configure(highlightbackground="#d9d9d9")
        self.black_pen_stock.configure(highlightcolor="black")
        self.black_pen_stock.configure(pady="0")
        self.black_pen_stock.configure(text=self.Inventory_item_stock('עט שחור 0.5'))

        self.math_paper_stock = tk.Button(top)
        self.math_paper_stock.place(relx=0.469, rely=0.329, height=43, width=76)
        self.math_paper_stock.configure(activebackground="#ececec")
        self.math_paper_stock.configure(activeforeground="#000000")
        self.math_paper_stock.configure(background="#d3bdd9")
        self.math_paper_stock.configure(disabledforeground="#a3a3a3")
        self.math_paper_stock.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.math_paper_stock.configure(foreground="#000000")
        self.math_paper_stock.configure(highlightbackground="#d9d9d9")
        self.math_paper_stock.configure(highlightcolor="black")
        self.math_paper_stock.configure(pady="0")
        self.math_paper_stock.configure(text=self.Inventory_item_stock('דפי משבצות A4 (חבילה 72)'))

        self.markers_stock = tk.Button(top)
        self.markers_stock.place(relx=0.469, rely=0.447, height=43, width=76)
        self.markers_stock.configure(activebackground="#ececec")
        self.markers_stock.configure(activeforeground="#000000")
        self.markers_stock.configure(background="#d3bdd9")
        self.markers_stock.configure(disabledforeground="#a3a3a3")
        self.markers_stock.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.markers_stock.configure(foreground="#000000")
        self.markers_stock.configure(highlightbackground="#d9d9d9")
        self.markers_stock.configure(highlightcolor="black")
        self.markers_stock.configure(pady="0")
        self.markers_stock.configure(text=self.Inventory_item_stock('מרקרים'))

        self.stripe_paper_stock = tk.Button(top)
        self.stripe_paper_stock.place(relx=0.469, rely=0.565, height=43
                                      , width=76)
        self.stripe_paper_stock.configure(activebackground="#ececec")
        self.stripe_paper_stock.configure(activeforeground="#000000")
        self.stripe_paper_stock.configure(background="#d3bdd9")
        self.stripe_paper_stock.configure(disabledforeground="#a3a3a3")
        self.stripe_paper_stock.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.stripe_paper_stock.configure(foreground="#000000")
        self.stripe_paper_stock.configure(highlightbackground="#d9d9d9")
        self.stripe_paper_stock.configure(highlightcolor="black")
        self.stripe_paper_stock.configure(pady="0")
        self.stripe_paper_stock.configure(text=self.Inventory_item_stock('דפי שורות A4 (חבילה 72)'))

        self.binder_stock = tk.Button(top)
        self.binder_stock.place(relx=0.469, rely=0.683, height=43, width=76)
        self.binder_stock.configure(activebackground="#ececec")
        self.binder_stock.configure(activeforeground="#000000")
        self.binder_stock.configure(background="#d3bdd9")
        self.binder_stock.configure(disabledforeground="#a3a3a3")
        self.binder_stock.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.binder_stock.configure(foreground="#000000")
        self.binder_stock.configure(highlightbackground="#d9d9d9")
        self.binder_stock.configure(highlightcolor="black")
        self.binder_stock.configure(pady="0")
        self.binder_stock.configure(text=self.Inventory_item_stock('קלסר שחור'))

        self.Message3 = tk.Message(top)
        self.Message3.place(relx=0.645, rely=0.907, relheight=0.066
                            , relwidth=0.173)
        self.Message3.configure(background="#7cacf3")
        self.Message3.configure(font="-family {Segoe UI} -size 10 -weight bold -underline 1")
        self.Message3.configure(foreground="#000000")
        self.Message3.configure(highlightbackground="#d9d9d9")
        self.Message3.configure(highlightcolor="black")
        self.Message3.configure(text='''סהכ לחיוב''')
        self.Message3.configure(width=197)

        self.total_cost = tk.Message(top)
        self.total_cost.place(relx=0.513, rely=0.907, height=53, width=156)
        self.total_cost.configure(background="#7cacf3")
        self.total_cost.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.total_cost.configure(foreground="#000000")
        self.total_cost.configure(highlightbackground="#d9d9d9")
        self.total_cost.configure(highlightcolor="black")
        self.total_cost.configure(pady="0")
        self.total_cost.configure(textvariable=self.total)

        self.mainmenu = tk.Button(top)
        self.mainmenu.place(relx=0.018, rely=0.88, height=73, width=166)
        self.mainmenu.configure(activebackground="#ececec")
        self.mainmenu.configure(activeforeground="#000000")
        self.mainmenu.configure(background="#1155bb")
        self.mainmenu.configure(disabledforeground="#a3a3a3")
        self.mainmenu.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.mainmenu.configure(foreground="#000000")
        self.mainmenu.configure(highlightbackground="#d9d9d9")
        self.mainmenu.configure(highlightcolor="black")
        self.mainmenu.configure(pady="0")
        self.mainmenu.configure(text='''תפריט ראשי''')
        self.mainmenu.configure(command=self.MainMenu)

        self.payment_button = tk.Button(top)
        self.payment_button.place(relx=0.256, rely=0.88, height=73, width=256)
        self.payment_button.configure(activebackground="#ececec")
        self.payment_button.configure(activeforeground="#000000")
        self.payment_button.configure(background="#2d79ec")
        self.payment_button.configure(disabledforeground="#a3a3a3")
        self.payment_button.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.payment_button.configure(foreground="#000000")
        self.payment_button.configure(highlightbackground="#d9d9d9")
        self.payment_button.configure(highlightcolor="black")
        self.payment_button.configure(pady="0")
        self.payment_button.configure(text='''תשלום''')
        self.payment_button.configure(command=self.Go_To_Payment)

        self.menubar = tk.Menu(top, font="TkMenuFont", bg=_bgcolor, fg=_fgcolor)
        top.configure(menu=self.menubar)

        self.cart_msg = tk.Message(top)
        self.cart_msg.place(relx=0.858, rely=0.039, relheight=0.038
                            , relwidth=0.067)
        self.cart_msg.configure(background="#7cacf3")
        self.cart_msg.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.cart_msg.configure(foreground="#000000")
        self.cart_msg.configure(highlightbackground="#d9d9d9")
        self.cart_msg.configure(highlightcolor="black")
        self.cart_msg.configure(text='''עגלה''')
        self.cart_msg.configure(width=70)

        self.pencil_msg = tk.Message(top)
        self.pencil_msg.place(relx=0.884, rely=0.105, relheight=0.039
                              , relwidth=0.094)
        self.pencil_msg.configure(background="#7cacf3")
        self.pencil_msg.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.pencil_msg.configure(foreground="#000000")
        self.pencil_msg.configure(highlightbackground="#d9d9d9")
        self.pencil_msg.configure(highlightcolor="black")
        self.pencil_msg.configure(text='''עפרון HB2''')
        self.pencil_msg.configure(width=106)

        self.pencil_q_msg = tk.Message(top)
        self.pencil_q_msg.place(relx=0.805, rely=0.105, relheight=0.039
                                , relwidth=0.067)
        self.pencil_q_msg.configure(background="#7cacf3")
        self.pencil_q_msg.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.pencil_q_msg.configure(foreground="#000000")
        self.pencil_q_msg.configure(highlightbackground="#d9d9d9")
        self.pencil_q_msg.configure(highlightcolor="black")
        self.pencil_q_msg.configure(textvariable=self.pencil)
        self.pencil_q_msg.configure(width=70)

        self.black_pen__msg = tk.Message(top)
        self.black_pen__msg.place(relx=0.884, rely=0.223, relheight=0.051
                                  , relwidth=0.103)
        self.black_pen__msg.configure(background="#7cacf3")
        self.black_pen__msg.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.black_pen__msg.configure(foreground="#000000")
        self.black_pen__msg.configure(highlightbackground="#d9d9d9")
        self.black_pen__msg.configure(highlightcolor="black")
        self.black_pen__msg.configure(text='''עט שחור''')
        self.black_pen__msg.configure(width=116)

        self.black_pen_q_msg = tk.Message(top)
        self.black_pen_q_msg.place(relx=0.805, rely=0.21, relheight=0.053
                                   , relwidth=0.066)
        self.black_pen_q_msg.configure(background="#7cacf3")
        self.black_pen_q_msg.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.black_pen_q_msg.configure(foreground="#000000")
        self.black_pen_q_msg.configure(highlightbackground="#d9d9d9")
        self.black_pen_q_msg.configure(highlightcolor="black")
        self.black_pen_q_msg.configure(textvariable=self.pen)
        self.black_pen_q_msg.configure(width=75)

        self.math_paper_msg = tk.Message(top)
        self.math_paper_msg.place(relx=0.875, rely=0.315, relheight=0.051
                                  , relwidth=0.103)
        self.math_paper_msg.configure(background="#7cacf3")
        self.math_paper_msg.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.math_paper_msg.configure(foreground="#000000")
        self.math_paper_msg.configure(highlightbackground="#d9d9d9")
        self.math_paper_msg.configure(highlightcolor="black")
        self.math_paper_msg.configure(text='''דפדפת חשבון''')
        self.math_paper_msg.configure(width=116)

        self.Message4 = tk.Message(top)
        self.Message4.place(relx=0.805, rely=0.302, relheight=0.078
                            , relwidth=0.065)
        self.Message4.configure(background="#7cacf3")
        self.Message4.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.Message4.configure(foreground="#000000")
        self.Message4.configure(highlightbackground="#d9d9d9")
        self.Message4.configure(highlightcolor="black")
        self.Message4.configure(textvariable=self.math)
        self.Message4.configure(width=74)

        self.markers_msg = tk.Message(top)
        self.markers_msg.place(relx=0.875, rely=0.434, relheight=0.067
                               , relwidth=0.118)
        self.markers_msg.configure(background="#7cacf3")
        self.markers_msg.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.markers_msg.configure(foreground="#000000")
        self.markers_msg.configure(highlightbackground="#d9d9d9")
        self.markers_msg.configure(highlightcolor="black")
        self.markers_msg.configure(text='''מרקרים''')
        self.markers_msg.configure(width=134)

        self.Message5 = tk.Message(top)
        self.Message5.place(relx=0.805, rely=0.447, relheight=0.038
                            , relwidth=0.067)
        self.Message5.configure(background="#7cacf3")
        self.Message5.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.Message5.configure(foreground="#000000")
        self.Message5.configure(highlightbackground="#d9d9d9")
        self.Message5.configure(highlightcolor="black")
        self.Message5.configure(textvariable=self.markers)
        self.Message5.configure(width=70)

        self.strip_paper_msg = tk.Message(top)
        self.strip_paper_msg.place(relx=0.875, rely=0.552, relheight=0.053
                                   , relwidth=0.103)
        self.strip_paper_msg.configure(background="#7cacf3")
        self.strip_paper_msg.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.strip_paper_msg.configure(foreground="#000000")
        self.strip_paper_msg.configure(highlightbackground="#d9d9d9")
        self.strip_paper_msg.configure(highlightcolor="black")
        self.strip_paper_msg.configure(text='''דפדפת שורות''')
        self.strip_paper_msg.configure(width=116)

        self.Message6 = tk.Message(top)
        self.Message6.place(relx=0.805, rely=0.552, relheight=0.053
                            , relwidth=0.067)
        self.Message6.configure(background="#7cacf3")
        self.Message6.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.Message6.configure(foreground="#000000")
        self.Message6.configure(highlightbackground="#d9d9d9")
        self.Message6.configure(highlightcolor="black")
        self.Message6.configure(textvariable=self.stripes)
        self.Message6.configure(width=76)

        self.Message7 = tk.Message(top)
        self.Message7.place(relx=0.884, rely=0.67, relheight=0.051
                            , relwidth=0.094)
        self.Message7.configure(background="#7cacf3")
        self.Message7.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.Message7.configure(foreground="#000000")
        self.Message7.configure(highlightbackground="#d9d9d9")
        self.Message7.configure(highlightcolor="black")
        self.Message7.configure(text='''קלסר''')
        self.Message7.configure(width=106)

        self.Message8 = tk.Message(top)
        self.Message8.place(relx=0.805, rely=0.683, relheight=0.038
                            , relwidth=0.067)
        self.Message8.configure(background="#7cacf3")
        self.Message8.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.Message8.configure(foreground="#000000")
        self.Message8.configure(highlightbackground="#d9d9d9")
        self.Message8.configure(highlightcolor="black")
        self.Message8.configure(textvariable=self.binder)
        self.Message8.configure(width=70)


if __name__ == '__main__':
    vp_start_gui()





