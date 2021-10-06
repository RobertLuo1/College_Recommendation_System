# coding:utf-8
import csv
import torch
"""
build specific nested dict from csv files
outer_key:the outer level key of nested dict
lst_inner_value: a list of column name,for circumstance that the inner value of the same outer_key are not distinct
{outer_key:{key of lst_inner_value:[...value of lst_inner_value...]}}
"""

def buildDict(source_file,outer_key,lst_inner_value):
    new_dict = {}
    with open(source_file, 'rt')as csv_file:
        data = csv.DictReader(csv_file, delimiter=",")
        for row in data:
            new_dict.setdefault(row[outer_key], []).append({k: row[k] for k in lst_inner_value})
    return new_dict

outer_key = 'school'
lst_inner_value = ['major','rank','avg','cov']
new_dict_li = buildDict('江苏省理科预测数据.csv',outer_key,lst_inner_value)
print(new_dict_li)
new_dict_wen = buildDict('江苏省文科预测数据.csv',outer_key,lst_inner_value)

torch.save(new_dict_li,'江苏理科字典.pt')
torch.save(new_dict_wen,'江苏文科字典.pt')
