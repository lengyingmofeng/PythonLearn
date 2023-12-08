# @作者 : 叶枫
# @文件 : 绘制多个图形.py 
# @时间 : 2020-12-15 17:11 
# @版本 ：1.0
# @功能描述:
import pandas as pd
from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.charts import Scatter, Grid, Bar, Line
from pyecharts.globals import ThemeType

x_data = ["{}月".format(i) for i in range(1, 13)]
zengfaliang = [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3]
jiangshuiliang = [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3]
average_wendu = [2.0, 2.2, 3.3, 4.5, 6.3, 10.2, 20.3, 23.4, 23.0, 16.5, 12.0, 6.2]

# grid = Grid()
#
# bar = Bar()
# grid.theme = ThemeType.PURPLE_PASSION
# line = Line()
data1 = pd.read_csv("DXYArea.csv")
data1 = data1[data1['provinceName']=='中国']
data1['time'] = data1['updateTime'].str[:10]
list = data1.groupby(['time']).head(1)
x_data = list['time'].tolist()
average_wendu = list['province_confirmedCount'].tolist()

# bar.add_xaxis(x_data)
# bar.add_yaxis("蒸发量", zengfaliang)
# bar.add_yaxis("降水量", jiangshuiliang)
# bar.set_global_opts(title_opts=opts.TitleOpts("Grid-多Y轴展示"),
#                     tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"))  # 交叉指向工具
# bar.extend_axis(yaxis=opts.AxisOpts(type_="value",
#                                     name="温度",
#                                     min_=0,
#                                     max_=25,
#                                     position="right",
#                                     axislabel_opts=opts.LabelOpts(formatter="{value} °C"),
#                                     ))
# 在bar上增加Y轴，在line图上选择对应的轴向
# line.add_xaxis(x_data)
# line.add_yaxis("平均温度", average_wendu, yaxis_index=1)
# 把line添加到bar上
# bar.overlap(line)
# 这里如果不需要grid也可以，直接设置bar的格式，然后显示bar即可
# bar.render_notebook()
# grid.add(chart=line, grid_opts=opts.GridOpts(), is_control_axis_index=True)
# grid.render("绘制多个图形.html")
