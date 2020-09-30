#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 07:53:25 2020

@author: niraj
"""

import sqlite3

conn = sqlite3.connect('Information.db')
c = conn.cursor()

user = "select *  from PatientInfo"
c.execute(user)
result = c.fetchall()
for value in result:
    print(value)