import re

import pandas as pd
from pyecharts.charts import Map
from pyecharts import options as opts

data = pd.read_csv('DXYArea.csv')
# 取出中国，省份不为中国的数据
china = data[(data['countryName'] == '中国') & (data['provinceName'] != '中国')].copy()
# 取出省份
provinceName = china['provinceName'].unique()
# 分组取出第一条数据
china = china.groupby('provinceName').head(1)
# 使用Serise对象去进行计算
confirm = china['province_confirmedCount'] - china['province_curedCount'] - china['province_deadCount']
# 重置索引，使用省份当做索引,并转化为字典类型,得到最终数据
confirm = dict(pd.Series(confirm.values, index=provinceName))
confirm = eval(re.sub('[省市壮族回族维吾尔自治区]', '', str(confirm)))
print(confirm)

c = (
    Map().add('疫情图', data_pair=list(confirm.items())[:], maptype='china')
        .set_global_opts(
        title_opts=opts.TitleOpts(title='中国新冠疫情图'),
        visualmap_opts=opts.VisualMapOpts(is_piecewise=True, pieces=[
            {'max': 10, 'label': '<10', 'color': 'green'},
            {'min': 10, 'max': 50, 'label': '10-50', 'color': 'grey'},
            {'min': 50, 'max': 100, 'label': '50-100', 'color': 'pink'},
            {'min': 100, 'max': 200, 'label': '100-200', 'color': 'red'},
            {'min': 300, 'label': '>300', 'color': 'orange'},
        ])).render('./1223中国疫情图.html')
)
