# @作者 : 叶枫
# @文件 : 列表中的奇偶数.py 
# @时间 : 2020/10/14 21:08 
# @版本 ：1.0
# @功能描述:
"""
任务：分别统计给定的列表中奇数和偶数的个数。
"""
list_value = [1, 2, 18, 7, 33, 22, 1045, 98, 78, 36, 10, 111, 105, 4320, 1014, 50, 63, 15, 18, 910, 2010, 3201, 2501, 25, 120, 320]
d, k =0, 0
list1 = []
list2 = []
for i in range(len(list_value)):
    if list_value[i] % 2 == 0:
        d += 1
        list1 .append(list_value[i])
    else:
        k += 1
        list2 .append(list_value[i])
print(d, k,)
print("list1 偶数= ", list1, "\n list1 奇数 = ", list2)

