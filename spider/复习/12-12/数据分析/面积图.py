# @作者 : 叶枫
# @文件 : 面积图.py 
# @时间 : 2021/12/14 19:41
# @版本 ：1.0
# @功能描述:
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
df = pd.DataFrame(np.random.rand(10, 4), columns=['a', 'b', 'c', 'd'])
# df.a.plot.area() # 单个列
# df.plot.area()
# plt.show()
labels = ["a", "b"]
# 面积图
plt.stackplot(df.index, df.a.values, df.b.values, labels=labels)

plt.legend()
plt.show()