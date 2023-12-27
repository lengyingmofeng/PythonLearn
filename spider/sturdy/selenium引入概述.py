# @作者 : 叶枫
# @文件 : selenium引入概述.py 
# @时间 : 2021/10/27 16:57
# @版本 ：1.0
# @功能描述:
# from selenium.webdriver import Chrome, Keys
#
# # 创建一个浏览器对象
# web = Chrome()
# web.get("https://www.baidu.com")  # 打开浏览器
# web.find_element('xpath', '//*[@id="kw"]').send_keys("哔哩哔哩", Keys.ENTER)


from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time

web = Chrome()

web.get("http://lagou.com")
btn = web.find_element('xpath', '//*[@id="changeCityBox"]/ul/li[1]/a')  # 找到全国按钮
btn.click()  # 点击这个按钮
time.sleep(1)  # 让浏览器反应⼀会⼉
# 找到⽂本框输⼊python, 点击搜索按钮
web.find_element('xpath', '//*[@id="search_input"]').send_keys("python", Keys.ENTER)
# web.find_element_by_xpath('//*[@id="search_button"]').click()
ls = web.find_elements('xpath', '//*[@id="s_position_list"]/ul/li')  # ⼀次性提取多个元素⽤elements
for item in ls:
    name = item.find_element('xpath', './div[1]/div[1]/div[1]/a/h3').text
    addr = item.find_element('xpath', './div[1]/div[2]/div[1]/a').text
    price = item.find_element('xpath', './div[1]/div[1]/div[2]/div/span').text
    experience = item.find_element('xpath', './div[1]/div[1]/div[2]/div').text
    print(name, addr, price, experience)
    # 其他内容你⾃⼰琢磨吧
# web.close()