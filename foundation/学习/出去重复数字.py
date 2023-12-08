# @作者 : 叶枫
# @文件 : 出去重复数字.py 
# @时间 : 2020/10/14 21:51 
# @版本 ：1.0
# @功能描述:除去列表中重复的数字

# list1 = [1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3]
# list2 = list(set(list1))
# print(list2)
#
# # print(set(list1))
# list2 = []
# for i in list1:
#     if not i in list2:
#         list2.append(i)
# print(list2)
#
#
list1 = [1, 1, 1, 2, 7, 3, 5, 9, 32, 0]
list2 = []
for i in list1:
    if not i in list2:
        list2.append(i)
print(list2)
