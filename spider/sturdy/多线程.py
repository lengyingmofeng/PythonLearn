# @作者 : 叶枫
# @文件 : 多线程.py 
# @时间 : 2021/10/25 17:17
# @版本 ：1.0
# @功能描述:
from threading import Thread


def func():
    for i in range(1000):
        print("子线程", i)


if __name__ == '__main__':
    func()
    thread = Thread(target=func)
    thread.start()
    for i in range(1000):
        print("主线程", i)


class MyThread(Thread):
    def run(self):
        for i in range(100000):
            print("func", i, "=")


if __name__ == '__main__':
    t = MyThread()
    t.start()
    for i in range(100000):
        print("main", i)



