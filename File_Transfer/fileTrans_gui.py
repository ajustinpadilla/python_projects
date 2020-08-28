from tkinter import *
import tkinter as tk

import fileTrans_main
import fileTrans_func

def load_gui(self):

    self.btn_browse = tk.Button(self.master, text="Files to be copied", width=15, font=("Helvetica, 16"), command=lambda: fileTrans_func.getDir(self))
    self.btn_browse.grid(row=0, column=0, padx=(30,0), pady=(40,0))
    self.btn_browse2 = tk.Button(self.master, text="Destination", width=15, font=("Helvetica, 16"), command=lambda: fileTrans_func.getDir2(self))
    self.btn_browse2.grid(row=1, column=0, padx=(30,0), pady=(30,0))
    self.btn_check = tk.Button(self.master, text="File Check", width=15, font=("Helvetica, 16"), command= lambda: fileTrans_func.copyFiles(self))
    self.btn_check.grid(row=3, column=0, padx=(30,0), pady=(30,0))
    self.btn_close = tk.Button(self.master, text="Close Program", width=15, font=("Helvetica, 16"))
    self.btn_close.grid(row=3, column=4, sticky=W, padx=(0,30), pady=(30,0))


    self.entry = tk.Entry(self.master, text="", font=("Helvetica, 16"))
    self.entry.grid(row=0, column=1, columnspan=3, padx=(30,0), pady=(30,0))
    self.entry2 = tk.Entry(self.master, text="", font=("Helvetica, 16"))
    self.entry2.grid(row=1, column=1, columnspan=3, padx=(30,0), pady=(30,0))






if __name__ == "__main__":
    pass