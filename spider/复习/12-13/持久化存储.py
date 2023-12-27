# @作者 : 叶枫
# @文件 : 持久化存储.py
# @时间 : 2021/12/12 13:40
# @版本 ：1.0
# @功能描述:
import csv
import json

import pymysql
import requests
import re


def save_txt(html):
    html = json.loads(html)
    fp = open("疫情数据.txt", "w", encoding='utf-8')
    json.dump(html, fp, ensure_ascii=False, indent=2)


# 保存为csv文件
def save_csv(html):
    file = open("../../12-17/数据可视化/各省疫情统计表.csv", "w", encoding='utf-8', newline='')
    file_csv = csv.writer(file)
    file_csv.writerow(["area", "city", "confirmed", "died", "crued",
                       "confirmedRelative", "asymptomaticRelative", "asymptomatic",
                       "nativeRelative", "curConfirm"])

    html = json.loads(html)
    for index, i in enumerate(html['component'][0]['caseList']):
        area = i['area']  # 地区
        city = i['subList']
        if not city:  # city是一个空列表表示该地区没有疫情
            file_csv.writerow([area, "", "", "", "", "", "", "", "", ""])
        print(city)
        for j in city:
            #
            file_csv.writerow([area, j['city'], j['confirmed'], j['died'],
                               j['crued'], j['confirmedRelative'], j['asymptomaticRelative'],
                               j['asymptomatic'], j['nativeRelative'], j['curConfirm']])


# 保存为JSON文件
def save_json(html):
    # 把数据转换成json数据，让ASCII码显示成中文
    html = json.loads(html)
    print(html)
    with open("疫情数据.json", "w", encoding='utf-8') as fp:
        # ensure_ascii设置为False,中文将不会以为ASCII显示
        # indent -> 缩进, 如果为None则不换行不缩进
        json.dump(html, fp, ensure_ascii=False, indent=2)


def save_mysql(html):
    html = json.loads(html)
    conn = pymysql.Connect(
        host="localhost",
        user="root",
        password="123456",
        database="ruo",
        port=3306
    )
    cursor = conn.cursor()
    print(html)
    try:
        pk = 476
        # sql命令
        sql = 'insert into yq (area, city, confirmed, died, crued, confirmedRelative, asymptomaticRelative, asymptomatic, nativeRelative, curConfirm)' \
              'value(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        # sql = 'insert into yq value(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        for i in html['component'][0]['caseList']:
            area = i['area']  # 地区
            city = i['subList']
            if not city:  # city是一个空列表表示该地区没有疫情
                v = [area, None, None, None, None, None, None, None, None, None]
                cursor.execute(sql, v)
                conn.commit()
                pk += 1
            # 数据存储
            for j in city:
                v = [area, j['city'], j['confirmed'], j['died'], j['crued'], j['confirmedRelative'],
                     j['asymptomaticRelative'], j['asymptomatic'], j['nativeRelative'], j['curConfirm']]
                print(v)
                cursor.execute(sql, v)
                conn.commit()
                pk += 1
    # 出现异常数据回滚
    except Exception as e:
        print(e)
        conn.rollback()


if __name__ == '__main__':
    url = "https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=osari_aladin_banner"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36',
    }
    response = requests.get(url, headers=headers).text
    # 使用正则匹配到我们想要的数据
    obj = re.compile('id="captain-config">(?P<page>.*?)</script>')
    # 按照我们compile里设置的page进行分组
    html = obj.search(response).group("page")
    save_csv(html)
    # save_mysql(html)
    # save_json(html)
    # save_txt(html)
