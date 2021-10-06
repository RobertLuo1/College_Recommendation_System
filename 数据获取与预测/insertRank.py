# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 16:59:33 2021

@author: dell
"""

import pandas as pd
import sqlite3

db_file = "db.sqlite3"
conn = sqlite3.connect(db_file)
cur = conn.cursor()

Lke = pd.read_csv("江苏省2020理科一分一段表.csv", encoding = 'UTF-8')
Wke = pd.read_csv("江苏省2020文科一分一段表.csv", encoding = 'UTF-8')

count = 0

for i in range(Lke.shape[0]):
    x = Lke.loc[i]
    year = 2020
    score = int(x[0])
    rank = int(x[1])
    provinceID = 4
    categoryID = 2
    t = [year,score,rank,categoryID,provinceID]
    t = tuple(t)
    # insert into + 表名 （列1，列2，...） values （？，？，？，）
    sql = 'insert into "Rankings"(year,score,rank,categoryID_id,provinceID_id)' \
          'values(?,?,?,?,?)'
    cur.execute(sql,t)
    conn.commit()
    count+=cur.rowcount
    
count = 0

for i in range(Wke.shape[0]):
    x = Wke.loc[i]
    year = 2020
    score = int(x[0])
    rank = int(x[1])
    provinceID = 4
    categoryID = 1
    t = [year,score,rank,categoryID,provinceID]
    t = tuple(t)
    # insert into + 表名 （列1，列2，...） values （？，？，？，）
    sql = 'insert into "Rankings"(year,score,rank,categoryID_id,provinceID_id)' \
          'values(?,?,?,?,?)'
    cur.execute(sql,t)
    conn.commit()
    count+=cur.rowcount
    
    
cur.close()
conn.close()




