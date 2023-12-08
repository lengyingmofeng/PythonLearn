# @作者 : 叶枫
# @文件 : 使用 matplotlib画出感染数前十的国家.py
# @时间 : 2020/12/11 14:37 
# @版本 ：1.0
# @功能描述: 找出疫情感染数前十的国家
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Bar
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']
import matplotlib.pyplot as plt
db = pd.read_csv('DXYArea.csv')
abroad = list(set(db['countryName']))
last_day = '2020-11-11'
to_day = '2020-11-12'
count_value = []  # 用来存储国家名字
values = []       # 用来存储感染数
for item in abroad:
    countName = db[db['countryName'] == item]  # 寻找国家名等于i的信息
    a = countName[countName['updateTime'].str.contains(last_day)]
    b = countName[countName['updateTime'].str.contains(to_day)]
    if len(a) > 0 and len(b) > 0:
        count_value.append(item)
        values.append(max(b['province_confirmedCount']) - max(a['province_confirmedCount']))
    else:
        count_value.append(item)
        values.append(0)
c = pd.DataFrame()
c['countryName'] = count_value
c['values'] = values
c = c.sort_values(by='values', ascending=False)
c1 = c.head(10)
name = c1['countryName'].values.tolist()
value = c1['values'].values.tolist()
color = []
for i in value:
    if i > 100000:
        color.append('r')
    else:
        color.append('g')
plt.bar(name, value, width=0.3, color=color)
plt.title("时间感染数top10国家")   # 标题
plt.xticks(name, rotation=45)     #
plt.grid(axis='y', linestyle='--')
plt.grid(axis='x', linestyle='--')
plt.show()

# # 使用pyecharts画出
# bar = (
#     Bar()
#     .add_xaxis(name)
#     .add_yaxis('感染数', value)
#     .set_global_opts(title_opts=opts.TitleOpts(title='新增确诊国家top10'),
#                      xaxis_opts=opts.AxisOpts(axislabel_opts={"rotate": 45}, ))
#     .render('top10.html')
# )


# # 国外 abroad = db.loc[db['countryName'] != '中国', ['countryName', 'province_confirmedCount',
# 'province_suspectedCount', 'province_curedCount', 'province_deadCount']] print(abroad) # 国内 domestic = db.loc[db[
# 'countryName'] == '中国', ['provinceName', 'province_confirmedCount', 'province_suspectedCount',
# 'province_curedCount', 'province_deadCount']] print(domestic)


# bar = (
#     Bar()
#     .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
#     .add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
#     .c(title_opts=opts.TitleOpts(title="飞龙超市销售", subtitle="我是副标题"))
#     .set_series_opts(
#         label_opts=opts.LabelOpts(is_show=True),
#         # 这里需要注意data是一个系列，就算只有一个也是必须做list处理
#         markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max", name="max"), opts.MarkPointItem(name="min", type_="min")]))
# )
# bar.render_notebook()
# line = Line()
# line.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
# line.add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
# render 会生成本地 HTML 文件，默认会在当前目录生成 render.html 文件
# 也可以传入路径参数，如 bar.render("mycharts.html")
# bar.render()
