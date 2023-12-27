# @作者 : 叶枫
# @文件 : 条形图.py 
# @时间 : 2021/12/9 16:07
# @版本 ：1.0
# @功能描述:
import matplotlib.pyplot as plt
import numpy as np
y = [4, 6, 2, 1, 6]
x = ["EDG", "RNG", "WE", "IG", "OMG"]

plt.figure(figsize=(10, 5), dpi=80)

# plt.barh(x, y, height=0.6)
# plt.show()
# plt.bar(x, y, width=0.6)
# plt.show()


arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
plt.plot(arr[0], arr[1:])
plt.show()
print(arr[0], arr[1:])
