from pyecharts.charts import Bar
from pyecharts import options as opts
from pyecharts.globals import ThemeType

bar = (
    Bar(
        # 配置初始化
        init_opts=opts.InitOpts(
            # 设置网页标题
            page_title="叶枫",
            # 图表主题
            theme=ThemeType.LIGHT,
        )
    )
    .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子", "爱心", "德玛", "赵信", "皇子", "加里奥"])
    .add_yaxis("A", [5, 10, 20, 13, 8, 9, 10, 12, 20, 16, 12], stack="stack1")
    .add_yaxis("D", [5, 3, 10, 13, 8, 9, 10, 11, 12, 15, 17], stack="stack1")
    .set_global_opts()
)

bar.render()
