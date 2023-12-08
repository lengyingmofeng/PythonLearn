import pandas as pd
from My_matplotlibs import pyplot as plt
from My_matplotlibs.ticker import MultipleLocator
from pyecharts.charts import Line
from pyecharts import options as opts

df = pd.read_csv('DXYArea.csv')
China = df.loc[(df['countryName'] == "中国") & (df['provinceName'] == "中国"), ['provinceName', 'province_confirmedCount', 'updateTime']]
date = China['updateTime'].sort_values(ascending=True)
date = pd.to_datetime(date).dt.date.unique().tolist()
date = [str(i) for i in date]
print(date)
China_data = []
for i in range(len(date)):
    if i == len(date) - 1:
        break
    else:
        num = China.loc[China['updateTime'].str.contains(date[i + 1]), ['province_confirmedCount']].iloc[0] - \
              China.loc[China['updateTime'].str.contains(date[i]), ['province_confirmedCount']].iloc[0]
        China_data.append(abs(int(num)))
all_Conutry = df.loc[df['countryName'] != "中国", ['provinceName', 'province_confirmedCount', 'updateTime']]
all_Data = []
for i in range(len(date)):
    if i == len(date) - 1:
        break
    else:
        shuju = all_Conutry.loc[
            all_Conutry['updateTime'].str.contains(date[i + 1]), ['province_confirmedCount', 'provinceName']]
        shuju1 = shuju.groupby('provinceName')['province_confirmedCount'].head(1).sum()
        a = all_Conutry.loc[
            all_Conutry['updateTime'].str.contains(date[i]), ['province_confirmedCount', 'provinceName']]
        b = a.groupby('provinceName')['province_confirmedCount'].head(1).sum()
        num = int(shuju1 - b)
        all_Data.append(abs(num))
del (date[0])


# 使用pandas内置matplotlib绘图
# d = pd.DataFrame()
# d['date'] = date
# d = d.set_index('date')
# d['China_data'] = China_data
# d['all_Data'] = all_Data
# d.plot()
# plt.show()

# 导入matplotlib库绘图
# plt.plot(date,China_data,color="r")
# plt.plot(date,all_Data,color="b")
# plt.xticks(rotation=45)
# x_major_locator=MultipleLocator(19)
# ax=plt.gca()
# ax.xaxis.set_major_locator(x_major_locator)
# plt.show()
def Line_charts() -> Line:
    c = Line()
    c.add_xaxis(xaxis_data=date)
    c.add_yaxis(series_name='中国新增趋势', y_axis=China_data)
    c.add_yaxis(series_name='国外新增趋势', y_axis=all_Data)
    data_zoom = {
        "show": False,
        "title": {"zoom": "data zoom", "back": "data zoom restore"}
    }
    # 不显示图形上y轴的值
    c.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    # 数据项设置,全局只设置一次
    c.set_global_opts(
        # 设置标题
        title_opts=opts.TitleOpts(title="国内与国外新增趋势"),
        # 设置图例is_show=False是不显示图例
        legend_opts=opts.LegendOpts(is_show=True),
        # 设置提示项
        tooltip_opts=opts.TooltipOpts(trigger='axis', axis_pointer_type='cross'),
        # 工具箱的设置
        toolbox_opts=opts.ToolboxOpts(is_show=True, feature=opts.ToolBoxFeatureOpts(data_zoom=data_zoom))
    )
    return c


tu = Line_charts()
tu.render("国内_国外.html")
