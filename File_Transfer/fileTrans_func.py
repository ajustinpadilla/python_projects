from tkinter import *
import tkinter as tk
from tkinter import filedialog
import shutil
import os
import stat
import time



import fileTrans_main
import fileTrans_gui


def getDir(self):
    dir = tk.filedialog.askdirectory()
    self.entry.delete(0,END)
    self.entry.insert(0,dir)

def getDir2(self):
    dir = tk.filedialog.askdirectory()
    self.entry2.delete(0,END)
    self.entry2.insert(0,dir)


def copyFiles(self):
    source = self.entry.get()+'/'
    dest = self.entry2.get()
    files = os.listdir(source)
    for i in files:
        modified = os.stat(source+i)
        mtime = modified.st_mtime
        modDate = (time.time() - mtime)/3600
        if(modDate < 24):
            shutil.copy2(source+i, dest)
        else:
            pass


if __name__ == "__main__":
   pass