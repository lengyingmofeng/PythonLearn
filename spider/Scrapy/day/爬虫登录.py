import time
from concurrent.futures import ThreadPoolExecutor

import requests
from bs4 import BeautifulSoup


class Spider:
    def __init__(self, user_url, header, cookie):
        self.user_url = user_url
        self.header = header
        self.cookie = cookie
        self.img_count = 0

    # 获取某一页要下载的图片所有链接
    def res(self):
        response = requests.get(self.user_url, headers=self.header, cookies=self.cookie).text
        soup = BeautifulSoup(response, "html.parser")
        img_href = soup.select(".thumb-listing-page > ul > li  a[href]")
        for i in img_href:
            self.detail_page(i.get("href"))

    # 获取详情页图片地址
    def detail_page(self, url):
        detail_page = requests.get(url, headers=self.header, cookies=self.cookie).text
        soup = BeautifulSoup(detail_page, "html.parser")
        try:
            img_url = soup.select("#showcase > div.scrollbox > img[src]")[0]["src"]
            self.download_images(img_url)
        except IndexError:
            self.detail_page(url)

    # 图片下载
    def download_images(self, img_url):
        img_name = img_url.split("/")[-1]  # 图片名字
        img = requests.get(img_url, headers=self.header).content
        with open("./Wallhaven/" + img_name, "wb") as fp:
            fp.write(img)
        print(img_url)
        print(img_name, "download,over~")
        self.img_count += 1

if __name__ == '__main__':
    url = "https://wallhaven.cc/search?categories=011&purity=111&sorting=date_added&order=desc&page=2"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.56',
    }
    cookie = {
        "_pk_id.1.01b8": "cf3ec85e45058bf8.1664183851.",
        "_pk_ses.1.01b8": "1",
        "remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d": "https://www.baidu.com/s?ie=UTF-8&wd=eyJpdiI6IjVLY3JHK1pSUEt0SEVsNU9haTNJKU2hfHGFYLoD1Bvxjix3AVxH4SEmaYuQwaWxvblJ2S1k5ZjBXdEl4Y1ZtZ3BxRFRoSHE1aDY0Kzhtam1WcjhvdFpLNUtwdUlXdm1QSTZKbFpTNJKU2hfHGFYLoD1Bvxjix3AVxH4SEmaYuJwdFNreDdodWZLeUJJc3ZOSk0yNlp3SUtHSkJzdXh4OCtFb3Bla283RmRvcjgzR0k0bFczb2xvNE1HSlN0eFF0VTNJKU2hfHGFYLoD1Bvxjix3AVxH4SEmaYucEZCR3RTRmh6a283VyIsIm1hYyI6IjBjYzZjY2QzNDkxNWM5MWRmMzkxNWY1ZDIwNTNJKU2hfHGFYLoD1Bvxjix3AVxH4SEmaYuZWVhMzE1MzlmNDcifQ",
        "XSRF-TOKEN": "eyJpdiI6IkQ4WDhodDYwN2RjY3VFZ2JTSTM3N0E9PSIsInZhbHVlIjoiN0pWYytDaHJBNmV1MXFIN08ybnNaTNJKU2hfHGFYLoD1Bvxjix3AVxH4SEmaYuSDdHSGo4UnliZlVUWWJIcCIsIm1hYyI6ImVjMTNJKU2hfHGFYLoD1Bvxjix3AVxH4SEmaYuBvxjix3AVxH4SEmaYuZjFlZmEyMGQ0NGM1M2Y2MWE4ZGYifQ",
        "wallhaven_session": "eyJpdiI6InR4T0R2dmlEdzRMQ0dyMlMzZ0V4S1E9PSIsInZhbHVlIjoiUkVoZWZYMXRCOHE1Q29UN2ZQTWZJRUw1cEhCT3VnOEI0SEZ5Q2lUTlJDU2djeFo1dHIycXlVUXA0Vitia1ZDOSIsIm1hYyI6IjI1ODhiZDFmZmM3YjQyNzJlNWFlMDI1N2ZmNGQ0ZWUyMDkyZmJkODIyMDJmYmJkMTlmYjZmNDY5ZDdjZjU0OWMifQ"
    }

    start = time.time()
    spider = Spider(url, headers, cookie)
    spider.res()
    end = time.time()
    print(spider.img_count)
    print(end - start)