# @作者 : 叶枫
# @文件 : Two_Home.py
# @时间 : 2020/11/28 20:19 
# @版本 ：1.0
# @功能描述:
import requests
from lxml import etree
url = 'https://www.xuexila.com/way/xuexijihua/c231050.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
}
# 获取源代码数据
response = requests.get(url, headers=headers).text
tree = etree.HTML(response)
# print(tree)
list_li = tree.xpath('/html')
fp = open("58.txt", "w", encoding="utf-8")
for li in list_li:
    title = li.xpath('./div[2]/h2/a/text()')[0]
    fp.write(title + "\n")
    print(title)
