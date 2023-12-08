# @作者 : 叶枫
# @文件 : Plot.py 
# @时间 : 2021/10/18 11:37
# @版本 ：1.0
# @功能描述:
import os.path
import random

import numpy as np
import requests
from matplotlib import pyplot as plt
x = range(0, 120)
y = [random.randint(20, 35) for i in range(120)]
# 设置图片大小
plt.figure(figsize=(20, 8), dpi=80)
plt.axis([1, 110, 6, 90])
# 绘图
plt.plot(x, y)

# 调整x轴刻度
x_tick_labels = ["10点{}分".format(i) for i in range(60)]
x_tick_labels += ["11点{}分".format(i) for i in range(60)]
# 设置刻度
plt.xticks(x, labels=x_tick_labels, rotation=45)
# 保存
plt.savefig("./plt.jpg")
# 展示图形
plt.show()
