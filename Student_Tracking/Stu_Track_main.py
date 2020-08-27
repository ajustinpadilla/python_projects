# Python ver:   3.8.3
#
# Author:       Angel Padilla
#
# Purpose:      Practice building a app that tracks student infomation
#
# Tested OS:`   This code was tested for use with Windows 10.
from tkinter import *
import tkinter as tk

# importing other modules
import Stu_Track_GUI
import Stu_Track_func


class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        # Define master frame
        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('700x500')
        self.master.title("Student Tracking")
        self.master.configure(bg="forestgreen")

        #loads GUI
        Stu_Track_GUI.load_gui(self)


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()