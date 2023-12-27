# @作者 : 叶枫
# @文件 : 哔哩哔哩评论.py 
# @时间 : 2021/12/19 15:26
# @版本 ：1.0
# @功能描述:
import json

import requests
import re
url = "https://api.bilibili.com/x/v2/reply/main?callback=jQuery172044763337754901467_1639898213554&jsonp=jsonp&next=0&type=1&oid=806812317&mode=3&plat=1&_=1639898229993"

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36',
    "referer": "https://www.bilibili.com/",
}

# response = requests.get(url, headers=header).text
# with open("./评论.json", "w", encoding='utf-8') as fp:
#    fp.write(response)

with open('评论.json', encoding='utf-8') as fp:
    data = fp.read()
message_list = []
data = json.loads(data)
data = data["data"]['replies']
for item in data:
    print(item['content']['message'])
# print(message_list)