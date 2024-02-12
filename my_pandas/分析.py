# @作者 : 叶枫
# @文件 : 分析.py 
# @时间 : 2021/11/17 20:30
# @版本 ：1.0
# @功能描述:
import numpy as np
import pandas as pd
import pymysql
import MySQLdb
from pandas import DataFrame

# df = pd.read_csv('dogNames2.csv')
# my_sql = pymysql.connect(host='localhost', user='root', password='123456', database='blog')
# df1 = pd.read_sql("select * from t_link", con=my_sql)
# print(df)

# a = [1, 2, 3]
# data = pd.Series(a)
# print(data)
#
#
# data = pd.Series(a, index=["x", "y", "z"])
# b = {"name": "yefeng", "age": 18, "sex": "boy"}
# x = pd.Series(b)
# print(x)

# data = pd.read_csv('dogNames2.csv')
# print(data.to_string())

t = DataFrame(np.arange(12).reshape((3, 4)))
print(t)

data = [{"id": 1,  "name": "yefeng", "age": 20}]
s = DataFrame(data, index=list("ABCD"))
print(s)

collection = [['Google', 10], ['Arrays', 30], ['dicts', 20]]
da = DataFrame(collection, index=list(np.arange(1, 4)), columns=['Site', 'Age'])
print(da)
