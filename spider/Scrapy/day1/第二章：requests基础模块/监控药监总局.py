# @作者 : 叶枫
# @文件 : 监控药监总局.py
# @时间 : 2020/11/27 20:36
# @版本 ：1.0
# @功能描述:
# http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById
import json

import requests
import time
times = time.time()
id_dic = []  # 用来存储药店id
str = []  # 用来存储药店所有数据
url = "http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0'
}
for page in range(1, 361):
    data = {
        'on': 'true',
        'page': 'page',
        'pageSize': '15',
        'productName': '',
        'conditionType': '1',
        'applyname': '',
        'applysn': ''
    }
    response = requests.post(url, data, headers=headers).json()
    for dic in response['list']:
        id_dic.append(dic['ID'])      # 存储药店id
    print(id_dic)
url_id = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
for id in id_dic:
    data = {
     'id': id
    }
    response = requests.post(url_id, data, headers=headers).json()
    str.append(response)
    print(response)
fp = open("药店信息.html", "w", encoding="utf8")
json.dump(str, fp, ensure_ascii=False)

k = time.time() - times

print("一个共用了", k, "秒")
