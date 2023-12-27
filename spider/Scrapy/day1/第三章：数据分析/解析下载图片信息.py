# @作者 : 叶枫
# @文件 : 解析下载图片信息.py 
# @时间 : 2020/11/28 20:54 
# @版本 ：1.0
# @功能描述:
import os
from pathlib import Path
import requests
from lxml import etree
import time
count_time = time.time()
# 判断是否有picLibs这个文件夹
if not os.path.exists("picLibs"):
    os.mkdir("picLibs")     # 没有就创建picLibs文件夹

url = "http://pic.netbian.com/4kmeinv/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
}
for i in range(98, 147):
    if i != 1:
        new_url = url + "index_" + str(i) + ".html"
    else:
        new_url = url
    response = requests.get(new_url, headers=headers).text
    tree = etree.HTML(response)
    list_li = tree.xpath("//ul[@class='clearfix']/li")
    for li in list_li:
        # 拼接a连接， 找到最终图片
        img_href = "http://pic.netbian.com" + li.xpath("./a/@href")[0]
        # 获取最终图片的页面
        response_img = requests.get(url=img_href, headers=headers).text
        trees = etree.HTML(response_img)
        img = trees.xpath('//div[@class="photo-pic"]/a/img/@src')[0]
        img_src = "http://pic.netbian.com" + img
        img_name = trees.xpath('//div[@class="photo-pic"]/a/img/@alt')[0] + ".jpg"
        img_name = "".join(img_name.encode('iso-8859-1').decode("gbk").split(" "))
        if img_name.find("/") != -1:
            img_name = "".join(img_name.split("/"))
        if img_name.find("*") != -1:
            img_name = "".join(img_name.split("*"))
        img_data = requests.get(img_src, headers=headers).content
        img_path = 'picLibs/' + img_name
        with open(img_path, "wb") as fp:
            fp.write(img_data)
            print("第", i, "页", img_name, "下载成功")
sum_time = time.time() - count_time
print("一共花了", sum_time, "秒")
