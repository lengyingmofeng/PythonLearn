# @作者 : 叶枫
# @文件 : 代理模式.py 
# @时间 : 2021/10/25 14:39
# @版本 ：1.0
# @功能描述:
import requests
url = "https://www.baidu.com/"
proxies = {
    "http": "121.8.215.106"
}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/94.0.4606.81 Safari/537.36",
}
resp = requests.get(url, headers=headers, proxies=proxies)
print(resp.text)