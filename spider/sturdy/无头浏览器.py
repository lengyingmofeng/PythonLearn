# @作者 : 叶枫
# @文件 : 无头浏览器.py 
# @时间 : 2021/10/28 16:03
# @版本 ：1.0
# @功能描述:
from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
import time
web = Chrome()
web.get('https://www.endata.com.cn/BoxOffice/BO/Year/index.html')