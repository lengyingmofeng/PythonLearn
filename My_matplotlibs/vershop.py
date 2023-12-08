# @作者 : 叶枫
# @文件 : vershop.py 
# @时间 : 2021/11/22 21:44
# @版本 ：1.0
# @功能描述:

import pandas as pd

df = pd.read_csv('property-data.csv')
print(df, '\n')

# 查看前五行数据
print(df.head(), '\n')

# 查看后五行数据
print(df.tail(), '\n')

# # 移除指定列有空值的行
# df.dropna(subset=['ST_NUM', 'PID'], inplace=True)
# print(df, '\n')
#
# df.dropna(inplace=True)
# print(df)

# 把所有为N/A的值复制为0
df.fillna(0, inplace=True)
print(df)

x = df['ST_NUM'].mode()
print(x)