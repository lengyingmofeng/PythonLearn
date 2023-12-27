# @作者 : 叶枫
# @文件 : 爬虫基础.py
# @时间 : 2020/11/22 10:51
# @版本 ：1.0
# @功能描述:
import requests
from bs4 import BeautifulSoup

url = "https://www.xuexila.com/way/xuexijihua/c231050.html"
response = requests.get(url)
response.encoding = 'GBK'
print(response.text)


# 获取详情页图片地址
def detail_page(self, list_img):
    # 遍历获取详情页图片地址
    for item in list_img:
        detail_page = requests.get(item, headers=self.header, cookies=self.cookie).text
        soup = BeautifulSoup(detail_page, "html.parser")
        img_url = soup.select("#showcase > div.scrollbox > img[src]")[0]["src"]
        self.img_list_url.append(img_url)
        print(img_url, "添加成功")
        self.error_img_url(item)
    return self.img_list_url