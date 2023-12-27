import os
import time
from multiprocessing.dummy import Pool

import requests
from bs4 import BeautifulSoup

class Spider:
    # 初始化数据
    def __init__(self, url, header, cookie):
        self.user_url = url
        self.header = header
        self.cookie = cookie
        self.img_list_url = []  # 存放一页的所有图片地址
        self.num = 0  # 计数爬取了多少张图片

    # 获取某一页要下载的图片所有链接
    def res(self):
        response = requests.get(self.user_url, headers=self.header, cookies=self.cookie).text
        soup = BeautifulSoup(response, "html.parser")
        img_href = soup.select(".thumb-listing-page > ul > li  a[href]")
        list_img = [i.get("href") for i in img_href]  # 所有的图片的href
        print("一共", len(list_img), "图片")
        return list_img

    # 获取详情页图片地址
    def detail_page(self, list_img):
        # 遍历获取详情页图片地址
        for item in list_img:
            detail_page = requests.get(item, headers=self.header, cookies=self.cookie).text
            soup = BeautifulSoup(detail_page, "html.parser")
            try:  # 访问过快会爬取不到详情页图片地址，则出现一个空列表从而导致下标越界
                img_url = soup.select("#showcase > div.scrollbox > img[src]")[0]["src"]
                self.img_list_url.append(img_url)
            except IndexError:  # 出现下标越界调用error_img_url方法
                self.error_img_url(item)
        return self.img_list_url

    # 处理获取失败的图片地址
    def error_img_url(self, url):
        # 休眠2秒重新发送请求
        time.sleep(1)
        detail_page = requests.get(url, headers=self.header, cookies=self.cookie).text
        soup = BeautifulSoup(detail_page, "html.parser")
        try:
            img_url = soup.select("#showcase > div.scrollbox > img[src]")[0]["src"]
            self.img_list_url.append(img_url)
        except IndexError:  # 如果还没有获取到图片地址那么递归调用
            self.error_img_url(url)

    # 图片下载
    def download_images(self, img_url):
        if img_url is not None:
            img_name = img_url.split("/")[-1]  # 图片名字
            img = requests.get(img_url, headers=self.header).content
            with open(img_path + "/" + img_name, "wb") as fp:
                fp.write(img)
            print(img_name, "download over~")
            self.num += 1

    def images_count(self):
        print("下载图片数量：", self.num)


if __name__ == '__main__':


    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.56',
    }

    # 用户cookie
    cookie = {
        "_pk_id.1.01b8": "cf3ec85e45058bf8.1664183851.",
        "_pk_ses.1.01b8": "1",
        "remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d": "https://www.baidu.com/s?ie=UTF-8&wd=eyJpdiI6IjVLY3JHK1pSUEt0SEVsNU9haTNJKU2hfHGFYLoD1Bvxjix3AVxH4SEmaYuQwaWxvblJ2S1k5ZjBXdEl4Y1ZtZ3BxRFRoSHE1aDY0Kzhtam1WcjhvdFpLNUtwdUlXdm1QSTZKbFpTNJKU2hfHGFYLoD1Bvxjix3AVxH4SEmaYuJwdFNreDdodWZLeUJJc3ZOSk0yNlp3SUtHSkJzdXh4OCtFb3Bla283RmRvcjgzR0k0bFczb2xvNE1HSlN0eFF0VTNJKU2hfHGFYLoD1Bvxjix3AVxH4SEmaYucEZCR3RTRmh6a283VyIsIm1hYyI6IjBjYzZjY2QzNDkxNWM5MWRmMzkxNWY1ZDIwNTNJKU2hfHGFYLoD1Bvxjix3AVxH4SEmaYuZWVhMzE1MzlmNDcifQ",
        "XSRF-TOKEN": "eyJpdiI6IkQ4WDhodDYwN2RjY3VFZ2JTSTM3N0E9PSIsInZhbHVlIjoiN0pWYytDaHJBNmV1MXFIN08ybnNaTNJKU2hfHGFYLoD1Bvxjix3AVxH4SEmaYuSDdHSGo4UnliZlVUWWJIcCIsIm1hYyI6ImVjMTNJKU2hfHGFYLoD1Bvxjix3AVxH4SEmaYuBvxjix3AVxH4SEmaYuZjFlZmEyMGQ0NGM1M2Y2MWE4ZGYifQ",
        "wallhaven_session": "eyJpdiI6InR4T0R2dmlEdzRMQ0dyMlMzZ0V4S1E9PSIsInZhbHVlIjoiUkVoZWZYMXRCOHE1Q29UN2ZQTWZJRUw1cEhCT3VnOEI0SEZ5Q2lUTlJDU2djeFo1dHIycXlVUXA0Vitia1ZDOSIsIm1hYyI6IjI1ODhiZDFmZmM3YjQyNzJlNWFlMDI1N2ZmNGQ0ZWUyMDkyZmJkODIyMDJmYmJkMTlmYjZmNDY5ZDdjZjU0OWMifQ "
    }

    img_path = "F:/Scrapy/day/2022-09-29"
    if not os.path.exists(img_path):
        os.mkdir(img_path)
    # 开启5个进程下载图片
    pool = Pool(5)
    for item in range(5, 30):
        start = time.time()
        print("正在爬取%d页" % item)
        url = f"https://wallhaven.cc/search?categories=011&purity=011&sorting=date_added&order=desc&page={item}"
        spider = Spider(url, headers, cookie)
        list_img = spider.res()
        img_list_url = spider.detail_page(list_img)
        pool.map(spider.download_images, img_list_url)
        end = time.time()
        spider.images_count()
        print(end - start)
