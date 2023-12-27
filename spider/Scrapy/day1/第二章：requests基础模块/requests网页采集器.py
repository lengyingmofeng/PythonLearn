# @作者 : 叶枫
# @文件 : requests网页采集器.py 
# @时间 : 2020/11/27 16:35 
# @版本 ：1.0
# @功能描述:
import requests

url = 'https://www.baidu.com/s?ie=UTF-8&'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0'
}
kw = input("enter a word:")
params = {
    'wd': kw
}
response = requests.get(url, params=params, headers=headers)
response.encoding = 'utf8'
FileName = kw + '.html'
with open(FileName, 'wb') as f:
    f.write(response.content)
