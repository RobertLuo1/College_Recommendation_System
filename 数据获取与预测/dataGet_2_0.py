# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 22:50:26 2021

@author: dell
"""

import pandas as pd
import sqlite3

def myFind(base, name, major):
    for j in range(len(base)):
        if base[j][0] == name and base[j][1] == major:
            return j
    return -1

# 补全数据
def fillData(base):
    c = 0
    for i in base:
        c += 1

        if i[2] != -1 and i[3] != -1 and i[4] != -1 and i[5]!= -1:
            continue

        fill = 0
        n = 0
        if i[2] != -1:
            fill += i[2]
            n += 1

        if i[3] != -1:
            fill += i[3]
            n += 1

        if i[4] != -1:
            fill += i[4]
            n += 1

        if i[5] != -1:
            fill += i[5]
            n += 1

        if n == 0:
            print(i, c)

        fill = fill / n

        if i[2] == -1:
            i[2] = fill

        if i[3] == -1:
            i[3] = fill

        if i[4] == -1:
            i[4] = fill
        
        if i[5] == -1:
            i[5] = fill     

    return base


# 匹配位次
def suit(score, rank_base):
    for i in rank_base:
        if score == i[0]:
            return i[1]
    t = sorted(rank_base)
    n = len(t)
    for i in range(n):
        if score < t[i][0]:
            if i == 0:
                return rank_base[i][1]
            return (t[i][1] + t[i - 1][1]) / 2
    return t[n - 1][1]


def trainData(aim_category="文科", aim_province="江苏"):
    aim_province = '\"' + aim_province + '\"'
    aim_category = '\"' + aim_category + '\"'

    # 连接数据库，数据库和该文件在同一目录下
    db_file = "db.sqlite3"
    conn = sqlite3.connect(db_file)
    cur = conn.cursor()



    sql1 = 'select "Provinces"."provinceID", "Provinces"."provinceName" from "Provinces" where "Provinces"."provinceName" = '
    sql1 += aim_province
    cur.execute(sql1)
    province_id = cur.fetchall()[0][0]

    sql2 = 'SELECT "Category"."categoryID", "Category"."categoryname" FROM "Category" WHERE "Category"."categoryname" = '
    sql2 += aim_category
    cur.execute(sql2)
    category_id = cur.fetchall()[0][0]

    sql2017 = 'SELECT "Majors"."id", "Majors"."collegeID_id", "Majors"."provinceID_id", "Majors"."categoryID_id", "Majors"."majorName", "Majors"."year", "Majors"."minScore", "Majors"."avgScore", "Majors"."maxScore", "Majors"."firstlevelIDs" FROM "Majors" WHERE ("Majors"."categoryID_id" = ' \
              + str(category_id) + ' AND "Majors"."provinceID_id" = ' + str(
        province_id) + ' AND "Majors"."year" = 2017)'
    cur.execute(sql2017)
    major2017 = cur.fetchall()


    sql2018 = 'SELECT "Majors"."id", "Majors"."collegeID_id", "Majors"."provinceID_id", "Majors"."categoryID_id", "Majors"."majorName", "Majors"."year", "Majors"."minScore", "Majors"."avgScore", "Majors"."maxScore", "Majors"."firstlevelIDs" FROM "Majors" WHERE ("Majors"."categoryID_id" = ' \
              + str(category_id) + ' AND "Majors"."provinceID_id" = ' + str(
        province_id) + ' AND "Majors"."year" = 2018)'
    cur.execute(sql2018)
    major2018 = cur.fetchall()


    sql2019 = 'SELECT "Majors"."id", "Majors"."collegeID_id", "Majors"."provinceID_id", "Majors"."categoryID_id", "Majors"."majorName", "Majors"."year", "Majors"."minScore", "Majors"."avgScore", "Majors"."maxScore", "Majors"."firstlevelIDs" FROM "Majors" WHERE ("Majors"."categoryID_id" = ' \
              + str(category_id) + ' AND "Majors"."provinceID_id" = ' + str(
        province_id) + ' AND "Majors"."year" = 2019)'
    cur.execute(sql2019)
    major2019 = cur.fetchall()


    sql2020 = 'SELECT "Majors"."id", "Majors"."collegeID_id", "Majors"."provinceID_id", "Majors"."categoryID_id", "Majors"."majorName", "Majors"."year", "Majors"."minScore", "Majors"."avgScore", "Majors"."maxScore", "Majors"."firstlevelIDs" FROM "Majors" WHERE ("Majors"."categoryID_id" = ' \
              + str(category_id) + ' AND "Majors"."provinceID_id" = ' + str(
        province_id) + ' AND "Majors"."year" = 2020)'
    cur.execute(sql2020)
    major2020 = cur.fetchall()





    sql_r2017 = 'SELECT "Rankings"."score", "Rankings"."rank" FROM "Rankings" WHERE ("Rankings"."provinceID_id" = ' \
                + str(province_id) + ' AND "Rankings"."year" = 2017 AND "Rankings"."categoryID_id" = ' + str(
        category_id) + ' )'
    cur.execute(sql_r2017)
    rank2017 = cur.fetchall()

    sql_r2018 = 'SELECT "Rankings"."score", "Rankings"."rank" FROM "Rankings" WHERE ("Rankings"."provinceID_id" = ' \
                + str(province_id) + ' AND "Rankings"."year" = 2018 AND "Rankings"."categoryID_id" = ' + str(
        category_id) + ' )'
    cur.execute(sql_r2018)
    rank2018 = cur.fetchall()

    sql_r2019 = 'SELECT "Rankings"."score", "Rankings"."rank" FROM "Rankings" WHERE ("Rankings"."provinceID_id" = ' \
                + str(province_id) + ' AND "Rankings"."year" = 2019 AND "Rankings"."categoryID_id" = ' + str(
        category_id) + ' )'
    cur.execute(sql_r2019)
    rank2019 = cur.fetchall()
    
    sql_r2020 = 'SELECT "Rankings"."score", "Rankings"."rank" FROM "Rankings" WHERE ("Rankings"."provinceID_id" = ' \
                + str(province_id) + ' AND "Rankings"."year" = 2020 AND "Rankings"."categoryID_id" = ' + str(
        category_id) + ' )'
    cur.execute(sql_r2020)
    rank2020 = cur.fetchall()
 
    
 

    mydata = []  # 学校 专业 17 18 19 20 分数
    myrank = []  # 位次版
    for i in major2017:
        c_id = i[1]
        sql_t = 'select "Colleges"."collegeName" from "Colleges" where "Colleges"."collegeID" =  '
        sql_t += str(c_id)
        cur.execute(sql_t)
        school = cur.fetchall()[0][0]
        data = [school, i[4], i[6], -1, -1,-1]
        rank_t = [school, i[4], suit(i[6], rank2017), -1, -1,-1]
        mydata.append(data)
        myrank.append(rank_t)
    

    for i in major2018:
        c_id = i[1]
        sql_t = 'select "Colleges"."collegeName" from "Colleges" where "Colleges"."collegeID" =  '
        sql_t += str(c_id)
        cur.execute(sql_t)
        school = cur.fetchall()[0][0]
        position = myFind(mydata, school, i[4])
        if position >= 0:
            mydata[position][3] = i[6]
            myrank[position][3] = suit(i[6], rank2018)
        else:
            data = [school, i[4], -1, i[6], -1,-1]
            mydata.append(data)
            rank_t = [school, i[4], -1, suit(i[6], rank2018), -1,-1]
            myrank.append(rank_t)


    for i in major2019:
        c_id = i[1]
        sql_t = 'select "Colleges"."collegeName" from "Colleges" where "Colleges"."collegeID" =  '
        sql_t += str(c_id)
        cur.execute(sql_t)
        school = cur.fetchall()[0][0]
        position = myFind(mydata, school, i[4])
        if position >= 0:
            mydata[position][4] = i[6]
            myrank[position][4] = suit(i[6], rank2019)
        else:
            data = [school, i[4], -1, -1, i[6],-1]
            mydata.append(data)
            rank_t = [school, i[4], -1, -1, suit(i[6], rank2019),-1]
            myrank.append(rank_t)
    
            
    for i in major2020:
        c_id = i[1]
        sql_t = 'select "Colleges"."collegeName" from "Colleges" where "Colleges"."collegeID" =  '
        sql_t += str(c_id)
        cur.execute(sql_t)
        school = cur.fetchall()[0][0]
        position = myFind(mydata, school, i[4])
        if position >= 0:
            mydata[position][4] = i[6]
            myrank[position][4] = suit(i[6], rank2020)
        else:
            data = [school, i[4], -1, -1, -1, i[6]]
            mydata.append(data)
            rank_t = [school, i[4], -1, -1, -1, suit(i[6], rank2020)]
            myrank.append(rank_t)


    
    mydata = fillData(mydata)
    myrank = fillData(myrank)

    cur.close()
    conn.close()
    # 分数为-1表示改年分数数据未知
    score = pd.DataFrame(mydata, columns=('学校', '专业', '2017分数', '2018分数', '2019分数','2020分数'))
    rank = pd.DataFrame(myrank, columns=('学校', '专业', '2017位次', '2018位次', '2019位次','2020位次'))
    return score, rank

if __name__ == "__main__":
    f1_s, f1_r = trainData(aim_category="理科")
    f2_s, f2_r = trainData(aim_category="文科")