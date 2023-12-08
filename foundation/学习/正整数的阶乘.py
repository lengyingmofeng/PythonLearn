# @作者 : 叶枫
# @文件 : 正整数的阶乘.py 
# @时间 : 2020/10/14 21:30 
# @版本 ：1.0
# @功能描述:
num = eval(input("请输入一个正整数："))
sm = 1
if isinstance(num, int) and num > 0:
    for i in range(1, num + 1):
        sm *= i
    print(sm)
else:
    print("你输入的有误不是一个正整数")