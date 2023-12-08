# @作者 : 叶枫
# @文件 : Serie.py 
# @时间 : 2021/11/25 14:43
# @版本 ：1.0
# @功能描述:
import pandas as pd
import numpy as np

# s = pd.Series(5., index=['a', 'b', 'c', 'd'])
#
# df = pd.Series([1, 2, 3, 4, 5, 6, 7, 8], index=list('abcdefgh'))
# print(df[3:])
# print(df.mean())
#
# # 筛选大于平均值的值
# num = df[df > df.median()]
# print(num)
#
# # 指定索引的内容，括号的列表是索引
# print(df[[1, 2, 1]])
#
# # 同索引相加，无索引位用 NaN 补齐
# su = df + df
# print(su)
#
# # 同索引相乘
# sw = df * 3
# print(sw)
#
# print(30*"*")
# we = df[1:] + df[:-1]
# print(df[1:], df[:-1])
# print(we)


d = {'one': pd.Series([1., 2., 3.], index=['a', 'b', 'c']),
     'two': pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(d)
print(d)
print(df)

s = pd.DataFrame(d, index=['d', 'b', 'a'], columns=['two', 'three'])
print(s)

data = np.zeros((2,), dtype=[('A', 'i4'), ('B', 'f4'), ('C', 'a10')])
print(data)

data2 = [{'a': 1, 'b': 2}, {'b': 5, 'a': 10}]
df = pd.DataFrame(data2, index=list("ED"))
print(df)
print(df.values)
print(df.to_numpy())

# df.set_index
# df = pd.DataFrame()
#
# s1 = pd.Series(['a', 'b', 'c', 'd', 'e'])
# sw = pd.DataFrame(s1, index=list("abcd"), columns=["one"])
# print(sw)
#
# print()

df = pd.read_csv("team.xlsx")
print()