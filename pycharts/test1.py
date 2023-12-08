# @作者 : 叶枫
# @文件 : test1.py
# @时间 : 2020/12/21 15:50
# @版本 ：1.0
# @功能描述:

import pandas as pd
from My_matplotlibs.ticker import MultipleLocator
from pyecharts import options as opts
from pyecharts.charts import Scatter, Grid, Bar, Line
from pyecharts.globals import ThemeType
# from
import My_matplotlibs.pyplot as plt
import time

start_times = time.time()
grid = Grid()
grid.theme = ThemeType.PURPLE_PASSION
line = Line()
Conner_data = pd.read_csv("DXYArea.csv")
data1 = Conner_data.loc[(Conner_data['countryName'] == '中国') & (Conner_data['provinceName'] == '中国'), ['provinceName',
                                                                                                       'province_confirmedCount',
                                                                                                       'updateTime']]
data1['time'] = data1['updateTime'].apply(lambda x: (x.split(" "))[0])
list_data1 = data1.groupby(['time']).head(1)
x_data  = list_data1['time'].sort_values(ascending=True).tolist()
China_data = []
for i in range(len(x_data)):
    if i == len(x_data) - 1:
        break
    else:
        num = data1.loc[data1['updateTime'].str.contains(x_data[i + 1]), ['province_confirmedCount']].iloc[0] - \
              data1.loc[data1['updateTime'].str.contains(x_data[i]), ['province_confirmedCount']].iloc[0]
        China_data.append(abs(int(num)))
print(China_data)
Abroad_list = Conner_data.loc[
    Conner_data['countryName'] != "中国", ['provinceName', 'province_confirmedCount', 'updateTime']]
Abroad = []
end_time = time.time() - start_times
print(end_time)
for i in range(len(x_data)):
    if i == len(x_data) - 1:
        break
    else:
        num = Abroad_list.loc[
            Abroad_list['updateTime'].str.contains(x_data[i + 1], ['province_confirmedCount', 'provinceName'])]
        head_num = num.groupby('provinceName')['province_confirmedCount'].head(1).sum()
        a = Abroad_list.loc[
            Abroad_list['updateTime'].str.contains(x_data[i]), ['province_confirmedCount', 'provinceName']]
        b = a.groupby('provinceName')['province_confirmedCount'].head(1).sum()
        num = int(head_num - b)
        Abroad.append(abs(num))

del (x_data[0])
print(Abroad)
end_time = time.time() - start_times
print(end_time)

# 使用pandas内置matplotlib绘图
plt.plot(x_data, China_data, color="r")
plt.plot(x_data, Abroad, color="b")
plt.xticks(rotation=45)
x_major_locator = MultipleLocator(19)
ax = plt.gca()
ax.xaxis.set_major_locator(x_major_locator)
plt.show()

# 导入matplotlib库绘图
# plt.plot(date,China_data,color="r")
# plt.plot(date,all_Data,color="b")
# plt.xticks(rotation=45)
# x_major_locator=MultipleLocator(19)
# ax=plt.gca()
# ax.xaxis.set_major_locator(x_major_locator)
# plt.show()

# average_wendu = list['province_confirmedCount'].tolist()
# # 在bar上增加Y轴，在line图上选择对应的轴向
# line.add_xaxis(x_data)
# line.add_yaxis("平均温度", average_wendu, yaxis_index=1)
# # 把line添加到bar上
# grid.add(chart=line, grid_opts=opts.GridOpts(), is_control_axis_index=True)
# grid.render("绘制多个图形1.html")
