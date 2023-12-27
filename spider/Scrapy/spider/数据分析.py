# @作者 : 叶枫
# @文件 : 数据分析.py 
# @时间 : 2021/11/27 10:17
# @版本 ：1.0
# @功能描述
import pandas as pd
from matplotlib import pyplot as plt

def show_bar():
    df = pd.read_csv('huashi.csv')
    df['likeNum'] = [int(float(str(i).split('w')[0]) * 10000) if str(i).endswith('w') else int(i) for i in
                     df['likeNum']]
    df.set_index("title", inplace=True)
    #
    df = df['likeNum'].sort_values(ascending=False)[:20]
    print(df)
    _x = df.index
    _y = df.values
    plt.figure(figsize=(15, 8), dpi=80)
    # 给柱状图颜色设置成#c04851,#22a2c3,#e2c027
    plt.bar(_x, _y, color=["#c04851", "#22a2c3", "#e2c027"])
    # 设置x轴刻度，并且标题旋转90°
    plt.xticks(range(len(_x)), _x, rotation=90)
    plt.show()

"""
    读取csv文件，分析出前10名绘画最多作品的作者
"""
def show_pie():
    df = pd.read_csv('huashi.csv')
    # 按照作者进行分组统计出前10名绘画作品最多的作者
    data = df.groupby("author")['likeNum'].count().sort_values(ascending=False)[:10]
    print(data)
    _x = data.index
    _y = data.values
    print(_x)
    print(_y)
    # 设置画布大小(10*8)
    plt.figure(figsize=(10, 8), dpi=100)
    plt.title("画师通前10名作者更新作品数量")
    # 绘画饼图，起始角度为90度
    plt.pie(_y, labels=_x, autopct='%1.1f%%', startangle=90)
    plt.show()


if __name__ == '__main__':
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 步骤一（替换sans-serif字体）
    plt.rcParams['axes.unicode_minus'] = False
    show_bar()
    show_pie()
