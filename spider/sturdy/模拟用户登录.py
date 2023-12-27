# @作者 : 叶枫
# @文件 : 模拟用户登录.py 
# @时间 : 2021/10/25 10:56
# @版本 ：1.0
# @功能描述:
import requests
session = requests.session()
data = {
    "loginName": "18614075987",
    "password": "q6035945"
}
url = "https://passport.17k.com/ck/user/login"
resp = session.post(url, data=data)

resp = session.get("https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919")
content = resp.json()
print(content['data'])

