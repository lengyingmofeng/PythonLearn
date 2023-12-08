# @作者 : 叶枫
# @文件 : test.py 
# @时间 : 2021/11/25 20:39
# @版本 ：1.0
# @功能描述:

import pandas as pd
import numpy as np
df = pd.read_excel('Books.xlsx', skiprows=3, usecols='C:F')

df = (
    df.assign(ID=range(1, 21))
    .assign(InStore=['Yes', 'No'] * 10)
    .assign(Date=pd.date_range('2021-11-25', periods=20, freq="MS"))
)
print(df)
df['Number'] = 100
print(df)
df = df.assign(ABC=100)
df['ABC'] = [[i for i in range(5)]] * 20
print(df)
df.pop('ABC')
print(df)

s1 = pd.Series(['a', 'b'])
s2 = pd.Series(['c', 'd'])
s3 = pd.concat([s1, s2])
s4 = pd.concat([s1, s2], ignore_index=True) # 索引重新编
print(s3)
print(s4)

s5 = pd.concat([s1, s2], keys=['s1', 's2'])
print(s5)