import shutil
import os

#set where the source of the files are
source = '/Users/ajust/Desktop/FolderA/'

#set the destination path to folderB
destination = 'C:/Users/ajust/Desktop/FolderB/'
files = os.listdir(source)

for i in files:
    # We are saying move the files representedby 'i' to their new destination
    shutil.move(source+i, destination)