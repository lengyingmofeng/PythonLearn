# @作者 : 叶枫
# @文件 : 新发地.py 
# @时间 : 2021/12/2 17:53
# @版本 ：1.0
# @功能描述:
import requests
import csv
import time

def downloader_vegetable_price(i):
    data = {
        "current": i
    }
    resp = requests.post(url, headers=headers, data=data)
    dic = resp.json()['list']
    for item in dic:
        prodName = item['prodName']
        lowPrice = item['lowPrice']
        highPrice = item['highPrice']
        avgPrice = item['avgPrice']
        place = item['place']
        unitInfo = item['unitInfo']
        pubDate = item['pubDate']
        csv_fp.writerow([prodName, lowPrice, highPrice, avgPrice, place, unitInfo, pubDate])
    print(f"第{i}爬取完成")




url = "http://www.xinfadi.com.cn/getPriceData.html"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/94.0.4606.81 Safari/537.36",
}

# 打开文件
fp = open("菜价.csv", "w", encoding="utf-8", newline='')
csv_fp = csv.writer(fp)
# 存入标题
csv_fp.writerow(["品名", "最低价", "平均价", "最高价", "产地", "单位", "发布日期"])
first_time = time.time()  # 开始时间
# with ThreadPoolExecutor(50) as t:
for i in range(1, 10):
        # t.submit(downloader_vegetable_price, i)
    downloader_vegetable_price(i)
last_time = time.time()     # 最终时间
final = last_time - first_time  # 用时时间
print(f"用时时间{final}")
fp.close()  # 关闭文件