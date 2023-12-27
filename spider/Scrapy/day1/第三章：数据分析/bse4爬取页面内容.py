# @作者 : 叶枫
# @文件 : bse4爬取页面内容.py 
# @时间 : 2020/11/28 16:58 
# @版本 ：1.0
# @功能描述:
import requests
from bs4 import BeautifulSoup

url = 'https://www.shicimingju.com/book/sanguoyanyi.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
}
page_text = requests.get(url=url, headers=headers)
page_text.encoding = 'UTF-8'
page_text = page_text.text
soup = BeautifulSoup(page_text, 'lxml')
li_list = soup.select(".book-mulu > ul > li")
print(len(li_list))

fp = open('三国.text', "w", encoding="utf-8")
for li in li_list:
    title = li.a.text
    detail_url = "https://www.shicimingju.com" + li.a['href']
    detail_url_text = requests.get(detail_url, headers=headers)
    detail_url_text.encoding = "utf-8"
    detail_url_text = detail_url_text.text
    detail_soup = BeautifulSoup(detail_url_text, 'lxml')
    # 找到div中带有class=chapter_content类的标签
    div_tag = detail_soup.find('div', class_='chapter_content')
    content = div_tag.text  # 取出div_tag里面的所有文字
    fp.write(title + ":" + content + '\n')
    print(title, "爬取成功")
