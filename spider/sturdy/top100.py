# -*- coding: utf-8 -*-
import requests
from lxml import etree


datalist = []
url = 'https://www.bilibili.com/ranking'
headers = {
    "User-Agent": "Mozilla / 5.0(Windows NT 10.0; Win64; x64)AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 80.0.3987.122Safari / 537.36"
}
resp = requests.get(url, headers=headers)
html = resp.text
print(html)
parse_html = etree.HTML(html)
# print(html)#得到bilibili排⾏榜信息
# 解析数据
Upzhu = parse_html.xpath('//*[@id="app"]/div[1]/div/div[1]/div[2]/div[3]/ul/li/div[2]/div[2]/div[1]/a/span/text()')
datalist.append(Upzhu)
title = parse_html.xpath('//*[@id="app"]/div[1]/div/div[1]/div[2]/div[3]/ul/li/div[2]/div[2]/a/text()')
datalist.append(title)
play = parse_html.xpath('//*[@id="app"]/div[1]/div/div[1]/div[2]/div[3]/ul/li/div[2]/div[2]/div[1]/span[1]/text()')
datalist.append(play)
comment = parse_html.xpath('//*[@id="app"]/div[1]/div/div[1]/div[2]/div[3]/ul/li/div[2]/div[2]/div[1]/span[2]/text()')
datalist.append(comment)
hot = parse_html.xpath('//*[@id="app"]/div[1]/div/div[1]/div[2]/div[3]/ul/li/div[2]/div[2]/div[2]/div/text()')
datalist.append(hot)
print(datalist)
# # 保存数据
# df = pd.DataFrame(datalist)
# df = pd.DataFrame(df.values.T, index=df.columns, columns=df.index)
# df.to_excel('Bilibili排⾏榜.xlsx')
