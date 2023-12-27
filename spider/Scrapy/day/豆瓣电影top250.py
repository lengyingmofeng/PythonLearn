# @作者 : 叶枫
# @文件 : 豆瓣电影top250.py 
# @时间 : 2021/10/13 16:08
# @版本 ：1.0
# @功能描述:
import csv

import requests
import re

url = "https://movie.douban.com/top250"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/94.0.4606.71 Safari/537.36 "
}
response = requests.get(url, headers=header)
page_content = response.text
response.close()

obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)</span>.*?<p class="">.*?<br>('
                 r'?P<year>.*?)&nbsp;.*?<span class="rating_num" property="v:average">(?P<score>.*?)</span>'
                 r'.*?<div class="star">.*?<span>(?P<eval>.*?)</span>', re.S)

result = obj.finditer(response.text)
f = open("top250.csv", "w", encoding="utf-8", newline='')
csv_writer = csv.writer(f)
for item in result:
    # print(item.group('name'))
    # print(item.group('year').strip())
    # print(item.group('score'))
    # print(item.group('eval'))
    # print(item.groupdict())
    dic = item.groupdict()
    # print(dic)
    dic['year'] = dic['year'].strip()
    print(dic.values())
    csv_writer.writerow(dic.values())

f.close()





# import requests
# import csv
# import re
# # 不算导包的话正式代码6行 存储到csv文件
# url = "https://movie.douban.com/top250?start={}&filter="
# headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"}
# obj = re.compile(r'a.*?<span class="title">(.*?)</span>.*?<br>\s+(.*?)&.*?:average">(.*?)</span>.*?<span>(.*?)人评价</span>', re.S)
# with open('douban250.csv', 'w', encoding='utf-8', newline='') as file:
#     csv_write = csv.writer(file)
#     [csv_write.writerows(obj.findall(requests.get(url=url.format(page), headers=headers).text)) for page in range(0, 226, 25)]
