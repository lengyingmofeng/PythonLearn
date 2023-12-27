# @作者 : 叶枫
# @文件 : 爬虫基础.py 
# @时间 : 2020/11/22 10:55 
# @版本 ：1.0
# @功能描述: 发送get请求

import requests
url = 'https://www.xuexila.com/way/xuexijihua/c231050.html'
# UA伪装： 让爬虫对应的请求载体身份标识伪装成的某一款浏览器
# 封装到一个字典中
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0'

}
# 发送一个get请求
response = requests.get(url, headers=headers)
# 手动设定编码格式
response.encoding = 'utf-8'
# 打印源码的str类型数据
# response.content是存储的bytes类型的响应源码，可以进行decode操作
print(response.text)
with open('baidu.html', 'wb') as f:
    f.write(response.content)

