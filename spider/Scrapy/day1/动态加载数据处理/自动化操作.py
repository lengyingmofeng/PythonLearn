# @作者 : 叶枫
# @文件 : 自动化操作.py 
# @时间 : 2020/11/29 16:45 
# @版本 ：1.0
# @功能描述:
from selenium import webdriver
from time import sleep
bro = webdriver.Chrome(executable_path=r'E:\爬虫\day1\动态加载数据处理\chromedriver.exe')
bro.get("https://www.taobao.com/")
# 标签定位
search = bro.find_element_by_id("q")
# 标签交互
search.send_keys("小米")
# 执行一组js程序
bro.execute_script('window.scrollTo(0, document.body.scrollHeight)')
sleep(5)
# 点击搜索按钮
btm = bro.find_element_by_css_selector('.btn-search')
btm.click()
sleep(5)
bro.get("https://www.baidu"
        ".com/")
bro.back()              # 前进
sleep(3)
bro.forward()           # 后退
sleep(3)
bro.quit()