# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 18:02:48 2021

@author: dell
"""

import pandas as pd
import sqlite3

data2017 = pd.read_csv("2017数据.csv", encoding = 'UTF-8')
data2018 = pd.read_csv("2018数据.csv", encoding = 'UTF-8')
data2019 = pd.read_csv("2019数据.csv", encoding = 'UTF-8')
db_file = "db.sqlite3"
conn = sqlite3.connect(db_file)
cur = conn.cursor()

count2017 = 0
for i in range(data2017.shape[0]):
    x = data2017.loc[i]
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
    
    t=[x[2],2017,int(x[3]),c_id ,s_id ,4]
    t=tuple(t)
    
    sql = "insert into 'Majors'(majorName,year,minScore,categoryID_id,collegeID_id,provinceID_id)" \
        "values(?,?,?,?,?,?)"
    # insert into + 表名 （列1，列2，...） values （？，？，？，）
    cur.execute(sql, t)
    # 执行插入时显示的提交数据,否则无法同步到数据库！！！
    conn.commit()
    count2017 += cur.rowcount


count2018 = 0
for i in range(data2018.shape[0]):
    x = data2018.loc[i]
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
    
    t=[x[2],2018,int(x[3]),c_id ,s_id ,4]
    t=tuple(t)
    
    sql = "insert into 'Majors'(majorName,year,minScore,categoryID_id,collegeID_id,provinceID_id)" \
        "values(?,?,?,?,?,?)"
    # insert into + 表名 （列1，列2，...） values （？，？，？，）
    cur.execute(sql, t)
    # 执行插入时显示的提交数据,否则无法同步到数据库！！！
    conn.commit()
    count2018 += cur.rowcount


count2019 = 0
for i in range(data2019.shape[0]):
    x = data2019.loc[i]
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
    
    t=[x[2],2019,int(x[3]),c_id ,s_id ,4]
    t=tuple(t)
    
    sql = "insert into 'Majors'(majorName,year,minScore,categoryID_id,collegeID_id,provinceID_id)" \
        "values(?,?,?,?,?,?)"
    # insert into + 表名 （列1，列2，...） values （？，？，？，）
    cur.execute(sql, t)
    # 执行插入时显示的提交数据,否则无法同步到数据库！！！
    conn.commit()
    count2019 += cur.rowcount
    
cur.close()
conn.close()
