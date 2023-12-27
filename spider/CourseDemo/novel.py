"""
@Time     :2023/12/7 11:12
@Author   :JOAAN
@FileName :下载小说.py
@SoftWare :PyCharm
"""

# 导入数据请求模块-->第三方模块，需要安装
import requests

# 导入正则表达式模块 -->内置模块，不需要安装
import re

"""
1、发送请求，模拟浏览器对于url地址发送请求
        请求链接：http://www.1biqug.net/book/994/1171642.html
        安装模块方法：
            --win+R 输入cmd，输入安装命令 pip install requests
            -- 在pycharm终端，输入安装命令
"""

# 请求链接
url = 'http://www.1biqug.net/book/994/1171642.html'

# 模拟浏览器  headers 请求头
headers = {
    # User-Agent:用户代理   表示浏览器基本身份信息
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}

# 发送请求
response = requests.get(url=url, headers=headers)

# <Response [200]>   响应对象，表示请求成功
# print(response)

"""
2、获取数据，获取服务器返回响应数据内容
    开发者工具：response
    response.text -->获取响应文本数据  <网页源代码/html字符串数据>

3、解析数据，提取我们想要的数据内容
    标题/内容
    re正则表达式：是直接对于字符串数据进行解析
        re.findall('什么数据','什么地方')   -->从什么地方，去找什么数据


    css选择器：根据标签属性提取数据
    xpath节点提取：提取标签节点提取数据
"""
title = re.findall('<h1>(.*?)</h1>', response.text)[0]
print(title)
content = re.findall(r'<div id="content">.*?<br />\s*(.*?)</div>', response.text, re.S)[0]
print(content)
text = re.sub(r'<br\s*?/?>', '', content)
text = re.sub('<span.*?>(.*?)</span>', '', text)
print(text)
