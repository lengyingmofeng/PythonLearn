# @作者 : 叶枫
# @文件 : request入门测试.py 
# @时间 : 2021/10/12 15:23
# @版本 ：1.0
# @功能描述:

import requests

# 爬取内容网址
# name = input("输入你想知道的内容：")
# url = f"https://www.baidu.com/s?ie=UTF-8&wd={name}"
# header = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36"
# }
# # 向网址发送get请求
# response = requests.get(url, headers=header)
# # 讲网址内容存储到文件中
# with open("123.html", "w", encoding="utf-8") as fp:
#     fp.write(response.text)
#
# # 读取完并且关闭
# fp.close()
# print("over")




# url = "https://fanyi.baidu.com/sug"
#
# header = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36"
# }
#
# en = input("输入你想要翻译的单词：")
# # 百度翻译中有一个名叫kw的字典，这个字典中包含了输入的英文单词和翻译出来的内容
# data = {
#     "kw": en
# }
# response = requests.post(url, headers=header, data=data)
# print(response.json())



# 爬取豆瓣电影数据
url = "https://movie.douban.com/j/search_subjects"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/94.0.4606.71 Safari/537.36 "
}
params = {
    "type": "movie",
    "tag": "热门",
    "sort": "recommend",
    "page_limit": "20",
    "page_start": "0"
}
response = requests.get(url, params=params, headers=header)
print(response.json())

response.close()
