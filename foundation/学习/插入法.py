# @作者 : 叶枫
# @文件 : 插入法.py 
# @时间 : 2020/10/10 19:14 
# @版本 ：1.0
import random
import time

lst = [random.randint(1, 9999) for i in range(5000)]
print("排序前：", lst)
start = time.time()
for i in range(1, len(lst)):                        # i 从1开始
    num = lst[i]                                    # 把第i个lst元素赋值给num
    j = i - 1
    while j >= 0 and lst[j] > num:
        lst[j + 1] = lst[j]
        j -= 1
    lst[j + 1] = num
print("排序后：", lst)
print("插入排序耗时：{}".format(time.time() - start))