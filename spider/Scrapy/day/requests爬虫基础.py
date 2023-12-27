# @作者 : 叶枫
# @文件 : requests爬虫基础.py 
# @时间 : 2020/11/22 10:51 
# @版本 ：1.0
# @功能描述:
from urllib.request import urlopen
from urllib.request import Request
#
url = "https://rt.huashi6.com/front/works/rank_page"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/94.0.4606.71 Safari/537.36 "
}
request = Request(url, headers=header)
response = urlopen(request)
html = response.read().decode('utf-8')
data = html
print(data)
# with open("mybaidu.html", "w", encoding='utf-8') as f:
#     f.write()
# print("over!")