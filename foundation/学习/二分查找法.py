# @作者 : 叶枫
# @文件 : 二分查找法.py
# @时间 : 2020/10/9 21:10
# @版本 ：1.0
import random
lst = []
for i in range(20):
    rand_num = random.randint(1, 101)
    while rand_num in lst:
        rand_num = random.randint(1, 101)
    lst.append(rand_num)
print("生产的随机列表", lst)
lst.sort()
print(lst)
math = eval(input("请输入你要查找的数字："))
index = -1
low = 0
high = len(lst) - 1
while high >= low:
    mid = (low + high) // 2
    if math < lst[mid]:
        high = mid - 1
    elif math == lst[mid]:
        index = mid
        break
    else:
        low = mid + 1
print("要查找的元素下标为：", index)
