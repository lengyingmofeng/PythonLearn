# @作者 : 叶枫
# @文件 : huashi.py 
# @时间 : 2021/11/27 9:07
# @版本 ：1.0
# @功能描述:
import csv
import json
from urllib import request
import re


# 获取网页源码
def url_request():
    url = "https://www.huashi6.com/hot"
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE"
    }
    req = request.Request(url, headers=header)
    data = request.urlopen(req)
    data = data.read().decode()
    return data


# 解析用户数据
def analysis(data):
    # 利用正则匹配到用户数据
    obj = re.compile(r'"user".*?,(?P<datas>.*?);(?P<name>.*?);', re.S)
    html = obj.search(data).group('datas')
    html = "{" + html
    # 把数据转换成json数据
    dic = json.loads(html)
    return dic


# 存储数据
def setCsvFile(html):
    file_csv.writerow(["title", "author", "likeNum"])
    data = html['works']['worksHotListData']['datas']
    for item in data:
        title = item['title']
        author = item['painter']['name']
        likeNum = int(item['likeNum'])
        if likeNum > 10000:
            likeNum = round(likeNum / 10000, 1)
            likeNum = str(likeNum) + "w"
        file_csv.writerow([title, author, likeNum])
    fp.close()


if __name__ == '__main__':
    fp = open("123.csv", "w", encoding='utf-8', newline='')
    file_csv = csv.writer(fp)
    data = url_request()
    dic = analysis(data)
    setCsvFile(dic)
