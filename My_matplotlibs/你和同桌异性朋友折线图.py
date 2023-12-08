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
plt.plot(x, y, label='自己', color='skyblue', linestyle='-.')
plt.plot(x, z, label='同桌', color='red', linestyle='--')

# 设置x刻度
x_tick_labels = ["{}岁".format(i) for i in x]
plt.xticks(x, x_tick_labels, fontproperties=font)

# 设置y轴刻度
plt.yticks(number)
plt.gray()
# 添加图例，
plt.legend(prop=font, loc="upper center")

# 展示
plt.show()