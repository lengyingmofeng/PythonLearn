# @作者 : 叶枫
# @文件 : 九九乘法表.py 
# @时间 : 2020/10/14 21:05 
# @版本 ：1.0
# @功能描述:
for i in range(1,10):
    for j in range(1, i + 1):
        print(i, "x", j, "=", i * j, end=" ")
    print("")
