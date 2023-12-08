# @作者 : 叶枫
# @文件 : movies.py 
# @时间 : 2021/11/24 14:46
# @版本 ：1.0
# @功能描述:
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

df = pd.read_csv('IMDB-Movie-Data.csv')
# print(df["Genre"])
# 统计分类的列表
temp_list = df["Genre"].str.split(",").tolist()
genre_list = list(set([i for j in temp_list for i in j]))

# 构造全为0的数组
zeros_df = pd.DataFrame(np.zeros((df.shape[0], len(genre_list))), columns=genre_list)
# print(zeros_df)

# 给每个电影出现分类的位置赋值1
for i in range(df.shape[0]):
    zeros_df.loc[i, temp_list[i]] = 1
# print(zeros_df)

# 统计每个分类的电影的数量
genre_count = zeros_df.sum(axis=0)
# print(genre_count)

# 排序
genre_count = genre_count.sort_values(ascending=False)
print(genre_count)
_x = genre_count.index
_y = genre_count.values
plt.figure(figsize=(20, 8), dpi=80)
plt.bar(_x, _y, width=0.4)
# plt.xticks(range(len(_x)), _x)
plt.show()