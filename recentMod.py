import os
import shutil
import stat
import time

source = "/Users/ajust/Desktop/FolderB/"
dest = "/Users/ajust/Desktop/newOrMod/"
files = os.listdir(source)
class copyFiles:
    for i in files:
        modified = os.stat(source+i)
        mtime = modified.st_mtime
        modDate = (time.time() - mtime)/3600
        if(modDate < 24):
            shutil.copy2(source+i, dest)
        else:
            pass


if __name__ == "__main__":
    copyFiles()