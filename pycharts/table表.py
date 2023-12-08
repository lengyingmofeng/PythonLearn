import pandas as pd
import numpy as np
import csv

from pyecharts.components import Table

db = pd.read_csv("DXYArea.csv")
test_china = db[['countryName', 'province_confirmedCount', 'province_suspectedCount', 'province_curedCount']]
test_china = test_china.groupby('countryName').head(1)
rows = []
for i in range(len(test_china)):
    rows.append(list(test_china.iloc[i]))
rows = sorted(rows, key=lambda x: x[1], reverse=True)[:10]

table = Table()
head = ['国家' , '新增', '疑似', '死亡']
table.add(head, rows)
table.set_global_opts(title_opts='基本')
table.render("前十表格.html")
