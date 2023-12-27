# @作者 : 叶枫
# @文件 : 多进程.py 
# @时间 : 2021/10/25 19:06
# @版本 ：1.0
# @功能描述:
from multiprocessing import Process


def func(name):
    for i in range(1000):
        print(name, i)


if __name__ == '__main__':
    p = Process(target=func, args=("周杰伦", ))
    p1 = Process(target=func, args=("许嵩", ))
    p1.start()
    p.start()
    for j in range(10000):
        print(j, "本兮")

