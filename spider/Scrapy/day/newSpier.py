# @作者 : 叶枫
# @文件 : 爬虫基础.py
# @时间 : 2020/11/22 10:51
# @版本 ：1.0
# @功能描述:
# import requests
# url = "https://www.xuexila.com/way/xuexijihua/c231050.html"
# response = requests.get(url)
# response.encoding = 'GBK'
# print(response.text)
import os
import requests
import redis
from lxml import etree
import urllib.request
import time
import threading
from queue import Queue
import re

Headers = {
    'authority': 'wallhaven.cc',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    # 'cookie': '',  # 请写上自己的
    'referer': 'https://wallhaven.cc/',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.56',  # 请修改为自己的
}


class Producer(threading.Thread):
    def __init__(self, page_queue, img_queue, *args, **kwargs):
        super(Producer, self).__init__(*args, **kwargs)
        self.page_queue = page_queue
        self.img_queue = img_queue

    def run(self):
        while True:
            # 如果page_queue是空的那么跳出死循环
            if self.page_queue.empty():
                break
            # 获取所有page_url
            page_url = self.page_queue.get()
            page_text = self.deal_url(page_url)
            self.parse_indexPage(page_text)

    # 拿到每一页html
    def deal_url(self, url):
        response = requests.get(url, headers=Headers)
        response.encoding = response.apparent_encoding
        return response.text

    # 解析每一页并且获取到图片地址
    def parse_indexPage(self, text):
        html = etree.HTML(text)
        wallpaper_urls = html.xpath("//img[@alt='loading']/@data-src")
        for url in wallpaper_urls:
            url = url.replace('th', 'w', 1)  # 替换第一个th为w
            url = url.replace('small', 'full')  # 替换small为full
            last_urlTail = re.search(r'[^/]+(?!.*/)', url).group()  # 正则获取url最后一个/后的内容
            new_urlTail = 'wallhaven-' + last_urlTail
            url = url.replace(last_urlTail, new_urlTail)  # 重构网址
            self.img_queue.put((new_urlTail, url))


class Consumer(threading.Thread):
    def __init__(self, page_queue, img_queue, *args, **kwargs):
        super(Consumer, self).__init__(*args, **kwargs)
        self.page_queue = page_queue
        self.img_queue = img_queue

    def run(self):
        while True:
            if self.img_queue.empty() and self.page_queue.empty():
                break
            img_name, img_url = self.img_queue.get()
            self.save_img(img_name, img_url)

    def save_img(self, img_name, img_url):
        root = './3_figure/'
        path = root + img_name
        try:
            if not os.path.exists(root):
                os.mkdir(root)
            if not os.path.exists(path):
                read_figure = requests.get(img_url)
                with open(path, 'wb') as f:
                    f.write(read_figure.content)
                    f.close()
                    print(path + " save ok！")
            else:
                print('文件已保存')
        except:
            print("文件爬取失败")


def main():
    base_url = 'https://wallhaven.cc/search?q={}&page={}'
    #     keyword = input("please input the keyword")
    keyword = 'anime'
    page_queue = Queue(20)
    img_queue = Queue(200)
    page_num = 10
    # 10页图片的url地址，添加到page_queue中
    for x in range(1, page_num + 1):
        url = base_url.format(keyword, x)
        page_queue.put(url)
        print(url)

    #
    for x in range(5):
        t = Producer(page_queue, img_queue)
        t.start()

    for x in range(5):
        t = Consumer(page_queue, img_queue)
        t.start()


if __name__ == '__main__':
    main()
