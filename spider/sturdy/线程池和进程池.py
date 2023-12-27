# @作者 : 叶枫
# @文件 : 线程池和进程池.py 
# @时间 : 2021/10/25 19:24
# @版本 ：1.0
# @功能描述:
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


def fn(name):
    for i in range(100):
        print(name, i)
    fc()


def fc():
    for i in range(1000):
        print("fc", i)


# 创建线程池
with ThreadPoolExecutor(50) as t:
    for i in range(100):
        print(i)
        t.submit(fn, name=f"线程{i}")
