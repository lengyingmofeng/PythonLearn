# @作者 : 叶枫
# @文件 : 动作和iframe的处理.py 
# @时间 : 2020/11/29 19:06 
# @版本 ：1.0
# @功能描述:
from selenium import webdriver
from selenium.webdriver import ActionChains
from  time import sleep
bro = webdriver.Chrome(executable_path=r'E:\爬虫\day1\动态加载数据处理\chromedriver.exe')
bro.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
bro.switch_to.frame("iframeResult")
div = bro.find_element_by_id("draggable")

action = ActionChains(bro)
# 点击长安指定的标签
action.click_and_hold(div)
for i in range(5):
    # perform立即执行动作操作链操作
    action.move_by_offset(17, 0).perform()
    sleep(0.3)
# 动作释放
action.release()
print(div)
quit()