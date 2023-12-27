# @作者 : 叶枫
# @文件 : cookeis.py 
# @时间 : 2020/11/22 17:01 
# @版本 ：1.0
# @功能描述:
import requests

temp = 'username= tangxi;password=123456'

cookies_list = temp.split(';')
print(cookies_list)
cookies = {}
for cookie in cookies_list:
    cookie_key = cookie.split("=")[0]
    cookie_value = cookie.split('=')[-1]
    cookies[cookie_key] = cookie_value
print(cookies)
print(cookies['username'])