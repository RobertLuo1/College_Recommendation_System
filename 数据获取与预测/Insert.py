# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 08:58:26 2021

@author: dell
"""

import pandas as pd
import sqlite3



def insert_Major(): 
    
    data2020 = pd.read_csv("2020数据.csv", encoding = 'UTF-8')
    db_file = "db.sqlite3"
    conn = sqlite3.connect(db_file)
    cur = conn.cursor()

    count = 0

    for i in range(data2020.shape[0]):
        x = data2020.loc[i]
        sql_c = ' select "Category"."categoryID" from "Category" where "Category"."categoryname" = '
        c_name = '\'' + x[1] + '\''
        sql_c += c_name
        cur.execute(sql_c)
        c_id = cur.fetchall()[0][0]
    
        sql_s = 'select "Colleges"."collegeID" from "Colleges" where "Colleges"."collegeName" = '
        s_name = '\'' + x[0] + '\''
        sql_s += s_name
        cur.execute(sql_s)
        s_id = cur.fetchall()[0][0]
    
        t=[x[2],2020,int(x[3]),c_id ,s_id ,4]
        t=tuple(t)
    
        sql = "insert into 'Majors'(majorName,year,minScore,categoryID_id,collegeID_id,provinceID_id)" \
              "values(?,?,?,?,?,?)"
        # insert into + 表名 （列1，列2，...） values （？，？，？，）
        cur.execute(sql, t)
        # 执行插入时显示的提交数据,否则无法同步到数据库！！！
        conn.commit()
        count+=cur.rowcount
    
    cur.close()
    conn.close()

    print(count)


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

for i in range(dataHot.shape[0]):
    x = dataHot.loc[i]
    job_main = x[1]
    sql_MJ_ID = 'select "MainJob"."mainJobID" from "MainJob" where "MainJob"."mainJobName" = '
    sql_MJ_ID+= '\''+ job_main +'\''
    cur.execute(sql_MJ_ID)
    main_job_id =cur.fetchall()[0][0]
    t = [x[2],x[3],main_job_id]
    t = tuple(t)
    sql_J ='insert into "Job"(jobName,salary,mainJobID_id)' \
            'values(?,?,?)' 
    cur.execute(sql_J,t)
    conn.commit()
    count+=cur.rowcount


count = 0
for i in range(dataLack.shape[0]):
    x = dataLack.loc[i]
    job_main = x[1]
    sql_MJ_ID = 'select "MainJob"."mainJobID" from "MainJob" where "MainJob"."mainJobName" = '
    sql_MJ_ID+= '\''+ job_main +'\''
    cur.execute(sql_MJ_ID)
    main_job_id =cur.fetchall()[0][0]
    t = [x[2],x[3],main_job_id]
    t = tuple(t)
    sql_J ='insert into "Job"(jobName,salary,mainJobID_id)' \
            'values(?,?,?)' 
    cur.execute(sql_J,t)
    conn.commit()
    count+=cur.rowcount


















db_file = "db.sqlite3"
conn = sqlite3.connect(db_file)
cur = conn.cursor()





cur.close()
conn.close()


