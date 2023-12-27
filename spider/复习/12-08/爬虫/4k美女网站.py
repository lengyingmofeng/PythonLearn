# @作者 : 叶枫
# @文件 : 4k壁纸大全.py
# @时间 : 2021/10/25 21:18
# @版本 ：1.0
# @功能描述:
import os.path
import time

import requests
from lxml import etree
from concurrent.futures import ThreadPoolExecutor

url = "https://pic.netbian.com/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36',
}
choose = input("选择你要爬取的主题：")

# 获取到主题总页数
def get_page(spider_url):
    response = requests.get(spider_url, headers=headers).text
    response = etree.HTML(response)
    total_page = response.xpath('//div[@class="page"]/span[@class="tex"]/text()')
    return total_page


# 获取到图片url
def getImages(spider_url, file_path):
    response = requests.get(spider_url, headers=headers).text
    response = etree.HTML(response)
    list_img = response.xpath('//div[@class="slist"]/ul/li/a/@href')
    # 遍历一页的图片
    for i in list_img:
        resp = requests.get(url + i, headers=headers)
        resp.encoding = 'gbk'
        resp = etree.HTML(resp.text)
        # 获取到图片路径
        images_url = resp.xpath('//*[@id="img"]/img/@src')[0]
        # 将图片路径进行切片，获得图片的扩展名
        suffix = "." + images_url.split(".")[1]
        # 图片名称
        imgName = resp.xpath('//div[@class="photo-hd"]/h1/text()')[0]
        download(images_url, imgName, suffix, file_path)


# 保存图片
def download(images_url, imgName, suffix, file_path):
    img = requests.get("https://pic.netbian.com/" + images_url, headers=headers).content
    with open(file_path + os.sep + imgName + suffix, "wb") as f:
        f.write(img)
    print(imgName, "over")


# 创建子文件夹
def create_file(i):
    path = r"E:\imgs\2022-9-25"
    # 切换到path路径下
    os.chdir(path)
    # 子文件夹命名
    file_name = "4k{}第{}页".format(choose, i)
    # 如果不存在就创建这个文件夹
    if not os.path.exists(file_name):
        os.makedirs(file_name)
    # 返回路径
    return os.getcwd() + os.sep + file_name


# 运行爬虫
def crawl():
    dit = {
        "美女": "4kmeinv/",
        "风景": "4kfengjing/",
        "游戏": "4kyouxi/",
        "动漫": "4kdongman/",
        "影视": "4kyingshi/",
        "汽车": "4kqiche/",
        "动物": "4kdongwu/",
        "人物": "4krenwu/",
        "美食": "4kmeishi/",
        "手机壁纸": "shoujibizhi/"
    }
    suffix = dit.get(choose)
    spider_url = url + suffix
    # 获取该主题一共有多少页
    total_page = get_page(spider_url)
    print("一共有{}页".format(total_page))
    # for i in range(1, int(total_page)):
    #     print("开始爬取{}页".format(i))
    #     # 存储文件路径
    #     file_path = create_file(i)
    #     if i == 1:
    #         getImages(spider_url, file_path)
    #         continue
    #     spider_url = url + suffix + "index_{}.html".format(i)
    #     getImages(spider_url, file_path)


if __name__ == '__main__':
    crawl()
