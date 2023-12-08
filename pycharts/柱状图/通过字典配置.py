# @作者 : 叶枫
# @文件 : 通过字典配置.py 
# @时间 : 2020/12/19 18:24 
# @版本 ：1.0
# @功能描述:
from pyecharts.charts import Bar
from pyecharts.faker import Faker
from pyecharts.globals import ThemeType

c = (
    Bar({"theme": ThemeType.MACARONS})
    .add_xaxis(Faker.choose())
    .add_yaxis("商家A", Faker.values())
    .add_yaxis("商家B", Faker.values())
    .set_global_opts(
        title_opts={"text": "Bar-通过 dict 进行配置", "subtext": "我也是通过 dict 进行配置的", "link": "https://www.baidu.com"},
    )
    .render("bar_base_dict_config.html")
)
