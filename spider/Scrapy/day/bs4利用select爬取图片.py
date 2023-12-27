# @作者 : 叶枫
# @文件 : bs4利用select爬取图片.py 
# @时间 : 2021/10/14 20:12
# @版本 ：1.0
# @功能描述:
import requests
import time

# url = "https://www.huashi6.com/hot"
url = "https://rt.huashi6.com/front/works/rank_page"
img_url = "https://img2.huashi6.com/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/86.0.4240.183 Safari/537.36 '
}
array_img =[":", "/", "'", ":D"]
# 页数
index = 1
while True:
    # data存储每页显示多少数据
    date = {"index": index, "size": 10}
    response = requests.post(url, headers=headers, data=date)
    response = response.json()
    # 获取到图片
    data = response.get('data').get('works')  # ['data']['works']
    for i in data:
        img_url_list = img_url + i['coverImage']['path']    # 拿到图片的url地址
        img_format = img_url_list.split(".")[-1]    # 获取到图片的扩展名
        img_name = i['title']   # 拿到图片标题
        if img_name in array_img:
            img_name = "array_img"
            print(img_name)
        # 图片下载
        print("img/" + img_name + '.' + img_format)
        with open("F:/Scrapy/day/img/" + img_name + '.' + img_format, "wb") as f:
            print(img_url_list)
            child_response_src = requests.get(img_url_list, headers=headers)
            f.write(child_response_src.content)
            print(img_name, "打印成功")

    if index < 5:
        index += 1
    else:
        break


a = ":D"
if a in array_img:
    print("在的")