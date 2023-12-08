# @作者 : 叶枫
# @文件 : 散点图.py 
# @时间 : 2020-12-15 16:38 
# @版本 ：1.0
# @功能描述:
from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.charts import Scatter
from pyecharts.globals import ThemeType
scatter = Scatter()
scatter.add_xaxis(Faker.choose())
scatter.add_yaxis("商家A", Faker.values())
# scatter.set_global_opts(title_opts=opts.TitleOpts(title="Scatter-基本示例"))
scatter.set_global_opts(
            title_opts=opts.TitleOpts(title="Scatter-显示分割线"),
            xaxis_opts=opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=True)),
            yaxis_opts=opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=True)),

        )
scatter.render("散点图.html")