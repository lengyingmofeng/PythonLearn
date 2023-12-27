# @作者 : 叶枫
# @文件 : headers参数的使用.py 
# @时间 : 2020/11/22 16:25 
# @版本 ：1.0
# @功能描述:

import requests
url = 'http://www.baidu.com'
headers = {

}
# 在请求头中带上user-agent，模拟浏览器发送请求
response = requests.get(url, headers=headers)
print(response.content.decode())
# 打印请求头信息
print(response.request.headers)
