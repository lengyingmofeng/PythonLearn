# @作者 : 叶枫
# @文件 : 他只是看上去不努力.py 
# @时间 : 2021/12/14 10:05
# @版本 ：1.0
# @功能描述:
import requests
from bs4 import BeautifulSoup
url = "https://www.chazidian.com/gushi53306/"

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36',
}
resp = requests.get(url, headers=headers).text
html = BeautifulSoup(resp, "html.parser")
txt = html.select("#print_content > p")
with open("他只是看上去不努力.txt", "w", encoding='utf-8') as fp:
    for item in txt:
        fp.write(item.text + '\n')

