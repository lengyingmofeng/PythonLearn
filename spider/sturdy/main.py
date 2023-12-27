import aiohttp
import asyncio
import time
import requests


# 异步下载
async def aiodownload(url, session):
    name = url.split("/")[-1]
    # 发送请求, 这⾥和requests.get()⼏乎没区别, 除了代理换成了proxy
    async with session.get(url) as resp:
        # 读取数据. 如果想要读取源代码. 直接resp.text()即可. ⽐原来多了个()
        content = await resp.content.read()
        # 写⼊⽂件, 有兴趣可以参考aiofiles, 我这⾥根本不需要.
        with open(name, mode="wb") as f:
            f.write(content)


async def main():
    # 创建session对象 -> 相当于requsts对象
    async with aiohttp.ClientSession() as session:
        # 添加下载任务
        tasks = [asyncio.create_task(aiodownload(url, session)) for url in urls]
        # 等待所有任务下载完成
        await asyncio.wait(tasks)


# 同步⽅式下载图⽚
def download(url):
    name = url.split("/")[-1]
    resp = requests.get(url)
    content = resp.content
    with open(name, mode="wb") as f:
        f.write(content)


# 我故意弄了⼀堆url做测试
urls = [
    "http://kr.shanghai-jiuxin.com/file/2020/1031/26b7e178e987be6d914bf8d1af120890.jpg",
    "http://kr.shanghai-jiuxin.com/file/2020/1031/191468637cab2f0206f7d1d9b175ac81.jpg",
    "http://kr.shanghai-jiuxin.com/file/2020/1031/563337d07af599a9ea64e620729f367e.jpg",
    "http://kr.shanghai-jiuxin.com/file/2020/1031/563337d07af599a9ea64e620729f367e.jpg",
]
if __name__ == '__main__':
    t2 = time.time()
    for url in urls:
        download(url)
    print(time.time() - t2)
    t1 = time.time()
    # 异步爬⾍
    asyncio.get_event_loop().run_until_complete(main())
    print(time.time() - t1)