# @作者 : 叶枫
# @文件 : parame.py 
# @时间 : 2020/11/22 16:31 
# @版本 ：1.0
# @功能描述:
import requests
url = 'https://www.baidu.com/s?ie=UTF-8&'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0'
}

# response = requests.get(url, headers=headers)
# 构件参数带字典
data = {
    'wd': 'python'
}
response = requests.get(url, headers=headers, params=data)
print(response.url)
with open('baidu.html', 'wb')as f:
    f.write(response.content)