# @作者 : 叶枫
# @文件 : 用字典判断单词出现.py 
# @时间 : 2020/10/20 10:10 
# @版本 ：1.0
# @功能描述:

word = input("输入几个单词：")
dict1 = {}
s = ""
for key in word:
    if key != ' ':
        s += key
    else:
        if dict1.get(s) == None:
            dict1[s] = 1
        else:
            dict1[s] += 1
        s = ""
if dict1.get(s) == None:
     dict1[s] = 1
else:
     dict1[s] += 1
print(dict1)