import pandas as pd  # 引用pandas
from pyecharts.charts import Bar
from pyecharts import options as opts

df = pd.read_csv('DXYArea.csv')  # 读取数据
countryName = list(set(df['countryName']))  # 去掉重复的国家名
df.drop_duplicates(inplace=True)
print(df.to_string())
# last_day = '2020-11-11'  # 昨天的日期
# today = '2020-11-12'  # 今天的日期
# country_values = []  # 定义一个国家的空数组
# values = []  # 定义一个确诊人数的空数组
# for i in countryName:  # for循环遍历国家
#     d = df[df['countryName'] == i]  # 寻找国家名等于i的信息
#     a = d[d['updateTime'].str.contains(last_day)]  # 模糊查询，等于昨天的信息
#     b = d[d['updateTime'].str.contains(today)]  # 模糊查询，等于今天的信息
#     if len(a) > 0 and len(b) > 0:  # 如果昨天和今天的信息的长度大于0，
#         country_values.append(i)  # 往国家的数组里面添加数据
#         values.append(max(b['province_confirmedCount']) - max(a['province_confirmedCount']))  # 往values数组里面放新增确诊人数的数据
#     else:  # 如果昨天和今天的信息长度等于0
#         country_values.append(i)  # 往国家的数组里面添加数据
#         values.append(0)  # 往values数组里面添加0
# c = pd.DataFrame()  # 定义一个空的DataFrame
# c['countryName'] = country_values  # 一列放国家
# c['values'] = values  # 一列放确诊人数
# c = c.sort_values(by='values', ascending=False)  # 进行从大到小排序
# c1 = c.head(10)  # 取前十个国家
# countryName = c1['countryName'].values.tolist()  # 获取前十个国家的名字
# values = c1['values'].values.tolist()  # 获取前十个国家的新增确诊人数
# import My_matplotlibs.pyplot as plt
#
# plt.rcParams['font.sans-serif'] = ['simhei']
# plt.bar(countryName, values)
# plt.xlabel('国家')
# plt.ylabel('新增确诊人数')
# plt.title('前十大国家新增确诊人数')
# plt.show()
#
# bar = (
#     Bar()
#     .add_xaxis(countryName)
#     .add_yaxis("感染数", values)
#     .set_global_opts(title_opts=opts.TitleOpts(title="国家前十感染数"),
#                      xaxis_opts=opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=True)),
#                      yaxis_opts=opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=True)), )
#     .render("世界前十国家感染数.html")
# )
