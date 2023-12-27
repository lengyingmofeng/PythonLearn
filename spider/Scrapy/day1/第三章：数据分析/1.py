# @作者 : 叶枫
# @文件 : 正则解析.py
# @时间 : 2020/11/28 9:29
# @版本 ：1.0
# @功能描述:
#-*- coding:utf-8 -*-
import re
import requests
import os
import pickle
from pathlib import Path
# 创建一个文件夹，用来保存图片
if not os.path.exists("img_src"):
    os.mkdir("img_src")
url = 'http://pic.netbian.com/4kdongman/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
}
page_text = requests.get(url, headers=headers).text
ex = '<li>.*?<img src="(.*?)" alt.*?></li>'
img = re.findall(ex, page_text, re.S)
print(img)
img_dir = Path('./img_src')
for src in img:
    # 拼接出一个完整的图片地址
    src = "http://pic.netbian.com" + src
    # 请求图片的二进制数据
    img_data = requests.get(src, headers=headers).content
    # 生成图片名称
    img_name = src.split('/')[-1]
    print(img_name)
    # 图片存储路径
    imgPath = "img_src/" + img_name
    with open(imgPath, "wb") as fp:
        print(img_data)
        fp.write(img_data)
        print(imgPath, "下载成功")


