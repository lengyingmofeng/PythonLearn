# @作者 : 叶枫
# @文件 : 爬取视频.py 
# @时间 : 2021/10/27 15:15
# @版本 ：1.0
# @功能描述:
import re

import requests

obj = re.compile(r"url: '(?P<url>.*?)',", re.S)  # 用来提取m3u8的url
url = "http://91kanju2.com/vod-play/6017-3-2.html"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/94.0.4606.81 Safari/537.36",
}

resp = requests.get(url, headers=headers).text
m3u8_url = obj.search(resp).group("url")
print(m3u8_url)

resp2 = requests.get(m3u8_url, headers=headers).content
with open("色戒.m3u8", "wb") as f:
    f.write(resp2)
print("下载完成")

n = 1
# 读取文件
with open("色戒.m3u8", "r", encoding="utf-8") as fp:
    for item in fp:
        item = item.strip()  # 先去掉空格，空白，换行符
        if item.startswith('#'):  # 不要#号开头的数据
            continue
        print(item)
        # 下载视频
        resp3 = requests.get(item, headers=headers)
        f = open(f"video/{n}.mp4", "ab")
        f.write(resp3.content)
        f.close()
        resp3.close()
        print(n)
        n += 1
