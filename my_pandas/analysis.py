# @作者 : 叶枫
# @文件 : analysis.py 
# @时间 : 2021/11/22 15:29
# @版本 ：1.0
# @功能描述:

import pandas as pd
from matplotlib.font_manager import FontProperties
from pandas import DataFrame
from matplotlib import pyplot as plt
from pyecharts.charts import Bar, Line
import pyecharts.options as opts
from pyecharts.globals import ThemeType

font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=14)  # 步骤二
df = pd.read_csv('my_dog.csv')
df.fillna(0, inplace=True)
for x in df.index:
    if df.loc[x, "姓名"] == "杨圣波" or df.loc[x, '姓名'] == "田思凯":
        df.loc[x, "语文"] = 0
        df.loc[x, "数学"] = 0
        df.loc[x, "英语"] = 0
name = df['姓名']
language = list(map(int, df['语文']))
math = list(map(int, df['数学']))
english = list(map(int, df['英语']))

# plt.figure(figsize=(10, 8), dpi=80)
# plt.bar(name, language, width=0.6, label="语文")
# plt.bar([i + 0.6 for i in range(len(name))], math, width=0.6, label="数学")
# plt.bar([i + 1.2 for i in range(len(name))], english, width=0.6, label="英语")
# plt.xticks([i + 0.3 for i in range(len(name))], name, fontproperties=font, rotation=45)
# plt.title(label="211班期末考试", fontproperties=font)
# plt.legend(prop=font)
# plt.show()

bar = (
    Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
    .add_xaxis([i for i in name])
    .add_yaxis("语文", language)
    .add_yaxis("数学", math)
    .add_yaxis("英语", english)
    .set_global_opts(
        title_opts=opts.TitleOpts()
    )
)
bar.render()