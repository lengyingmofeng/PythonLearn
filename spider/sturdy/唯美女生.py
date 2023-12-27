# @作者 : 叶枫
# @文件 : 唯美女生.py 
# @时间 : 2021/12/6 19:17
# @版本 ：1.0
# @功能描述:
import requests
from bs4 import BeautifulSoup
url = "https://baike.baidu.com/item/%E5%91%A8%E6%9D%B0%E4%BC%A6/129156"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
}
resp = requests.get(url, headers=header)
resp.encoding = 'utf-8'
resp = resp.text
content = BeautifulSoup(resp, "html.parser")
cont = content.select(".lemmaWgt-lemmaCatalog")
print(cont)