from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties

# 设置字体
font = FontProperties(fname=r"c:\windows\fonts\STSONG.TTF", size=10)

x = [i for i in range(11, 31)]  # 表示年龄
y = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1]  # 表示自己异性朋友个数
z = [0, 0, 1, 1, 2, 2, 3, 3, 2, 3, 2, 3, 4, 3, 4, 3, 3, 2, 1, 1]  # 表示同桌异性朋友个数
number = range(0, 7)
# 图纸设置大小
plt.figure(figsize=(10, 8), dpi=100)

# 绘图
lines = plt.plot(x, y, x, z)
# 设置x刻度
x_tick_labels = ["{}岁".format(i) for i in x]
plt.xticks(x, x_tick_labels, fontproperties=font)

# 设置y轴刻度
plt.yticks(number)
plt.legend(lines, ["自己", "同桌"], shadow=True, fancybox=True, prop=font)
# 添加参考线
plt.axvline(x=23, linestyle='--')
plt.axhline(y=3, linestyle='--')

# 添加参考区域
plt.axvspan(xmin=18, xmax=30, alpha=0.3, ymax=1)
plt.axhspan(ymin=2, ymax=4, alpha=0.3)


# 添加指向型注释文本
plt.annotate("最小值", xy=(13, 1), xytext=(13, 1.2), arrowprops=dict(arrowstyle="-|>"), fontproperties=font)
# 展示
plt.show()