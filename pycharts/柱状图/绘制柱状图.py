# @作者 : 叶枫
# @文件 : 绘制柱状图.py 
# @时间 : 2020/12/19 15:37 
# @版本 ：1.0
# @功能描述:
from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.charts import Scatter, Bar
from pyecharts.globals import ThemeType     # 导入主题包
Bar = (
    # theme-主题 - LIGHT明亮 page_title-网页标题 bg_color-背景颜色
    Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT, page_title="世界疫情表"))
    .add_xaxis(Faker.week)
    .add_yaxis("中国", Faker.values())
    .add_yaxis("美国", Faker.values(), stack="stack1")   # stack堆叠
    .add_yaxis("意大利", Faker.values())
    .add_yaxis("日本", Faker.values())
    .add_yaxis("英国", Faker.values(), stack="stack1")
    .set_global_opts(
        title_opts=opts.TitleOpts(title="柱状图", title_link="https://www.baidu.com"),
        xaxis_opts=opts.AxisOpts(name="x", splitline_opts=opts.SplitLineOpts(is_show=True),  # x分割线
                                 axislabel_opts=opts.LabelOpts(rotate=15)),  # x标题rotate-顺时针旋转15度
        yaxis_opts=opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=True)),       # y分割线
    )
    .render("柱状图.html")
)
