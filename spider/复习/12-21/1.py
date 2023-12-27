import json
import re
from urllib import request

import demjson
from lxml import etree
import pandas as pd
import numpy as np
import requests

url = "https://cs.anjuke.com/sale/"
# headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
    "cookie": "ctid=27; aQQ_ajkguid=E88C7D36-6C34-4232-A448-E9DF5C9C758C; sessid=0B254BB0-3AAE-408F-9FD1-8C55ABEF683E; fzq_h=925c48af33f8b24ba98fc2184915a04d_1640141844969_f9fd9780dd104badb7d9a30b2cbe262e_3740328732; twe=2; id58=CrIH0GHClBZ5r0wZecYTAg==; _ga=GA1.2.1241715007.1640141846; _gid=GA1.2.112542584.1640141846; 58tj_uuid=e35534c4-1e29-4799-a6f5-3b5db70c5c9a; init_refer=; new_uv=1; new_session=0; als=0; fzq_js_anjuke_ershoufang_pc=d4deda20077edf92886baab5909f2752_1640142235353_24; obtain_by=2; xxzl_cid=07622a91599e48baa8656ca5d51fc4a1; xzuid=2097b4e6-e7d4-4572-a157-2fd2dd3d4561"
           }
# response = request.Request(url, headers=headers)
# r = request.urlopen(response)
# h = r.read().decode("utf-8")

response = requests.get(url=url, headers=headers)
response.encoding = 'utf-8'
h = response.text
# html = etree.HTML(h)
obj = re.compile(r"has_more:c,list:(.*?),categories")
data = re.findall(obj, h)[0].replace('\\', '')
print(data)
data = data.replace('c', '1433')
q = demjson.decode(data)
for i in q:
    print(type(q))
# for i in data:
#     print(i)
# # 爬取字段：图片url、房源标题、房屋面积、朝向、建房时间、地址、单价
# data_list = {}
# img_src = html.xpath("//div[@class='property']/a/div[1]/img[@class='lazy-img cover']/@data-src")
# title_list = html.xpath("//div[@class='property']/a/div[2]/div[1]/div[1]/h3/@title")
# area_list = html.xpath("//div[@class='property']/a/div[2]/div[1]/section/div[1]/p[2]/text()")
# toward_list = html.xpath("//div[@class='property']/a/div[2]/div[1]/section/div[1]/p[3]/text()")
# time_list = html.xpath("//div[@class='property']/a/div[2]/div[1]/section/div[1]/p[5]/text()")
# address_list = html.xpath("//div[@class='property']/a/div[2]/div[1]/section/div[2]/p[2]/span[3]/text()")
# price_list = html.xpath("//div[@class='property']/a/div[2]/div[2]/p[2]/text()")
#
#
# # data_list["图片路径"] = img_src
# data_list["房源标题"] = [str(i).strip() for i in title_list]
# data_list["房屋面积"] = [str(i).strip() for i in area_list]
# data_list["朝向"] = toward_list
# data_list["建房时间"] = [str(i).strip() for i in time_list]
# data_list["建房时间"] = address_list
# data_list["单价"] = price_list
# # print(data_list)
# data = pd.DataFrame(data_list)
# print(data.to_string())
