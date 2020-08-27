import os
from tkinter import *
from tkinter import messagebox
import tkinter
import sqlite3

# importing other modules
import Stu_Track_main
import Stu_Track_GUI


# Creating the database if it hasn't yet
def create_db(self):
    conn = sqlite3.connect("Student_info.db")
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS tbl_student_info( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            fname TEXT, \
            lname TEXT, \
            fullname TEXT, \
            phone TEXT, \
            email TEXT, \
            courseTaken TEXT);")
        conn.commit()
    conn.close()

def onSelect(self, event):
    varList = event.widget
    select = varList.curselection()[0]
    value = varList.get(select)
    conn = sqlite3.connect("Student_info.db")
    with conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT fname,lname,phone,email,courseTaken FROM tbl_student_info WHERE fullname = (?)""", [value])
        varBody = cursor.fetchall()
        # This returns a tuple and we can slice it into 4 parts using data[] during the iteration
        for data in varBody:
            self.txt_fname.delete(0,END)
            self.txt_fname.insert(0,data[0])
            self.txt_lname.delete(0,END)
            self.txt_lname.insert(0,data[1])
            self.txt_phone.delete(0,END)
            self.txt_phone.insert(0,data[2])
            self.txt_email.delete(0,END)
            self.txt_email.insert(0,data[3])
            self.txt_course.delete(0,END)
            self.txt_course.insert(0,data[4])

def onSubmit(self):
    fname = self.txt_fname.get().strip().title()
    lname = self.txt_lname.get().strip().title()
    #stripping off extra spaces that might have been put in
    fname = fname.strip()
    lname = lname.strip()
    fname = fname.title()
    lname = lname.title()
    fullname = ("{} {}".format(fname,lname))
    phone = self.txt_phone.get().strip()
    email = self.txt_email.get().strip()
    course = self.txt_course.get().strip()
    if (len(fname) > 0) and (len(lname) > 0) and (len(phone) > 0) and(len(email) > 0) and (len(course) > 0):
        conn = sqlite3.connect('Student_info.db')
        with conn:
            cursor = conn.cursor()
            cursor.execute("""INSERT INTO tbl_student_info (fname,lname,fullname,phone,email,courseTaken) VALUES (?,?,?,?,?,?)""",(fname, lname, fullname, phone, email, course))
            self.lstbox.insert(END, fullname)
            onClear(self)
        conn.commit()
        conn.close()
    else:
        messagebox.showerror("Missing Text Error","Please ensure that there is data in all four fields.")
    

def onClear(self):
    # clear the text in these textboxes
    self.txt_fname.delete(0,END)
    self.txt_lname.delete(0,END)
    self.txt_phone.delete(0,END)
    self.txt_email.delete(0,END)
    self.txt_course.delete(0,END)

def onDelete(self):
    selected = self.lstbox.get(self.lstbox.curselection())
    conn = sqlite3.connect('Student_info.db')
    with conn:
        cur = conn.cursor()
        # Making sure to not delete the last record to avoid an error
        cur.execute("""SELECT COUNT(*) FROM tbl_student_info""")
        count = cur.fetchone()[0]
        if count > 1:
            confirm = messagebox.askokcancel("Delete Confirmation", "All information associated with, ({}) \nwill be permenantly deleted from the database. \n\nProceed with the deletion request?".format(selected))
            if confirm:
                conn = sqlite3.connect('Student_info.db')
                with conn:
                    cursor = conn.cursor()
                    cursor.execute("""DELETE FROM tbl_student_info WHERE fullname = '{}'""".format(selected))
                onDeleted(self)
                conn.commit()
        else:
            confirm = messagebox.showerror("Last Record Error", "({}) is the last record in the database and cannot be deleted at this time. \n\nPlease add another record first before you can delete ({}).".format(selected,selected))
    conn.close()

def onDeleted(self):
    onClear(self)
    try:
        index = self.lstbox.curselection()[0]
        self.lstbox.delete(index)
    except IndexError:
        pass

def onRefresh(self):
    # Populate the listbox, coinciding with the database
    self.lstbox.delete(0,END)
    conn = sqlite3.connect('Student_info.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT COUNT(*) FROM tbl_student_info""")
        count = cursor.fetchone()[0]
        i = 0
        while i < count:
                cursor.execute("""SELECT fullname FROM tbl_student_info""")
                varList = cursor.fetchall()[i]
                for item in varList:
                    self.lstbox.insert(0,str(item))
                    i = i + 1
    conn.close()