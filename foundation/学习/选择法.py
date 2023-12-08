# @作者 : 叶枫
# @文件 : 选择法.py 
# @时间 : 2020/10/10 19:07 
# @版本 ：1.0
import random
lst = [random.randint(1, 101) for i in range(5)]
print("排序前:", lst)
for i in range(len(lst)):
    for j in range(len(lst)):
        if lst[i] < lst[j]:
            lst[i], lst[j] = lst[j], lst[i]
print("排序后:", lst)