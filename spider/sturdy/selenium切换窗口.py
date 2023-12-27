# @作者 : 叶枫
# @文件 : selenium切换窗口.py
# @时间 : 2021/10/28 15:34
# @版本 ：1.0
# @功能描述:
from selenium.webdriver import Chrome, Keys

web = Chrome()
web.get("http://lagou.com")
btn = web.find_element('xpath', '//*[@id="changeCityBox"]/ul/li[1]/a')  # 找到全国按钮
btn.click()  # 点击这个按钮
web.find_element('xpath', '//*[@id="search_input"]').send_keys("python", Keys.ENTER)
# 点击a标签进入详情页
web.find_element('xpath', '//*[@id="s_position_list"]/ul/li[1]/div[1]/div[1]/div[1]/a/h3').click()
# 切换浏览器窗口， 跳转到最后一个窗口
web.switch_to.window(web.window_handles[-1])
demand = web.find_element('xpath', '//*[@id="job_detail"]/dd[2]/div').text
print(demand)
# web.close()  # 关闭窗口
# 切换到原来窗口
# web.switch_to.window(web.window_handles[0])

# web = Chrome()
# web.get("https://www.91kanju.com/vod-play/541-2-1.html")
# # 找到那个iframe
# iframe = web.find_element_by_xpath('//*[@id="player_iframe"]')
# web.switch_to.frame(iframe)
# val = web.find_element_by_xpath('/html/body/div[4]').get_attribute("value")
# print(val)

