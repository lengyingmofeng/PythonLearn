import csv
import json

import requests
from bs4 import BeautifulSoup


# 打开文件
def open_file(fm):
    fd = None
    if fm == 'txt':
        fd = open('douban.txt', 'w', encoding='utf-8')
    elif fm == 'json':
        fd = open('douban.json', 'w', encoding='utf-8')
    elif fm == 'csv':
        fd = open('douban.csv', 'w', encoding='utf-8', newline='')
    return fd


# 爬取网页数据
def get_page(url):
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
    }
    response = requests.get(url, headers=header).text
    return response


# 解析网页源代码
def parse_page(response):
    titles = []
    links = []
    html = BeautifulSoup(response, "html.parser")
    content = html.select('.card_sub_box > a')
    for item in content:
        titles.append(item.text)
        links.append(item.get('href'))
    data = zip(titles, links)
    return data


# 将爬取到的数据保存到文件中
def save(fm, fd, data):
    if fm == 'txt':
        for item in data:
            fd.write(item[0] + "," + item[1] + '\n')

    if fm == 'json':
        b = []
        # 作为字典的key
        temp = ('title', 'link')
        for item in data:
            # 将数据转成字符串并写入到文件中
            b.append(dict(zip(temp, item)))
        json.dump(b, fd, ensure_ascii=False, indent=2)

    if fm == "csv":
        csv_fm = csv.writer(fd)
        csv_fm.writerow(["title", "link"])
        for item in data:
            csv_fm.writerow(item)


# 开始爬取数据
def crawl():
    url = "https://duomoyu.com/"
    response = get_page(url)
    data = parse_page(response)
    fm = input("请输入文件保存格式（txt、json、csv）：")
    while fm != "txt" and fm != "csv" and fm != "json":
        fm = input("输入有误请重新输入文件保存格式（txt、json、csv）：")
    fd = open_file(fm)
    save(fm, fd, data)


if __name__ == '__main__':
    crawl()
