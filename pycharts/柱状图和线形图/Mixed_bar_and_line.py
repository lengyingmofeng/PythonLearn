# @作者 : 叶枫
# @文件 : Mixed_bar_and_line.py 
# @时间 : 2020/12/19 20:02 
# @版本 ：1.0
# @功能描述:
from pyecharts.faker import Faker
from pyecharts.charts import Bar, Line
import pyecharts.options as opts
from pyecharts.globals import ThemeType
import random

bar = (
    Bar(init_opts=opts.InitOpts(theme='light', page_title="柱状图和线形图"))
    .add_xaxis(Faker.months)
    .add_yaxis(
        series_name="中国",
        y_axis=[random.randint(10000, 1000000) for i in range(13)],
        label_opts=opts.LabelOpts(is_show=True)
    )
        .add_yaxis(
        series_name="美国",
        y_axis=[random.randint(10000, 10000000) for i in range(13)],
        label_opts=opts.LabelOpts(is_show=True)
    )
        .add_yaxis(
        series_name="日本",
        y_axis=[random.randint(10000, 1000000) for i in range(13)],
        label_opts=opts.LabelOpts(is_show=True)
    )
        .set_global_opts(
        title_opts={'text': "柱状图", 'link': 'https://www.baidu.com'},
        xaxis_opts=opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=True)),
        yaxis_opts=opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=True))
    )
)
line = (
    Line()
        .add_xaxis(xaxis_data=Faker.months)
        .add_yaxis(
        series_name="感染数",
        yaxis_index=1,
        y_axis=Faker.values(),
        label_opts=opts.LabelOpts(is_show=True)
    )
)
bar.overlap(line).render("线形图和柱状图.html")
