# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 17:16:19 2021

@author: dell
"""

import pandas as pd
import sqlite3

db_file = "db.sqlite3"
conn = sqlite3.connect(db_file)
cur = conn.cursor()

sql = 'SELECT "Majors"."id" FROM "Majors" WHERE ("Majors"."year" = 2017 OR "Majors"."year" = 2018 OR "Majors"."year" = 2019 OR "Majors"."year" = 2016)'
sql1 = sql = 'SELECT "Majors"."id" FROM "Majors" WHERE "Majors"."year" = 2015 '
cur.execute(sql1)
x = cur.fetchall()

count = 0
for i in x:
    sql_t = sql = 'delete from Majors where id=?'
    t = tuple(i)
    cur.execute(sql_t, t)
    count += cur.rowcount
    conn.commit()
    
cur.close()
conn.close()