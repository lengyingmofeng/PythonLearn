# @作者 : 叶枫
# @文件 : bs4今日热榜.py 
# @时间 : 2021/10/15 9:48
# @版本 ：1.0
# @功能描述:
import requests
from bs4 import BeautifulSoup
url = "https://tophub.today/"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/86.0.4240.183 Safari/537.36 '
}

res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')
# div_a_span = soup.select("#node-1 > div > div")[1:][0].select("span.t")
# for item in div_a_span:
#     print(item.string)

div_a_span = soup.select("#node-1 > div > div")[1:][0].find_all('a')
for item in div_a_span:
    print(item['href'])

