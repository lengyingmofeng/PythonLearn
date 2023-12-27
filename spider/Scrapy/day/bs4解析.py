# @作者 : 叶枫
# @文件 : bs4解析.py 
# @时间 : 2021/10/14 15:31
# @版本 ：1.0
# @功能描述:
from bs4 import BeautifulSoup
import requests

url = 'https://www.umei.cc/bizhitupian/weimeibizhi/index.htm'
url_href = "https://www.umei.cc"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/94.0.4606.71 Safari/537.36 "
}

response = requests.get(url, headers=header)
response.encoding = 'utf-8'
# print(response.text)

main_page = BeautifulSoup(response.text, "html.parser")
# main_page.select()
a_List = main_page.find("div", class_="TypeList").find_all("a")
for a in a_List:
    href = url_href + a.get('href')
    # 拿到子页面的源码
    child_page_response = requests.get(href, headers=header)
    child_page_response.encoding = 'utf-8'
    child_page = BeautifulSoup(child_page_response.text, "html.parser")
    # 获取到子页面中img的src路径
    img_src = child_page.find("p", align="center").find('img')
    src = img_src.get('src')
    img_response = requests.get(src)  # 下载图片
    img_name = src.split('/')[-1]  # 命名图片名字区src路径最后一个内容
    with open("img/" + img_name, "wb") as f:
        f.write(img_response.content)  # 图片内容写入文件
    print("over", img_name)
