# @作者 : 叶枫
# @文件 : QQ空间登录.py 
# @时间 : 2020/11/29 19:23 
# @版本 ：1.0
# @功能描述:
from selenium import webdriver
from time import sleep
bro = webdriver.Chrome(executable_path=r'E:\爬虫\day1\动态加载数据处理\chromedriver.exe')
bro.get('https://i.qq.com/')
bro.switch_to.frame('login_frame')
a_tag = bro.find_element_by_id("switcher_plogin")
a_tag.click()

username = bro.find_element_by_id('u')
password = bro.find_element_by_id('p')
sleep(2)
username.send_keys("1797719651")
sleep(2)
password.send_keys("010514s+")

btm = bro.find_element_by_id("login_button")
btm.click()

sleep(3)

bro.quit()

