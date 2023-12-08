import pandas as pd

from pyecharts.charts import Bar
from pyecharts import options as opts

df = pd.read_csv("DXYArea.csv")
# 取出不包含中国的
all = df.loc[df['countryEnglishName'] != "China", ["provinceName", 'provinceEnglishName', 'province_confirmedCount']]
# 取出英文省份的唯一值
allContry = all['provinceEnglishName'].unique().tolist()
# 添加中国
allContry.append("China")
# 国家不为中国省份中有香港 和澳门,去除
del (allContry[-2])
del (allContry[-2])
# 数据中有nan值,找到去除
for i in allContry:
    if type(i) == float:
        allContry.remove(i)

# 拿到所有的省份英文名/省份感染总计人数/更新时间
an = df.loc[:, ['provinceEnglishName', 'province_confirmedCount', 'updateTime']]
# 计算取值
list = {}
for i in range(len(allContry)):
    # 获得英文名为指定的国家的数据
    db = an.loc[an['provinceEnglishName'] == allContry[i], ['province_confirmedCount', 'updateTime']]
    # 起始日期
    c = '2020-11-12'
    q = '2020-11-11'
    while True:
        # 如果没有找到,最后的日期停止,赋值为0
        if q.__contains__('2020-01-22'):
            list[allContry[i]] = 0
            break
        else:
            # 模糊查询
            a = db.loc[db['updateTime'].str.contains(c), ['province_confirmedCount']]
            b = db.loc[db['updateTime'].str.contains(q), ['province_confirmedCount']]
            # 如果前一个日期下的没有数据,日期提前一天
            if len(a) == 0 or len(b) == 0:
                c = pd.to_datetime(c) + pd.Timedelta(days=-1)
                c = str(c).split(' ')[0]
                q = pd.to_datetime(q) + pd.Timedelta(days=-1)
                q = str(q).split(' ')[0]
            else:
                # 计算结果
                num = a.iloc[0] - b.iloc[0]
                # 字典包裹
                list[allContry[i]] = int(num)
                break
# 将字典转换为DataFrame
p = pd.DataFrame(list, index=['A']).stack().unstack(level=0)
# 将DataFrame转为Series
pa = pd.Series(p['A'].values, index=p.index)
# 对数据排序
pa = pa.sort_values(ascending=False).head(10)
# 取出国家列表
country = pa.index.tolist()
# 取出对应的数据列表
values = pa.values.tolist()
print(country)
print(values)

# 绘图
bar = (
    Bar()
    .add_xaxis(country)
    .add_yaxis("感染人数", values, category_gap='80%')
    .set_global_opts(title_opts=opts.TitleOpts(title="新增top10的国家"),
                     xaxis_opts=opts.AxisOpts(axislabel_opts={"rotate": 45}), )
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
)
bar.render("新增top10.html")
