# @作者 : 叶枫
# @文件 : numpy_nadarray.py 
# @时间 : 2021/11/9 19:58
# @版本 ：1.0
# @功能描述:
import numpy as np

# # 多于一个维度
# a = np.array([[1,1,1], [2, 2, 2]])
# print(a)
#
# # 最小维度
# b = np.array([1, 2, 3, 4, 5, 6], ndmin=3)
# print(b)
#
# # 把array的类型设置成float类型
# c = np.array([1,  2,  3], dtype=float)
# print(c)
#
# # arange(10) -> array(range(10))
# d = np.arange(10)
# print(d)
#
#
# x = [1, 2, 3]
# x = np.array(x)
# print(x, type(x))
#
# y = (1, 2, 3)
# y = np.array(y)
# print(y)


# x = np.array([[1, 2], [3, 4], [5, 6]])
# y = x[[0, 1, 2], [0, 0, 0]]
# y = x[[0, 1, 2], [1, 1, 1]]
# y = x[[1, 0, 2], [1, 0, 1]]
#
#
# print(y)

# x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
# print('我们的数组是：')
# print(x)
# print('\n')
# rows = np.array([[0, 1], [3, 2]])
# cols = np.array([[0, 2], [0, 2]])
# print()
# y = x[rows, cols]
# print('这个数组的四个角元素是：')
# print(y)

arr = np.arange(6).reshape((1, 2, 3))
print(arr)