import requests
import aiohttp
import asyncio
import aiofiles
from time import time
from lxml import etree
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os
from time import sleep

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36 Edg/86.0.622.43",
}

def preprocessing(browser):
    url = 'https://m.tuiimg.com/'
    browser.get(url=url)
    windows = browser.window_handles
    a_arr = browser.find_elements_by_xpath('//*[@id="main"]/li/a')
    for image in a_arr:
        # 图片地址 https://m.tuiimg.com/meinv/2195/
        item_href = image.get_attribute("href")
        res = requests.get(url=item_href, headers=headers).content
        tree = etree.HTML(res)
        total_text = tree.xpath('//*[@id="allbtn"]/text()')[0]
        # 图集总数量
        image_total = int(total_text.split('/')[1].replace(")", ""))
        # 图解名称
        images_name = tree.xpath('//*[@id="container"]/div[3]/h1/text()')[0]
        print(images_name)
        base_img_url = "/".join(tree.xpath('//*[@id="nowimg"]/@src')[0].split("/")[0:-1]) + "/"
        print(base_img_url)
        start_time = time()
        tasks = []
        for i in range(1, image_total + 1):
            # 耗时操作 异步处理
            tasks.append(saveImage(base_img_url + str(i) + ".jpg", images_name + str(i) + ".jpg"))
        loop = asyncio.get_event_loop()
        loop.run_until_complete(asyncio.wait(tasks))
        print(images_name, "图集下载花费的时间是" + str(time() - start_time), "秒")


async def saveImage(image_url, images_name):
    print("准备下载", images_name)
    file_path = "./妹子美图合集1/"
    if not os.path.exists(file_path):
        os.mkdir(file_path)
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(url=image_url) as response:
            async with aiofiles.open(file_path + images_name, "wb") as afp:
                await afp.write(await response.content.read())
        print(images_name, "保存成功")

if __name__ == '__main__':
    s = Service("chromedriver.exe")
    chrome = webdriver.Chrome()
    preprocessing(browser=chrome)

