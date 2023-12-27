import requests
from bs4 import BeautifulSoup
import csv

url = "https://changsha.zbj.com/search/f/?kw=后端"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/94.0.4606.81 Safari/537.36 "
}

reps = requests.get(url, headers=headers)
page = BeautifulSoup(reps.text, 'lxml')
fp = open("猪八戒.csv", "w", encoding='utf-8', newline='')  # 打开一个文件夹
csv_fp = csv.writer(fp)      # 写入文件
csv_fp.writerow(["公司", "价格", "交易数量"])
title_list = page.select("div.new-service-wrap > div")
for item in title_list:
    title = item.select("div > div > a.service-bottom-wrap > div.service-shop > p")[0].text.strip()
    price = item.select("div > div > a.service-top-wrap > div.service-info-wrap > div.service-price > span.price")[0].text.replace('¥', '')
    amount = item.select("div > div > a.service-top-wrap > div.service-info-wrap > div.service-price > span.amount")[0].text
    amount = amount.split(':')[-1].replace('笔', '')
    csv_fp.writerow([title, price, amount])
