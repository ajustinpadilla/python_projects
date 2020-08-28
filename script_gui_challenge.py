from tkinter import *
import tkinter as tk
from tkinter import filedialog

class Window(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)

        self.master=master
        self.master.minsize(500,300)

        self.master.title("Check files")


        self.btn_browse = tk.Button(self.master, text="Browse...", width=10, command=lambda: getDir(self))
        self.btn_browse.grid(row=0, column=0, padx=(10,0), pady=(40,0))
        self.btn_browse2 = tk.Button(self.master, text="Browse...")
        self.btn_browse2.grid(row=1, column=0, padx=(10,0), pady=(10,0))
        self.btn_check = tk.Button(self.master, text="Check for files...")
        self.btn_check.grid(row=3, column=0, padx=(10,0), pady=(10,0))
        self.btn_close = tk.Button(self.master, text="Close Program")
        self.btn_close.grid(row=3, column=4, sticky=W, padx=(10,0), pady=(10,0))


        self.entry = tk.Entry(self.master, text="")
        self.entry.grid(row=0, column=1, columnspan=3)
        self.entry2 = tk.Entry(self.master, text="")
        self.entry2.grid(row=1, column=1, columnspan=3)




def getDir(self):
    dir = tk.filedialog.askdirectory()
    self.entry.delete(0,END)
    self.entry.insert(0,dir)


if __name__ == "__main__":
    root = tk.Tk()
    app = Window(root)
    root.mainloop()