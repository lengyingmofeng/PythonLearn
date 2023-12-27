# # @作者 : 叶枫
# # @文件 : num5.py
# # @时间 : 2021/12/17 9:46
# # @版本 ：1.0
# # @功能描述:
# import sys
#
import sys
import requests
from bs4 import BeautifulSoup
url = "http://www.lvyun188.com/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36',
}
response = requests.get(url, headers=headers).text
html = BeautifulSoup(response, "html.parser")
content_list = html.select(".entry__text")
# 换成迭代器
it = iter(content_list)
while True:
    try:
        # 获取下一个迭代对象
        i = next(it)
        # 获取标题名称
        title = i.find('h1', class_="entry__title").a.text
        print(title)
        # 获取作者
        author = i.find('div', class_="entry__date").a.text
        print(author)
        # 获取内容
        content = i.find('div', class_="entry__excerpt").p.text
        print(content)
        # 将爬取到内容存储到E:/古诗/文件下以标题作为文件名后缀为txt
        with open("E:/古诗/" + title + '.txt', "w", encoding='utf-8') as fp:
            fp.write(title + '\n' + author + '\n' + content)
    except Exception:
        sys.exit()

