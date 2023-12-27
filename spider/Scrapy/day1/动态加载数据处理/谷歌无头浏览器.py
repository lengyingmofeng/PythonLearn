# @作者 : 叶枫
# @文件 : 谷歌无头浏览器.py 
# @时间 : 2020/11/29 19:34 
# @版本 ：1.0
# @功能描述:
from selenium import webdriver
from time import sleep
# 实现无可视化界面
from selenium.webdriver.chrome.options import Options
# 实现规避检测
from selenium.webdriver import ChromeOptions

# 无头浏览器操作
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument("--disable-gpu")

# 实现规避检测
option = ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])

bro = webdriver.Chrome(executable_path=r'E:\爬虫\day1\动态加载数据处理\chromedriver.exe', chrome_options=chrome_options, option=option)

# 无可视化界面（无头浏览器） phantmJs
bro.get("https://www.baidu.com")
print(bro.page_source)
sleep(2)
bro.quit()
