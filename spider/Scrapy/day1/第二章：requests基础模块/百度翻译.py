# @作者 : 叶枫
# @文件 : 百度翻译.py 
# @时间 : 2020/11/27 17:14 
# @版本 ：1.0
# @功能描述:
import json

import requests
url = 'https://fanyi.baidu.com/sug'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0'
}
query = input("请输入要翻译的内容：")
data = {
    'kw': query
}
response = requests.post(url, data=data, headers=headers)
response = response.json()
print(response)
Filename = query + '.html'
fp = open(Filename, "w", encoding='utf-8')
json.dump(response, fp, ensure_ascii=False)
fp.close()