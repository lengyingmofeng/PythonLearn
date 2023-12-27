# @作者 : 叶枫
# @文件 : urlopen.py 
# @时间 : 2021/10/17 10:54
# @版本 ：1.0
# @功能描述:
import json
import csv
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

# url = "https://rt.huashi6.com/front/works/rank_page"
# img_url = "https://img2.huashi6.com/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/86.0.4240.183 Safari/537.36 '
}
# request = Request(url, headers=headers)
# response = urlopen(url)
# html = response.read().decode('utf-8')
# data = json.loads(html)
# for index, data in enumerate(data['data']['works']['datas']):
#     print("author:", data['painter']['name'])
#     print("title:", data['title'])
#     print("img_url:", data['coverImage']['path'])

url = "http://tjj.hunan.gov.cn/hntj/tjsj/sjfb/hnsj/202101/t20210129_14302808.html"
request = Request(url, headers=headers)
response = urlopen(request)
html = response.read().decode('utf-8')
html = BeautifulSoup(html, 'html.parser')
List_html = html.select('div#d_article')[0].select('table > tbody > tr')[3::]
with open("text2.csv", "w", encoding='utf-8', newline='\n') as f:
    csv_writer = csv.writer(f)
    for item in List_html:
        lst = []
        a = item.select('td > p')
        g = 0
        for arg in a:
            if g == 0:
                d = arg.text.strip()
                if d != '-':
                    lst.append(d)
                else:
                    lst.append('')
                g+=1
            else:
                d = arg.text.strip()
                if d != '-':
                    lst.append(float(d))
                else:
                    lst.append('')
        print(lst)
        csv_writer.writerow(lst)
    f.close()
