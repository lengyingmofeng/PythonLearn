# @作者 : 叶枫
# @文件 : 多线程测试.py 
# @时间 : 2021/12/9 8:35
# @版本 ：1.0
# @功能描述:
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


def getPar(name, age, sex):
    for i in range(name):
        print("name", i)

    for j in range(age):
        print("age", j)

    for k in range(sex):
        print("sex", k)
    J(age)
    K(sex)

def J(age):
    num = 0
    for i in range(age):
        print("this is a J", i)
        num += 1
    print("num:", num)

def K(sex):
    number = 0
    for i in range(sex):
        print("this is a K", i)
        number += 1
    print("number:", number)

if __name__ == '__main__':
    args = (100, 200, 300)
    with ThreadPoolExecutor(60) as t:
        for i in range(300):
            # t.submit(lambda x: getPar(*x), (100, 200, 300))
            t.submit(lambda x: getPar(*x), args)
