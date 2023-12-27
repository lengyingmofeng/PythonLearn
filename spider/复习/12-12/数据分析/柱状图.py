# @作者 : 叶枫
# @文件 : 柱状图.py 
# @时间 : 2021/12/13 21:18
# @版本 ：1.0
# @功能描述:
import pandas as pd
from matplotlib import pyplot as plt
df = pd.read_excel('team.xlsx')
# print(df[:5])
# df[:5].plot.bar(x='name', y=["Q1", "Q2", "Q3", "Q4"], rot=0)
# plt.show()


# df["Q1"] = df["Q1"] - 70
# df.set_index('name', inplace=True)
# df[:10].plot.bar(rot=0)
# plt.show()


# df.set_index('name', inplace=True)
# df[5:10].plot.bar(rot=0, stacked=True)
# plt.show()


df.set_index('name', inplace=True)
df[5:10].plot.barh(rot=0, stacked=True)
df[:5].plot.bar(subplots=True, rot=0)
plt.xlabel("成绩单", fontproperties="SimHei")
plt.show()

