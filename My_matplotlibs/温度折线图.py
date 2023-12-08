# @作者 : 叶枫
# @文件 : 温度折线图.py 
# @时间 : 2021/11/5 18:04
# @版本 ：1.0
# @功能描述:
import random

from matplotlib import pyplot as plt

plt.rcParams['font.sans-serif'] = ['KaiTi']  # 步骤一（替换sans-serif字体）
plt.rcParams['axes.unicode_minus'] = False  # 步骤二（解决坐标轴负数的负号显示问题）

x = range(0, 120)
y = [random.randint(20, 35) for i in range(120)]
y1 = [random.randint(20, 35) for j in range(120)]
plt.figure(figsize=(20, 8), dpi=80)

plt.plot(x, y, label='上海')
plt.plot(x, y1, label="北京")

# 添加图例
plt.legend()

# 调整x轴刻度
x_tick_labels = ["10点{}分".format(i) for i in range(60)]
x_tick_labels += ["11点{}分".format(i) for i in range(60)]
# 取步长，数字和字符串一一对应，数据的长度一样
plt.xticks(list(x)[::3], x_tick_labels[::3], rotation=45)  # 旋转45度

# 添加描述信息
plt.xlabel("时间")
plt.ylabel("温度")
# 图例
plt.title("10点到11点温度统计表")
plt.show()
