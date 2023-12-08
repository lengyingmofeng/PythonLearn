# @作者 : 叶枫
# @文件 : 国家10月份.py 
# @时间 : 2020/12/25 21:45 
# @版本 ：1.0
# @功能描述:
import csv
import pandas as pd
import numpy as np
db = pd.read_csv('DXYArea.csv')
db['updateTime'] = db['updateTime'].apply(lambda x: x[5:10])
chiame = db[db['provinceName'] == '中国'].drop_duplicates('updateTime', keep='first').reset_index(drop=True)
print(chiame['provinceName'])
config = np.array(chiame['province_confirmedCount'])[:-1] - np.array(chiame['province_confirmedCount'])[1:]
chiame = dict(pd.Series(config, index=chiame['updateTime'])[:-1])
arse = db[db['countryName'] != '中国'].copy()
arse = arse.drop_duplicates(['countryName', 'updateTime'], keep='first')
