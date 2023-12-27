# @作者 : 叶枫
# @文件 : 雷达图.py 
# @时间 : 2021/12/9 19:02
# @版本 ：1.0
# @功能描述:

import numpy as np
import matplotlib
import matplotlib.pyplot as plt

matplotlib.rcParams['font.family'] = 'SimHei'
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
labels = np.array(['第一周', '第二周', '第三周', '第四周', '第五周', '第六周'])
nAttr = 6
Python = np.array([60.4, 57.9, 100, 100, 92.4, 87.5])
angles = np.linspace(0, 2 * np.pi, nAttr, endpoint=False)

# Python = np.concatenate((Python, [Python[0]]))
# angles = np.concatenate((angles, [angles[0]]))


print(np.pi)
fig = plt.figure(facecolor="white")
plt.subplot(111, polar=True)
plt.plot(angles, Python, 'ro--', color='g', linewidth=2, markersize=30)
plt.fill(angles, Python, facecolor='g', alpha=0.2)
plt.thetagrids(angles * 180 / np.pi, labels)
plt.figtext(0.52, 0.95, 'Rachel的python成绩分析图', ha='left')
plt.figtext(0.52, 0.95, '2019310143011', ha='right')
plt.grid(True)
plt.savefig('acculate.JPG')
plt.show()
