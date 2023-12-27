import requests

headers = {
    #代理信息  模拟浏览器
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
}
with open("./咖啡图片.txt", "r") as fp:
    url_list = fp.readlines()

for url in url_list:
    url = url.strip()
    response = requests.get(url, headers=headers)
    name = url.split("/")[-1]
    name = name.split("_.webp")[0]
    with open("H:/coffee/" + name, "wb") as f:
        f.write(response.content)
        print(name)

