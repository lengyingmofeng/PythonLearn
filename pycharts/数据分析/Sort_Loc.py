# @作者 : 叶枫
# @文件 : Sort_Loc.py 
# @时间 : 2020/12/22 10:35 
# @版本 ：1.0
# @功能描述:
import re

import pandas as pd
import pyecharts.options as opts
import csv

from pyecharts.charts import Map

list_data1 = pd.read_csv('../DXYArea.csv')
china = list_data1.loc[list_data1['countryName'] == '中国']
china = china.loc[china.provinceName != '中国']
china = china.groupby('provinceName').head(1)
Data = []
for i in range(len(china)):
    num = china.iloc[i]['province_confirmedCount'] - (china.iloc[i]['province_curedCount'] + china.iloc[i]['province_deadCount'])
    province = re.sub("[省市维吾尔自治区回族自治区壮族]", "", china.iloc[i]['provinceName'])
    Data.append([province, int(num)])
print(Data)
map = (
    Map()
    .add(series_name='确诊病例', data_pair=Data)
    .set_global_opts(
        title_opts=opts.TitleOpts(title="中国地图", subtitle='现有疫情'),
        visualmap_opts=opts.VisualMapOpts(max_=0, is_piecewise=True, pieces=[
            {'max': 9, 'min': 0, 'label': '0-9', 'color': "pink"},
            {'max': 90, 'min': 10, 'label': '10-999', 'color': "skyblue"},
            {'max': 999, 'min': 100, 'label': '1000-9999', 'color': "yellow"},
            {'max': 9999, 'min': 1000, 'label': '10000-99999', 'color': "pink"},
            {'max': 99999, 'min': 10000, 'label': '100000-99999', 'color': "red"}
        ]),
    )
    .render("new_china.html")
)