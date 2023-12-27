# @作者 : 叶枫
# @文件 : aiohttp模块应用.py 
# @时间 : 2021/10/26 16:24
# @版本 ：1.0
# @功能描述:
import asyncio
import time

import aiohttp
import requests
import aiofiles
from lxml import etree

url = "https://www.umei.cc/p/gaoqing/"
child_url = "https://www.umei.cc/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/94.0.4606.81 Safari/537.36",
}


async def get_ListImg(url):
    resp = requests.get(url, headers=headers)
    resp.encoding = 'utf-8'
    html = etree.HTML(resp.text)
    List_img = html.xpath('//div[@class="TypeList"]/ul/li/a/@href')
    tasks = []
    for item in List_img:
        item = child_url + item
        tasks.append(get_ChildImg(item))
    print(tasks)
    await asyncio.wait(tasks)


async def get_ChildImg(url):
    task = []
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as resp:
            html = etree.HTML(await resp.text())
            # img_a = html.xpath('//div[@class="NewPages"]/a/@href')
            # img_count = html.xpath('//div[@class="NewPages"]/a/@href')[-1]
            # img_count = img_count.split('_')[-1].split('.')[0]
            # print(img_count)
            img_src = html.xpath('//div[@class="ImageBody"]/p//img/@src')
            task.append(download(img_src[0]))
        print(task)
        await asyncio.wait(task)


async def download(url):
    name = url.split("/")[-1]
    # 发送请求 aiohttp.ClientSession <==> requests.session
    async with aiohttp.ClientSession() as session:
        # 得到图片
        async with session.get(url, headers=headers) as resp:
            async with aiofiles.open("weimei/" + name, "wb") as fp:  # 保存图片
                # resp.text() 读取文本， resp.json() 转换成json， resp.content.read() 读取二进制
                await fp.write(await resp.content.read())  # 读取内容是异步的，需要await挂起
            print(name, "over")


if __name__ == '__main__':
    t1 = time.time()
    asyncio.get_event_loop().run_until_complete(get_ListImg(url))
    print(time.time() - t1)
