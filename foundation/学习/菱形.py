# @作者 : 叶枫
# @文件 : 菱形.py 
# @时间 : 2020/10/20 10:22 
# @版本 ：1.0
# @功能描述:
rows=int(input("输入列数："))
i = j = k = 1
print("打印一个菱形:\n")
# 菱形的上半部分
for i in range(rows):
    for j in range(rows-i):
        print(" ", end=" ")
        j += 1
    for k in range(2*i-1):
        print("*", end=" ")
        k += 1
    print("\n")
# 菱形的下半部分
for i in range(rows):
    for j in range(i):
        print(" ", end=" ")
        j += 1
    for k in range(2*(rows-i)-1):
        print("*", end=" ")
        k += 1
    print("\n")
