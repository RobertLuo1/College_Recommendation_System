# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 16:56:59 2021

@author: dell
"""

import pandas as pd
import sqlite3

# 与db.sqlite3在同一目录下时

def insert_MainJob():
    dataHot = pd.read_csv("jobhot.csv", encoding = 'UTF-8')
    dataLack = pd.read_csv("joblack.csv", encoding = 'UTF-8')
    db_file = "db.sqlite3"
    conn = sqlite3.connect(db_file)
    cur = conn.cursor()
    count = 0

    hotJob = []
    lackJob = []

    for i in range(dataHot.shape[0]):
        if dataHot.loc[i][1] not in hotJob:
            hotJob.append(dataHot.loc[i][1])
    
    for i in range(dataLack.shape[0]):
        if dataLack.loc[i][1] not in lackJob:
            lackJob.append(dataLack.loc[i][1])

    for i in range(len(hotJob)):
    
        sql_MJ ='insert into "Mainjob"(mainJobName,mainJobCategory)' \
                'values(?,?)'    
        x = hotJob[i]
        t = [x,1]
        t = tuple(t)
        cur.execute(sql_MJ,t)
        conn.commit()
        count+=cur.rowcount
   
   
    count = 0   
    for i in range(len(lackJob)):
    
        sql_MJ ='insert into "Mainjob"(mainJobName,mainJobCategory)' \
                'values(?,?)'    
        x = lackJob[i]
        t = [x,2]
        t=tuple(t)
        cur.execute(sql_MJ,t)
        conn.commit()
        count+=cur.rowcount

    cur.close()
    conn.close()
    
    
dataHot = pd.read_csv("jobhot.csv", encoding = 'UTF-8')
dataLack = pd.read_csv("joblack.csv", encoding = 'UTF-8')
db_file = "db.sqlite3"
conn = sqlite3.connect(db_file)
cur = conn.cursor()
count = 0

# for i in range(dataHot.shape[0]):
#     x = dataHot.loc[i]
#     M_job = x[1]
#     sql1 = 'select "MainJob"."mainJobID" from "MainJob" where ("MainJob"."mainJobName" = '
#     sql1 += '\''+ x[1] +'\' ' + 'and '+ '"MainJob"."mainJobCategory" = 1)' 
#     cur.execute(sql1)
#     M_id = cur.fetchall()[0][0]
#     salary = x[3]
#     job_name = x[2]
    
#     sql2 = 'insert into "Job"(jobName,salary,MainJobID_id) values(?,?,?)'
#     t = [job_name,salary,M_id]
#     t = tuple(t)
#     cur.execute(sql2,t)
#     conn.commit()
#     count+=cur.rowcount
    
for i in range(dataLack.shape[0]):
    x = dataLack.loc[i]
    M_job = x[1]
    sql1 = 'select "MainJob"."mainJobID" from "MainJob" where ("MainJob"."mainJobName" = '
    sql1 += '\''+ x[1] +'\' ' + 'and '+ '"MainJob"."mainJobCategory" = 2)' 
    cur.execute(sql1)
    M_id = cur.fetchall()[0][0]
    salary = x[3]
    job_name = x[2]
    
    sql2 = 'insert into "Job"(jobName,salary,MainJobID_id) values(?,?,?)'
    t = [job_name,salary,M_id]
    t = tuple(t)
    cur.execute(sql2,t)
    conn.commit()
    count+=cur.rowcount  
    
    