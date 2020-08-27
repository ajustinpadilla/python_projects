
from tkinter import *
import tkinter as tk

# importing other modules
import Stu_Track_main
import Stu_Track_func


def load_gui(self):

    # defining labels for input boxes
    self.lbl_fname = tk.Label(self.master, text="First Name:", font=("Helvetica, 16"), bg='forestgreen')
    self.lbl_fname.grid(row=0, column=0, padx=(30,0), pady=(10,0), sticky=N+W)
    self.lbl_lname = tk.Label(self.master, text="Last Name:", font=("Helvetica, 16"), bg='forestgreen')
    self.lbl_lname.grid(row=2, column=0, padx=(30,0), pady=(10,0), sticky=N+W)
    self.lbl_phone = tk.Label(self.master, text="Phone Number:", font=("Helvetica, 16"), bg='forestgreen')
    self.lbl_phone.grid(row=4, column=0, padx=(30,0), pady=(10,0), sticky=N+W)
    self.lbl_email = tk.Label(self.master, text="Email Address:", font=("Helvetica, 16"), bg='forestgreen')
    self.lbl_email.grid(row=6, column=0, padx=(30,0), pady=(10,0), sticky=N+W)
    self.lbl_course = tk.Label(self.master, text="Course:", font=("Helvetica, 16"), bg='forestgreen')
    self.lbl_course.grid(row=8, column=0, padx=(30,0), pady=(10,0), sticky=N+W)
    self.lbl_course = tk.Label(self.master, text="Student:", font=("Helvetica, 16"), bg='forestgreen')
    self.lbl_course.grid(row=0, column=4, padx=(30,0), pady=(10,0), sticky=N+W)

    # defining text boxes
    self.txt_fname = tk.Entry(self.master, text="", font=("Helvetica, 16"), bg="black", fg='purple')
    self.txt_fname.grid(row=1, column=0, columnspan=4, padx=(30,0), pady=(10,0), stick=N+W+E)
    self.txt_lname = tk.Entry(self.master, text="", font=("Helvetica, 16"), bg="black", fg='purple')
    self.txt_lname.grid(row=3, column=0, columnspan=4, padx=(30,0), pady=(10,0), stick=N+W+E)
    self.txt_phone = tk.Entry(self.master, text="", font=("Helvetica, 16"), bg="black", fg='purple')
    self.txt_phone.grid(row=5, column=0, columnspan=4, padx=(30,0), pady=(10,0), stick=N+W+E)
    self.txt_email = tk.Entry(self.master, text="", font=("Helvetica, 16"), bg="black", fg='purple')
    self.txt_email.grid(row=7, column=0, columnspan=4, padx=(30,0), pady=(10,0), stick=N+W+E)
    self.txt_course = tk.Entry(self.master, text="", font=("Helvetica, 16"), bg="black", fg='purple')
    self.txt_course.grid(row=9, column=0, columnspan=4, padx=(30,0), pady=(10,0), stick=N+W+E)


    # Defining the listbox with a scroll bar
    self.scrollbar = Scrollbar(self.master, orient=VERTICAL)
    self.lstbox = Listbox(self.master, exportselection=0, yscrollcommand=self.scrollbar.set, font=("Helvetica, 16"), bg="black", fg='purple')
    self.scrollbar.grid(row=1, column=10, rowspan=9, padx=(0,0), pady=(10,0), sticky=N+E+S)
    self.lstbox.grid(row=1, column=4, rowspan=9, columnspan=6, padx=(30,0), pady=(10,0), sticky=N+S+E+W)
    self.lstbox.bind('<<ListboxSelect>>', lambda event: Stu_Track_func.onSelect(self, event))

    # Defining the buttons
    self.btn_submit = tk.Button(self.master, width=12, height=2, text='Submit', command=lambda: Stu_Track_func.onSubmit(self))
    self.btn_submit.grid(row=10, column=3, padx=(30,0), pady=(30,0), sticky=W)
    self.btn_delete = tk.Button(self.master, width=12, height=2, text='Delete', command=lambda: Stu_Track_func.onDelete(self))
    self.btn_delete.grid(row=10, column=4, padx=(30,0), pady=(30,0), sticky=W)

    Stu_Track_func.create_db(self)
    Stu_Track_func.onRefresh(self)



if __name__ == "__main__":
    pass