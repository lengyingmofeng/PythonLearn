# @作者 : 叶枫
# @文件 : 条形图.py 
# @时间 : 2021/11/8 21:10
# @版本 ：1.0
# @功能描述:

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
y = [4, 6, 2, 1, 6]
x = ["EDG", "RNG", "WE", "IG", "OMG"]

font = FontProperties(fname=r"C:\Windows\Fonts\simsun.ttc")

# 给条形图设置一个宽度
width = 0.3
plt.figure(figsize=(15, 7), dpi=80)
plt.bar(x, y, width=width, label="春季赛")
"""
[i + 0.3 for i in range(len(x))] 改变x轴绘图的坐标让图形不在同一个坐标上
np.random.randint(1, 6, 5) 随机生成1~6五个数字

"""
plt.bar([i + 0.3 for i in range(len(x))], np.random.randint(1, 6, 5), width=width, label="夏季赛")
# 改变x轴的刻度让标题在两个图形中间
plt.xticks([i + 0.15 for i in range(len(x))], x)
plt.legend(loc=1, prop=font)
plt.grid()
plt.show()