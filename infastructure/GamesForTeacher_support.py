#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 6.0
#  in conjunction with Tcl version 8.6
#    Jan 03, 2021 02:24:33 PM +0200  platform: Windows NT
#    Dec 27, 2020 05:12:45 PM +0200  platform: Windows NT
#    Dec 27, 2020 05:12:45 PM +0200  platform: Windows NT

#    Jan 03, 2021 02:24:33 PM +0200  platform: Windows NT
#    Dec 27, 2020 05:12:45 PM +0200  platform: Windows NT
#    Dec 31, 2020 11:42:46 AM +0200  platform: Windows NT


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

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import GamesForTeacher
    GamesForTeacher.vp_start_gui()




