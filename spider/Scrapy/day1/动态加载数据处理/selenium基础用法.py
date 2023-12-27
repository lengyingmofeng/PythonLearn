# @作者 : 叶枫
# @文件 : selenium基础用法.py 
# @时间 : 2020/11/29 15:24 
# @版本 ：1.0
# @功能描述:
from random import random
from time import sleep
from lxml import etree
from selenium import webdriver
bro = webdriver.Chrome(executable_path=r'E:\爬虫\day1\动态加载数据处理\chromedriver.exe')
bro.get('https://wallhaven.cc/search?categories=010&purity=111&topRange=1M&sorting=toplist&order=desc&page=21')
page_text = bro.page_source
tree = etree.HTML(page_text)
li_list = tree.xpath('//*[@id="thumbs"]/section/ul/li/figure/a/@href')
for li in li_list:
    bro.get(li)
    page_text = bro.page_source
    tree = etree.HTML(page_text)
    img_src = tree.xpath('//*[@id="wallpaper"]/@src')[0]
    img_data = bro.get(img_src)
    print(img_data)
