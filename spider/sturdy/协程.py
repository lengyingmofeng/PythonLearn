# @作者 : 叶枫
# @文件 : 协程.py 
# @时间 : 2021/10/26 12:04
# @版本 ：1.0
# @功能描述:
import asyncio
import time


async def fun1():
    print("周杰伦")
    await asyncio.sleep(3)
    print("周杰伦")


async def fun2():
    print("2")
    await asyncio.sleep(4)
    print("2")


async def fun3():
    print("3")
    await asyncio.sleep(2)
    print("3")


task = [
    fun3(),
    fun2(),
    fun1()
]
asyncio.run(asyncio.wait(task))
