from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from . import models
import json
import os
import sqlite3 as db
import torch
import math

# Create your views here.

province = ['','河南省','天津市','海南省','江苏省','陕西省','青海省','澳门','香港','上海市','山西省','江西省','黑龙江省','浙江省','贵州省','西藏自治区','山东省','河北省','辽宁省','福建省','新疆维吾尔自治区','湖北省','湖南省','吉林省','广东省','北京市','台湾省','重庆市','安徽省','广西壮族自治区','甘肃省','宁夏回族自治区','云南省','四川省','内蒙古自治区']
category = ['','文科','理科','综合']

def find(request):
    """
    用于测试数据库相关数据，用来操作数据库
    :param request:
    :return:
    """
    # cmd ='select c.collegeName, m.year year, m.majorName major_name, m.minScore min_score from Colleges c left join Majors m on m.collegeID_id in (select c.collegeID from Colleges c left join Provinces p on c.provinceID_id=p.ProvinceID where p.provinceID={}) order by m.year,m.minScore'.format(province.index('江苏省'))
    # cmd = 'select p.provinceName,c.collegeName,m.categoryID_id category_id,m.year year, m.majorName major_name, m.minScore min_score,r.rank rank from Majors m left join Colleges c on m.collegeID_id = c.collegeID left join Rankings r on r.categoryID_id=m.categoryID_id AND m.minScore=r.score AND r.year=m.year left join Provinces p on m.provinceID_id=p.provinceID AND c.provinceID_id=1 AND r.provinceID_id=p.provinceID where p.provinceID={} order by c.collegeName,m.year,m.minScore'.format(province.index('江苏省'))
    # cmd = 'select p.provinceName,c.collegeName,m.categoryID_id category_id,m.year year, m.majorName major_name, m.minScore min_score,r.rank rank from Majors m left join Colleges c on m.collegeID_id = c.collegeID left join Rankings r on r.categoryID_id=m.categoryID_id AND m.minScore=r.score AND r.year=m.year left join Provinces p on m.provinceID_id=p.provinceID AND c.provinceID_id=34 AND r.provinceID_id=p.provinceID where p.provinceID={} order by c.collegeName,m.year,m.minScore'.format(province.index('江苏省'))
    # cmd = "select p.provinceName,c.collegeName,m.categoryID_id category_id,m.year year, m.majorName major_name, m.minScore min_score,r.rank rank from Majors m left join Colleges c on m.collegeID_id = c.collegeID AND c.collegeName='东南大学' left join Rankings r on r.categoryID_id=m.categoryID_id AND m.minScore=r.score AND r.year=m.year left join Provinces p on m.provinceID_id=p.provinceID AND c.provinceID_id=4 AND r.provinceID_id=p.provinceID where p.provinceID={} order by c.collegeName,m.year,m.minScore".format(province.index('江苏省'))
    # data = readDB(cmd)
    # print(data)
    # cmd1 ='select c.collegeName from Colleges c left join Provinces p on c.provinceID_id=p.ProvinceID where p.provinceID=34'
    # cmd1 = "select c.collegeID ,c.collegeName from Colleges c where c.collegeName='东南大学'"
    # data1 = readDB(cmd1)
    # data = models.Provinces.objects.get(provinceID=4)
    # print(data)
    # print(data1)
    return HttpResponse('ok')


def cal_distance(cur,des):
    '''辅助函数，用于计算经纬度'''
    distance = (cur['lng']-des['lng'])**2+(cur['lat']-des['lat'])**2
    return distance

def cal_possibility(rank,predict_rank,covariance):
    """
    根据输入的排名确定推荐概率
    :param rank: 用户输入的排名
    :param predict_rank: 预测排名
    :param covariance:
    :return: 用户上这所学校的概率
    """
    deNum1 = deNum2 = 1
    if rank > 0 and rank < 10000:
        deNum1 = 700
        deNum2 = 500
    elif  rank >= 10000:
        deNum1 = 1400
        deNum2 = 1000
    x = (predict_rank - rank)
    possibility =1
    if x > 0:
        possibility = math.exp(-((x/deNum1) **3) / 2)
    else:
        possibility =math.exp(-((x/deNum2)**2)/2)
    return possibility


def query(request):
    """
    响应前端返回的数据并进行相应的推荐
    :param request:
    :return:
    """
    content = {}
    if request.method=='POST':
        datatype = json.loads(request.body.decode('utf-8')) #得到前端返回的数据
        province_all = datatype['all']
        current_loc = datatype['currentLocation']  # 得到当前的省份，以这份省份为基准点算出经纬度
        if province_all == 'true': #如果判断是全国的话，就是会直接将全国的数据返回
            provinces_loc = province #
            provinces_loc_sorted = province
        else:
            provinces_loc = datatype['regions']  # 得到所需要的大学
            distance = []
            for i in range(len(provinces_loc)):
                distance.append(cal_distance(current_loc, provinces_loc[i]))
            provinces_loc_sorted = [x['pos'] for y, x in sorted(zip(distance, provinces_loc))]  # 排序后的省份，按照距离来进行排序
        colleges = []
        rank = (datatype['rank']) #获得排名
        category = datatype['category'] #获得类别
        if len(rank) == 0  or len(category) == 0 or len(provinces_loc) == 0 :#如果有一个是空则返回500状态码
            return JsonResponse({
                'status_code':500
            })
        else:
            rank = float(rank)#将rank变成float型来方便判断
        temp=[]
        data={}
        col_majors = {}
        if category=='理科': #判断是否为理科
            pdir = os.path.dirname(os.getcwd())  # 获取父目录
            file = os.path.join(pdir, 'python14\江苏理科字典.pt')
            predicted_data = torch.load(file) #导入理科的预测的排名
            for province_loc in provinces_loc_sorted:
                colleges_carrier = models.Colleges.objects.filter(provinceID=province.index(province_loc))#找到学校
                for college in colleges_carrier:
                    major_carrier = models.Majors.objects.filter(provinceID=4,collegeID=college.collegeID, categoryID=2)#找到专业
                    if len(major_carrier)!= 0:
                        majors_ranks = predicted_data[college.collegeName]#从预测数据中找到rank
                        for major_rank in majors_ranks:
                            possibility = cal_possibility(float(rank), float(major_rank['rank']),
                                                          float(major_rank['cov']))  # 计算相应的概率

                            if possibility>=0.2:#设置了一个推荐的阈值来控制推荐数量
                                data['major'] = major_rank['major']
                                data['rank'] = major_rank['rank']
                                data['possibility'] = round(possibility*5,3)
                                temp.append(data.copy())
                    if len(temp) !=0:#如果不为空则可以代表有推荐的学校和专业
                        col_majors[college.collegeName]=temp[:]
                        colleges.append(college.collegeName)
                        temp.clear()

        if category == '文科':
            pdir = os.path.dirname(os.getcwd())  # 获取父目录
            file = os.path.join(pdir, 'python14\江苏文科字典.pt')
            predicted_data = torch.load(file)
            for province_loc in provinces_loc_sorted:
                colleges_carrier = models.Colleges.objects.filter(provinceID=province.index(province_loc))
                for college in colleges_carrier:
                    major_carrier = models.Majors.objects.filter(provinceID=4,collegeID=college.collegeID,categoryID=1)
                    if len(major_carrier)!=0:
                        majors_ranks = predicted_data[college.collegeName]
                        for major_rank in majors_ranks:
                            possibility = cal_possibility(float(rank), float(major_rank['rank']),
                                                          float(major_rank['cov']))
                            if possibility>=0.2:
                                data['major'] = major_rank['major']
                                data['rank'] = major_rank['rank']
                                data['possibility'] = round(possibility*5,3)
                                temp.append(data.copy())
                    if len(temp) != 0:
                        col_majors[college.collegeName] = temp[:]
                        colleges.append(college.collegeName)
                        temp.clear()

        content={
            'colleges':colleges,
            'status_code':200,
            'col_majors':col_majors
        }
        return JsonResponse(content)

def readDB(exeCMD):
    '''数据库查询标准函数'''
    pdir = os.path.dirname(os.getcwd())  # 获取父目录
    sql_file = os.path.join(pdir, 'python14\db.sqlite3')  # 获取excel文件路径
    print(sql_file)
    try:
        conn = db.connect(sql_file) #该 API 打开一个到 SQLite 数据库文件 database 的链接，如果数据库成功打开，则返回一个连接对象
        c = conn.cursor()           #该例程创建一个 cursor，将在 Python 数据库编程中用到。
        cursor = c.execute(exeCMD)  #该例程执行一个 SQL 语句
        rows = cursor.fetchall()    #该例程获取查询结果集中所有（剩余）的行，返回一个列表。当没有可用的行时，则返回一个空的列表。
        return rows                 #输出查询结果
    except Exception as e:
        print(e)
        print('查询数据失败')
    finally:
        conn.close()


def queryCollege(request):
    '''对接前端地图查询学校功能，返回一个省份查询的学校'''
    if request.method == 'POST':
        datatype = json.loads(request.body.decode('utf-8'))
        province_ = datatype['region']
        college = []
        colleges = models.Colleges.objects.filter(provinceID=province.index(province_))
        for college_ in colleges:
            college.append(college_.collegeName)
        content = {
            'content':college,
            'status':200 #返回200表示可以访问
        }
        return JsonResponse(content)


def result(request):
    '''
    对接前端的响应接口，用于前端的985，211，双一流，的筛选
    :param request:
    :return:
    '''
    if request.method=='POST':
        data = json.loads(request.body.decode('utf-8'))
        flag = data['flag']
        collegeName = data['colleges']
        temp=[]
        content={}
        if flag=='985': #如果前端返回回来是985进行判断
            for collegeName_ in collegeName:
                college = models.Colleges.objects.filter(project985=True,collegeName=collegeName_)
                # print(college)
                if len(college) != 0:
                    temp.append(collegeName_)
        if flag=='211':#如果前端返回回来211
            for collegeName_ in collegeName:
                college = models.Colleges.objects.filter(project211=True, collegeName=collegeName_)
                if len(college) != 0:
                    temp.append(collegeName_)
        if flag=='双一流':
            for collegeName_ in collegeName:
                college = models.Colleges.objects.filter(top=True, collegeName=collegeName_)
                if len(college) != 0:
                    temp.append(collegeName_)
        if flag=='全部':
            temp=collegeName
        content={
            'colleges':temp,
            'status_code':200
        }
        return JsonResponse(content)

def collegeRank(request):
    if request.method=='GET':
        collegeRank = [{'id':i,'img_url': "http://10.208.82.71:5000/static/collegeRank_"+str(i)+".png"} for i in range(1,11)]#发送给前端数据
        content = {
            'collegeRank':collegeRank,
            'status_code':200
        }
        return JsonResponse(content)

def Jobs(request):
    """
    用于找到对应的热门职业以及对应的需求职业
    :param request:
    :return:相应的职业的数据结构
    """
    if request.method=='GET':
        Jobs = {}
        hotJobs = []
        lackJobs = []
        hot_temp = {}
        lack_temp ={}
        hot_mainJobs = models.MainJob.objects.filter(mainJobCategory=1)
        for hot_mainJob in hot_mainJobs:
            hot_temp['大职业'] = hot_mainJob.mainJobName
            hot_jobs = models.Job.objects.filter(mainJobID=hot_mainJob)
            hot_temp['subjobs'] = [{'子职业':hot_job.jobName,'薪资':hot_job.salary}  for hot_job in hot_jobs]
            hotJobs.append(hot_temp.copy())
            hot_temp.clear()
        Jobs['热门职业'] = hotJobs
        lack_mainJobs = models.MainJob.objects.filter(mainJobCategory=2)
        for lack_mainJob in lack_mainJobs:
            lack_temp['大职业'] = lack_mainJob.mainJobName
            lack_jobs = models.Job.objects.filter(mainJobID=lack_mainJob)
            lack_temp['subjobs'] = [{'子职业': lack_job.jobName, '薪资': lack_job.salary} for lack_job in lack_jobs]
            lackJobs.append(lack_temp.copy())
            lack_temp.clear()
        Jobs['稀缺职业'] = lackJobs
        content = {
            'Jobs':Jobs,
            'status_code':200
        }
        return JsonResponse(content)



