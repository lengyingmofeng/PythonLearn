# @作者 : 叶枫
# @文件 : re模块.py 
# @时间 : 2021/10/13 11:33
# @版本 ：1.0
# @功能描述:

# findall
import re
import urllib.request

import requests

requests.Request()

# lst = re.findall("c", "this is a books")
# print(lst)
#
lst = re.findall(r"\d+", "9点之前，你要给我发9000块钱\n12313iadkaldjklaljvzn\d\t")
print(lst)

ret = re.search(r"\w+", "5点之前，给我5000").group()
print(ret)
#
# it = re.finditer("m", "mai le fo len, mai ni mei!")
# for item in it:
#     print(item.group())

# obj = re.compile(r"\d{3}")
# ret = obj.search("abcd123egddads")
# print(ret.group())

s = "<div class='jay'><span id='10010'>中国联通</span></div>"

# obj = re.compile(r"<span id='(?P<id>\d+)'>(?P<name>\w+)</span>", re.S)
# result = obj.search(s)
# print(result.group("name"))

obj = re.compile(r"\d{3}")
ret = obj.findall("abcd123egddads")
print(ret)