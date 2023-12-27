# @作者 : 叶枫
# @文件 : 雷达图绘制极点.py 
# @时间 : 2021/12/9 21:35
# @版本 ：1.0
# @功能描述:
from matplotlib import pyplot as plt
import numpy as np
plt.polar(0.25 * np.pi, 90, 'ro', lw=2)
plt.ylim(0, 50)
plt.show()




