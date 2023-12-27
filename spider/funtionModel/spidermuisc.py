#!/usr/bin/python3
# *_*coding:utf8 *_*
# @Time : 2020/10/19 20:48
# @Author : XiaoFan
# @File : 酷我音乐VIP歌曲破解.py
"""
分析需求
1，确定目标网址
2，获取目标网址的所有数据
3，筛选我们想要的数据
4，下载歌曲保存
"""
import os

import requests    #模拟浏览器浏览网页  第三方库  工具包
singer = input("请输入歌手姓名：")
num = input("请输入你想下载的页数：")
#目标网址
url = f"https://www.kuwo.cn/api/www/search/searchMusicBykeyWord?key={singer}&pn={num}&rn=30&httpsStatus=1&reqId=0e333970-f90a-11ec-a02d-9b5117697bc1"
print(url)
#伪装一下  请求头
headers = {
    #代理信息  模拟浏览器
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
    #令牌  钥匙
    "csrf": "0G1J21RT96FN",
    #打开哪个门
    "Cookie": "kw_token=0G1J21RT96FN",
    #域名
    "Host": "www.kuwo.cn",
    #防盗链  从哪里来的
    "Referer": f"https://www.kuwo.cn/search/list?key=%E5%91%A8%E6%9D%B0%E4%BC%A6"
}
#模拟浏览器发送请求
response = requests.get(url, headers=headers).json()
print(response)
data = response["data"]["list"]

#print(data)
for i in data:
    rid = i["rid"]
    name = i["name"]
    print(rid,name)
    #新目标网址
    # new_url = f'https://www.kuwo.cn/api/v1/www/music/playUrl?mid={rid}&type=music&httpsStatus=1&reqId=5085a771-f902-11ec-8529-cdb133e96ad8'
    new_url = f'https://apis.jxcxin.cn/api/kuwo?id={rid}&type=json'
    # new_url = "https://kuwo.cn/url?format=mp3&rid=" + str(rid) + "&response=url&type=convert_url3&br=128kmp3&from=web&t=1604320123221&httpsStatus=1&reqId=f202c851-1d06-11eb-91ba-83cb90e3e81e"
    # #请求新网址
    res = requests.get(new_url).json()
    # print(res)
    #print(res["url"])
    #下载歌曲  最后一次请求
    r = requests.get(res["url"]).content
    #路径
    path = os.path.join(os.path.expanduser("~"), 'Desktop') + os.sep + name + ".mp3"
    #保存 文件操作 以二进制写入
    with open(path, "wb") as f:
        f.write(r)
        print("正在下载",name)
