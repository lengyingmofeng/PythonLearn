# @作者 : 叶枫
# @文件 : requests豆瓣电影获取.py
# @时间 : 2020/11/27 18:48
# @版本 ：1.0
# @功能描述:
import requests
url = 'https://wenku.baidu.com/view/b664ac4fcf84b9d528ea7a85.html?rec_flag=default'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0'
}
response = requests.get(url, headers=headers)
print(response.text)
response.encoding = "utf-8"
with open("物理试卷.html", "wb") as fp:
    fp.write(response.content)


