import numpy as np
import pandas as pd
import My_matplotlibs
import My_matplotlibs.pyplot as plt

data = pd.read_csv('DXYArea.csv')
print(data['updateTime'])
# 清洗时间
data['updateTime'] = data['updateTime'].apply(lambda x: x[5:10])
# 提取出省份为中国的数据并对时间进行去重,然后重置索引
china = data[data['provinceName'] == '中国'].drop_duplicates('updateTime', keep='first').reset_index(drop=True)
# 错位相减
confirm = np.array(china['province_confirmedCount'])[:-1] - np.array(china['province_confirmedCount'])[1:]
# # 先转化成Series对象再转化为字典
china = dict(pd.Series(confirm, index=china['updateTime'][:-1]))
# # china['7-10'] = 0
# # china['7-28'] = 0
# # 提取出非中国数据并copy
areas = data[data['countryName'] != '中国'].copy()
# 根据国家名称和时间去重
areas = areas.drop_duplicates(['countryName', 'updateTime'], keep='first')
# 提取出时间并去重
updateTime = areas['updateTime'].unique()
# 根据时间进行分组并聚合根据索引进行排序
areas = areas.groupby('updateTime').agg('sum').sort_index(ascending=False)
# 求出每日新增确诊的人数
confirm = abs(np.array(areas['province_confirmedCount'])[:-1] - np.array(areas['province_confirmedCount'])[1:])
# 先转化为Series类型排序再转化为字典
areas = dict(pd.Series(confirm, index=updateTime[:-1]).sort_index(ascending=False)[:237])
areas = dict(sorted(areas.items(), key=lambda x: x[0], reverse=False))
print(china)
print(areas)


# My_matplotlibs.rcParams['font.family'] = 'SimHei'
# plt.plot(areas.keys(), areas.values(), c='red')
# plt.plot(china.keys(), china.values(), c='pink')
# plt.legend(['国外', '国内'])
# plt.xticks([list(areas.keys())[i] for i in range(0, len(areas), 20)])
# plt.xlabel('日期', fontsize=15)
# plt.ylabel('确诊病例', fontsize=15)
# plt.show()
