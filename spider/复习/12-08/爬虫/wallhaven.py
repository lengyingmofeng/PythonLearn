# @作者 : 叶枫
# @文件 : wallhaven.py
# @时间 : 2021/12/8 15:31
# @版本 ：1.0
# @功能描述:
import os
import time
from concurrent.futures import ThreadPoolExecutor

import requests
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36',
    "XSRF-TOKEN": "eyJpdiI6IlU0Z1dUUXQweHF6c0toT3ZxaHpibnc9PSIsInZhbHVlIjoiU1lmcU5McE5DWUJHRmVXZDhQb2lmNVlaeE1jQ2gxUzBITUowZm42b1RFOGdEWlgwXC9DRmU5YXgxdjdCZm04aTNJKU2hfHGFYLoD1Bvxjix3AVxH4SEmaYuZmUyZWVlMGU2MGE3NmFiYTI4NDE3MDkzY2M5NjE5ODg3ZDhjOWRmZDMxNWYwIn0%3D;"
}


def get_page(i):
    url = "https://wallhaven.cc/latest"
    if i == 1:
        resp = requests.get(url, headers=headers).text
        resp = etree.HTML(resp)
        all_images = resp.xpath('//section[@class="thumb-listing-page"]/ul/li/figure/a/@href')
        getChildPage(all_images, i)
    else:
        spare_url = url + "?page={}".format(i)
        resp = requests.get(spare_url, headers=headers).text
        resp = etree.HTML(resp)
        all_images = resp.xpath('//section[@class="thumb-listing-page"]/ul/li/figure/a/@href')
        getChildPage(all_images, i)


def getChildPage(all_images, file_name):
    # 创建文件夹
    path = create_file(file_name)
    for index, data in enumerate(all_images):
        time.sleep(1)
        resp = requests.get(data, headers=headers).text
        resp = etree.HTML(resp)
        time.sleep(1)
        images_url = resp.xpath('//*[@id="wallpaper"]/@src | div[@class="scrollbox"]/img/@src')
        # 判断是否获取到图片地址，获取到则下载否则保存到txt文件中
        if images_url:
            print(index + 1, "获取到", data)
            download(path, images_url[0])
        else:
            print(index, "没有爬取到的图片地址", data)
            fp.write(data + "\n")


# 创建文件夹
def create_file(file_name):
    # 需要创建的文件名
    i = "第{}页".format(file_name)
    # 保存文件路径
    path = r"E:\imgs\2022-09-25"
    os.chdir(path)  # 切换到该路径下
    # 如果需要的文件名称不存在则创建
    if not os.path.exists(i):
        os.makedirs(i)
    print(i)
    # 返回该目录
    return os.getcwd() + os.sep + i


# 下载到之前保存的目录
def download(path, images_url):
    imgName = images_url.split('/')[-1]
    resp = requests.get(images_url, headers=headers).content
    with open(path + os.sep + imgName, "wb") as fp:
        fp.write(resp)
    print(path + os.sep + imgName, "over")


# 运行爬虫
def crawl():
    i = 1
    with ThreadPoolExecutor(3) as t:
        while i < 30:
            t.submit(get_page, i)
            # get_page(i)
            i += 1
        t.shutdown()


if __name__ == '__main__':
    fp = open("./没有爬取到的图片地址.txt", "a")
    crawl()
    fp.close()
