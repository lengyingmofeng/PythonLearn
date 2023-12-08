# @作者 : 叶枫
# @文件 : 冒泡法.py 
# @时间 : 2020/10/10 18:22 
# @版本 ：1.0
import random
lst = [random.randint(1, 100) for i in range(5)]
print("排序前：", lst)
for i in range(len(lst)):                               # for(int i = 0 ; i < lst.length(); i++)
    for j in range(len(lst) - i - 1):                   # for(int j = 0 ; j < lst.length() - 1 - i ; j++)
        if lst[j] > lst[j + 1]:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]
print("排序后:", lst)