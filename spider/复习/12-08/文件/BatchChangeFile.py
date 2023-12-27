# @作者 : 叶枫
# @文件 : BatchChangeFile.py
# @时间 : 2021/12/8 9:44
# @版本 ：1.0
# @功能描述: 批量更改文件名
import os
import random
import string
# 要更改文件路径
path = r"E:\imgs\2021-12-8"
# 使用列表推导式将26个大小写字母添加到s列表中
s = [i for i in string.ascii_letters]
os.chdir(path)
# 获取该目录下的所有文件
fileList = os.listdir()
for i in fileList:
    # 随机生成0~100的数字
    num = random.randint(0, 100)
    # 获取文件的扩展名
    sub_file = i.split(".")[1]
    # 旧文件名
    old_name = i
    # 防止文件名重复，添加几个随机字符串和随机数字
    new_name = "yefeng-" + s[random.randint(0, 51)] + str(num) + s[random.randint(0, 51)] + os.curdir + sub_file
    # 更改文件名称
    os.rename(old_name, new_name)
    print(old_name, "->", new_name)

