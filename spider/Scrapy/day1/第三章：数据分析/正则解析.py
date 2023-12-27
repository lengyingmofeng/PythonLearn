# @作者 : 叶枫
# @文件 : 正则解析.py 
# @时间 : 2020/11/28 9:29 
# @版本 ：1.0
# @功能描述:
#-*- coding:utf-8 -*-
import re
import requests
import os
# 创建一个文件夹，用来保存图片
if not os.path.exists("wallhaven"):
    os.mkdir("wallhaven")
url = 'http://pic.netbian.com/4kdongman/%s'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
}
for i in range(1, 147):
    index = "index_" + str(i) + ".html"
    # print(index)
    new_url = format(url%index)
    # print(new_url)
    page_text = requests.get(new_url, headers=headers).text
    ex = '<li>.*?<img src="(.*?)" alt.*?></li>'
    img = re.findall(ex, page_text, re.S)
    # print(img)
    for src in img:
        # 拼接出一个完整的图片地址
        src = "http://pic.netbian.com" + src
        # 请求图片的二进制数据
        img_data = requests.get(src, headers=headers).content
        # 生成图片名称
        img_name = src.split('/')[-1]
        # 图片存储路径
        imgPath = "wallhaven/" + img_name
        with open(imgPath, "wb") as fp:
            fp.write(img_data)
            print(imgPath, "下载成功")
    print("第", i, "页")
