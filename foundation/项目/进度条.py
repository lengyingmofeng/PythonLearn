# -*- coding: utf-8 -*- 
# @Time : 2020/10/9 20:46 
# @Author : 叶枫
# @File : 进度条.py
import time
print("开始打印进度条".center(100, "*"))
start_time = time.time()                        # 开始时间
today_time = 0                                  # 当前消耗时间
for i in range(100):
    rect_solid = "■" * (i + 1)                 # 图标1
    rect_hello = "□" * (100 - i - 1)           # 图标2
    percent = (i + 1) / 100 * 100
    today_time += time.time() - start_time
    start_time = time.time()
    print("\r{:^3.0f}% [{} >> {}] 耗时: {:.1f} s" .format(percent, rect_solid, rect_hello, today_time), end="")
    time.sleep(0.01)