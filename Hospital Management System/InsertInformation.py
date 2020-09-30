#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 12:43:21 2020

@author: niraj
"""
import sqlite3
from tkinter import* 

conn = sqlite3.connect('PatientInfomation.db')
c = conn.cursor()

class InsertInformation:
    def __init__(self, master):
        self.master = master
        self.name = StringVar()
        self.contact = IntVar()
        self.address = StringVar()
        self.gender = BooleanVar()
        self.profile = StringVar()
        
        title = Label(master, text="Hospital Entry Panel", font=("times new roman", 18, "bold"), bg="blue", fg="white",
                       relief=GROOVE)
        title.place(x=2, y=0, relwidth=1)
        


        Data_Frame = Frame(master, bg="white")
        Data_Frame.place(x=20, y=100)

        
        fullname = Label(Data_Frame, text="Fullname", compound=LEFT, font=("times new roman", 12), bg="white")
        fullname.grid(row=0, column=0, padx=40, pady=0)
        enter_fullname = Entry(Data_Frame, bd=2, width=15, textvariable=self.name, relief=GROOVE, font=("", 12))
        enter_fullname.grid(row=0, column=1, padx=10)
        
        address = Label(Data_Frame, text="Address", compound=LEFT, font=("times new roman", 12), bg="white")
        address.grid(row=1, column=0, padx=20, pady=0)
        enter_address = Entry(Data_Frame, bd=2, width=15, textvariable=self.address, relief=GROOVE, font=("", 12))
        enter_address.grid(row=1, column=1, padx=10)
        
        contact = Label(Data_Frame, text="Contact", compound=LEFT, font=("times new roman", 12), bg="white")
        contact.grid(row=2, column=0, padx=20, pady=0)
        enter_contact = Entry(Data_Frame, bd=2, width=15, textvariable=self.contact, relief=GROOVE, font=("", 12))
        enter_contact.grid(row=2, column=1, padx=10)
        
        gender = Label(Data_Frame, text="Gender", compound=LEFT, font=("times new roman", 12), bg="white")
        gender.grid(row=3, column=0, padx=20, pady=0)
        male = Radiobutton(root, text='Male',bg="white").place(x=180,y=185)
        female = Radiobutton(root, text='Female',bg = "white").place(x=250,y=185)

        btn_submit = Button(master, text="Submit", width=8, font=("times new roman", 14, "bold"),
                         bg="#0dc1a6", fg="green", bd=4, command=None)
        btn_submit.place(x=180,y=250)
        
        def infromation_insert(self):
            pass
        


root=Tk()
root.title('Hospital Information Management')
root.geometry('450x450')
InsertInformation(root)
root.configure(bg="white")
root.mainloop()



