# @作者 : 叶枫
# @文件 : 4k壁纸大全.py
# @时间 : 2021/10/25 21:18
# @版本 ：1.0
# @功能描述: 爬取4k图片
import os.path
import time

import requests
from lxml import etree
from concurrent.futures import ThreadPoolExecutor


def download(url):
    page_text = requests.get(url, headers=headers, proxies=proxies).text
    tree = etree.HTML(page_text)
    list_img = tree.xpath('//div[@class="slist"]/ul/li/a/@href')
    for item in list_img:
        item = child_url + item
        resp = requests.get(item, headers=headers).text
        tre = etree.HTML(resp)
        child = tre.xpath('//*[@id="img"]/img/@src')[0]
        img_name = child.split("/")[-1]
        child = child_url + child
        img = requests.get(child, headers=headers)
        with open("img_src/" + img_name, "wb") as f:
            f.write(img.content)
        print(img_name, "over")
    time.sleep(2)


# 地址
child_url = "https://pic.netbian.com"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36',
    "referer": "https://pic.netbian.com/4kmeinv/"
}
# 使用代理
proxies = {
    "http:": "http://183.47.237.251:80"
}

if not os.path.exists("img_src"):
    os.mkdir("img_src")
i = 1
with ThreadPoolExecutor(12) as t:
    while i <= 148:
        if i == 1:
            url = "https://pic.netbian.com/4kmeinv"
            i += 1
        else:
            suffix = f"/index_{i}.html"
            url = "https://pic.netbian.com/4kmeinv" + suffix
            i += 1
        t.submit(download, url)
