# # @作者 : 叶枫
# # @文件 : 肯德基.py
# # @时间 : 2020/11/27 19:42
# # @版本 ：1.0
# # @功能描述:
# import json
#
# import requests
# url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op='
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0'
# }
# data = {
#     'cname': '',
#     'pid': '',
#     'keyword': '湖南',
#     'pageIndex': '1',
#     'pageSize': '10'
# }
# response = requests.post(url, data=data, headers=headers)
# print(response.text)
# response.encoding = "utf8"
# with open("肯德基.html", "wb") as fp:
#     fp.write(response.content)
import json

data = 'dr1666619586766({"result":1,"aolno":10267,"m46":0,"v46ip":"172.220.10.151","myv6ip":"","sms":0,"ufee":0,"NID":"蒋文艳","olno":1,"udate":"","olmac":"fe0387e10273","ollm":0,"olm1":"00000000","olm2":"0000","olm3":0,"olmm":2,"olm5":0,"gid":8,"olno":1,"olip":"172.220.42.123","oaf":109842,"oat":3842,"mac1":"","mac2":"9ce65ec06299","mac3":"fe0387e10273","mac4":"","mac5":"","mac6":"","ac0":"MTAzMjU=","oltime":4294967295,"olflow":4294967295,"lip":"172.220.10.151","stime":"2022-10-24 21:52:42","etime":"2022-10-24 21:53:08","uid":"10325","sv":0})'
print(len("dr1666619586766("))
print(json.loads(data[16:-1]))

蒋文艳
10325
卢彬
10363