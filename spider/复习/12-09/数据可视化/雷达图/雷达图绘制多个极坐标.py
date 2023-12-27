import matplotlib.pyplot as plt
import numpy as np

"""
绘制多个点，并且第一个点与最后一个点相同，使其成为闭合图案
"""

thete = np.array([0.35, 0.45, 0.64, 1, 1.3])
theta = np.array([0.25, 0.75, 1, 1.5, 0.25])
r = [20, 60, 40, 80, 20]
s = [10, 35, 25, 45, 16]
# 闭合图案背景样色为橙色
plt.polar(theta * np.pi, r, "o-", lw=2)
# 设置填充样色，并且透明度为0.75
plt.fill(theta * np.pi, r, "orange", alpha=0.75)
# 闭合图案背景样色为红色
plt.polar(thete * np.pi, s, "r-", lw=2)
plt.fill(thete * np.pi, s, "r", alpha=0.65)
plt.ylim(1, 100)

# 实现网格线
plt.grid(True)
plt.show()
