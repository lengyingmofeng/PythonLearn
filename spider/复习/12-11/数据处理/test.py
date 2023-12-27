# @作者 : 叶枫
# @文件 : test.py 
# @时间 : 2021/12/11 15:33
# @版本 ：1.0
# @功能描述:
import os.path

file_list = []

def seach(path):
    find_list = ['.jpg', '.png', '.mp4', '.mp3']
    os.chdir(path)
    file = os.listdir(os.curdir)
    for i in file:
        suffix = os.path.splitext(i)[1]
        if suffix in find_list:
            file_list.append(os.getcwd() + os.sep + i + os.linesep)
        elif os.path.isdir(i):
            seach(i)
            os.chdir(os.pardir)

path = r"E:\imgs"
# seach(path)
# print(file_list)


os.chdir(path)
file = os.listdir(os.curdir)
for i in file:
    print(i)
    print(os.path.isdir(i))
    print(os.path.isfile(i))
# s = 123
# if s in int:
#     print(s)