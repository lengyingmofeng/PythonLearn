# @作者 : 叶枫
# @文件 : 简历模板.py 
# @时间 : 2020/11/29 10:21 
# @版本 ：1.0
# @功能描述:
import os

import requests
from lxml import etree

if not os.path.exists("moban"):
    os.mkdir("moban")
url = 'https://sc.chinaz.com/moban/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
}
# response = requests.get(url, headers=headers).text
# tree = etree.HTML(response)
# count = tree.xpath('//div[@class="fenye"]')
# for item in count:
#     print(item)
for i in range(34, 899):
    response = requests.get(url, headers=headers).text
    tree = etree.HTML(response)
    page_text = tree.xpath("//*[@id='container']/div/div/a/@href")
    for page in page_text:
        new_url = 'https:' + page
        new_response = requests.get(new_url, headers=headers).text
        new_tree = etree.HTML(new_response)
        new_page = new_tree.xpath('//div[@class="downbody"]/div[3]/a[1]/@href')
        title = new_tree.xpath('//title/text()')[0]
        title = title.encode('iso-8859-1').decode("utf-8")
        file_path = "moban/" + title
        for item in new_page:
            file_data = requests.get(item, headers=headers, allow_redirects=False).content
            with open(file_path, "wb") as fp:
                fp.write(file_data)
                print("第", i, "页", title)