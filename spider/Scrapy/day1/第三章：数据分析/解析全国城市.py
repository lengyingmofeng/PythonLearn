# @作者 : 叶枫
# @文件 : 解析全国城市.py 
# @时间 : 2020/11/29 10:07 
# @版本 ：1.0
# @功能描述:
import requests
from lxml import etree
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
}
url = 'https://www.aqistudy.cn/historydata/'
response = requests.get(url, headers=headers).text
tree = etree.HTML(response)
a_list = tree.xpath("//div[@class='bottom']/ul/li/a | //div[@class='bottom']/ul/div[2]/li/a")
count = []
for a in a_list:
    list_a = a.xpath('./text()')[0]
    count.append(list_a)
print(count, len(count))