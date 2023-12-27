# @作者 : 叶枫
# @文件 : bse4基础.py
# @时间 : 2020/11/28 16:14 
# @版本 ：1.0
# @功能描述:
from bs4 import BeautifulSoup
# 将本地的HTML文件中的数据加载到该对象中
fp = open('../瞎玩/bilibli.html', "r", encoding='utf8')
soup = BeautifulSoup(fp, 'lxml')
# print(soup.div)           # 找出HTML中的第一个div
# print(soup.find("a"))       # 等同于soup.div
# print(soup.find_all("a"))   # 找出HTML中的所有a标签
# print(soup.find("div", class_="wrapper_l wrapper_new"))     # 找出HTMLdiv中的带有class类的
# print(soup.select("#primaryPageTab"))        # 某种选择器（id, class 标签...选择器），返回一个列表
print(soup.select("."))

