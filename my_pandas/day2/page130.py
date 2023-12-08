# # @作者 : 叶枫
# # @文件 : page130.py
# # @时间 : 2021/11/26 9:43
# # @版本 ：1.0
# # @功能描述:
# import pandas as pd
# from matplotlib import pyplot as plt
# from matplotlib.font_manager import FontProperties
#
# font = FontProperties(fname=r"c:\windows\fonts\STSONG.TTF", size=10)
# df = pd.read_csv("starbucks_store_worldwide.csv")
# print(df)
# # print(df.info())
# df = df[df["Country"] == "CN"]
# datal = df.groupby("City").count()["Brand"].sort_values(ascending=False)[:10]
#
# print(datal)
# _x = datal.index
# _y = datal.values
# print(_x)
# plt.figure(figsize=(15, 10), dpi=80)
# plt.bar(_x, _y, width=0.4)
# plt.xticks(range(len(_x)), _x, fontproperties=font)
# plt.show()



# @作者 : 叶枫
# @文件 : 数据分析.py
# @时间 : 2021/11/27 10:17
# @版本 ：1.0
# @功能描述
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties

font = FontProperties(fname=r"c:\windows\fonts\STSONG.TTF", size=10)
df = pd.read_csv('huashi.csv')

df['likeNum'] = [int(float(str(i).split('w')[0])*10000) if str(i).endswith('w') else int(i) for i in df['likeNum']]
df.set_index("title", )
# df = df.sort_values(['likeNum'], ascending=False)['likeNum'][:10]
#
# _x = df.index
# _y = df.values
# print(_x)
# print(_y)
#
# plt.figure(figsize=(15, 10), dpi=80)
# #
# plt.bar(_x, _y, width=0.5, color='#458994')
# plt.xticks(range(len(_x)), _x, fontproperties=font, rotation=90)
# plt.show()

