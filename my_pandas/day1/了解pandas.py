# @作者 : 叶枫
# @文件 : 了解pandas.py 
# @时间 : 2021/11/25 10:46
# @版本 ：1.0
# @功能描述:

import pandas as pd
import numpy as np

df = pd.read_excel('team.xlsx')
# 建立索引并生效
df.set_index('name', inplace=True)
# print(df)
# print(df['Q1'])
# print(df[['team', 'Q1']])
# print(df.loc[:, ['team', 'Q1']])
# print(df[df.index == 'Liver'])
# print(df.iloc[:10,:])
# print(df.loc['Ben', 'Q1':'Q4'])
# print(df.loc['Eorge':'Alexander', 'team':'Q4'])
# print(df[df.Q1 > 90])

# 组合条件
df_list = df[(df['Q1'] > 90) & (df['team'] == 'C')]
print(df_list)

# 多重筛选
df_loc = df[df['team'] == 'C'].loc[df.Q1 > 90]
print(df_loc)

# 默认是升序，设置成False为降序
df_sort = df.sort_values('Q1', ascending=False)
print(df_sort)

# team 升，Q1 降序
dfs = df.sort_values(['team', 'Q1'], ascending=[True, False])
print(dfs)

# 分组
dfs = df.groupby('team').sum()
print(dfs)
