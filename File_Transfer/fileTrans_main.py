from tkinter import *
import tkinter as tk
import fileTrans_gui as gui
import fileTrans_func


class ParentWindow(Frame):
    def __init__(self,master):
        Frame.__init__(self, master)
        self.master = master
        # define window frame config
        self.master.minsize(700,300)
        self.master.title("File Transfer")
        gui.load_gui(self)








if __name__ == "__main__":
    root = tk.Tk()
    app = ParentWindow(root)
    root.mainloop()