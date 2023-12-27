# @作者 : 叶枫
# @文件 : wallhaven.py
# @时间 : 2020/11/29 12:31
# @版本 ：1.0
# @功能描述:
import math
import random

import requests
from urllib.request import urlopen
from lxml import etree
url = "https://wallhaven.cc/search?categories=010&purity=111&topRange=1M&sorting=toplist&order=desc"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
}
j = 0


for i in range(9, 96):
    new_url = url + "&page=" + str(i)
    print(new_url)
    response = requests.get(new_url, headers=headers).text
    tree = etree.HTML(response)
    list_li = tree.xpath('//*[@id="thumbs"]/section/ul/li/figure/a/@href')
    for li_a in list_li:                                            # 遍历获得的a标签地址
        print(li_a)
        new_response = requests.get(li_a, headers=headers).text     # 获取a标签的页面
        new_tree = etree.HTML(new_response)
        img_src = new_tree.xpath('//*[@id="wallpaper"]/@src')[0]    # 图片最后地址
        mant = random.randint(400, 1000000)
        img_alt = "wallhaven" + str(mant)
        img_path = 'wall/' + img_alt + ".jpg"                     # 存储路径
        img_data = requests.get(img_src, headers=headers).content
        with open(img_path, "wb") as fp:
            fp.write(img_data)
            print(img_alt, "下载成功")
            j += 1
    print("第", i, "页")
