# @作者 : 叶枫
# @文件 : requests豆瓣电影获取.py 
# @时间 : 2020/11/27 18:48 
# @版本 ：1.0
# @功能描述:
import json
import requests
url = 'https://movie.douban.com/j/search_subjects'
s = {
    'type': 'movie',
    'tag': '日本',
    'sort': 'recommend',
    'page_limit': '20',
    'page_start': '0'
}
headers = {
     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0'
}
response = requests.get(url, s, headers=headers)
response = response.json()
fp = open('豆瓣.html', "w", encoding='utf8')
json.dump(response, fp, ensure_ascii=False)
