import pyautogui
import pyperclip
import time
import random

# text = ["祖安大舞台 有妈你就来", "天工造物不测，怎么造出你这么个东西",
#         "扔块肉在屏幕上，狗都比你会连招",
#         "你脑子进水了吧，还是100°的那种沸水",
#         "我终于知道你是一个什么怪物了，原来你是臭水沟里老鼠蜕变的呀，难怪浑身臭气熏天呢！"
#         "别在卖萌嘟嘴剪到手了，都是被人叫做叔叔阿姨的人了",
#         "其实我挺佩服你的，能长成这样，你长的比芙蓉姐还恶心，比凤姐还销魂。"]  # 注意我这里只定义了一点喷人的话，你想的话可以自己在这个列表里面加入，到时候程序会自动在这个text列表中选择然后发送。
# user = ["@Captain Paxton", "@K", "@Mortal"]
# print("提示：输入完回车继续--")
# # num = int(input("请输入次数：\n"))  # 定义要骂多少句
# # times = eval(input("请输入间隔时间，默认秒，可输入小数：\n"))  # 定义每一句发送的时间间隔
# num = 30
# times = 5
# print("请在3秒内切回输入框")  # 注意在使用时，运行到这句之后马上切回到要骂人的地方，然后点击一下输入框，程序就会自动开始执行。记得要点击一下输入框
# for i in range(3, 0, -1):
#     print("\r倒计时{}秒！\n".format(i), end="")
#     time.sleep(1)
# print('程序开始...')
# for i in range(num):
#     msg = random.choice(user)
#     msg += random.choice(text)
#     pyperclip.copy(msg)
#     pyautogui.hotkey('ctrl', 'v')
#     pyautogui.typewrite(['enter'], times)
#


import itchat

@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    return "Hello"

itchat.auto_login()
itchat.run()

