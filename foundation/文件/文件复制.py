# @作者 : 叶枫
# @文件 : 文件复制.py 
# @时间 : 2020/10/17 19:10 
# @版本 ：1.0
# @功能描述:
import os
import shutil

# file_list = []
# def search_file(path):
#     # 切换当前目录为指定路径
#     os.chdir(path)
#     # 定义需要查找的文件类型
#     search_list = [".md"]
#     # 列举当前目录下的文件名
#     allFile = os.listdir(os.curdir)
#     # 遍历所有文件名
#     for i in allFile:
#         # 用于分离文件名和扩展名，返回（name,extension)元组，此处只返回扩展名
#         extension = os.path.splitext(i)[1]
#         if extension in search_list:
#             # getcwd()获取当前工作目录；sep输出文件的路径分隔符；linesep是换行
#             file_list.append(os.getcwd()+os.sep + i+os.linesep)
#         # 判断指定路径i存在并且是一个目录
#         elif os.path.isdir(i):
#             # 递归调用
#             search_file(i)
#             # 递归调用后返回上一层目录
#             os.chdir(os.pardir)
# search_file("F:/笔记/")
# print(file_list)


# 复制所有文件
# def copy_allfiles(src, dest):
#     # src:原文件夹；dest:目标文件夹
#     src_files = os.listdir(src)                                 # 得到原文件的名称
#     print(src_files)
#     for file_name in src_files:                                 # 遍历该文件的目录
#         full_file_name = os.path.join(src, file_name)           # 文件目录进行拼接
#         if os.path.isfile(full_file_name):                      # 判断文件是否是个文件
#             shutil.copy(full_file_name, dest)                   # 复制dest目录中
#     print("复制成功")
# #
# src = "E:/a"
# dest = "E:/b"
# copy_allfiles(src, dest)


def copy(old_file, new_file):
    # 判断是否为目录
    if os.path.isdir(old_file) and os.path.isdir(new_file):
        # 获取改old_file下的文件
        list1 = os.listdir(old_file)
        for i in list1:
            # 将需要读取的目录与文件名进行拼接
            path1 = os.path.join(old_file, i)
            # 将需要写入的目录与文件名进行拼接
            path2 = os.path.join(new_file, i)
            # 判断读取目录是否为一个目录
            if os.path.isdir(path1):
                # 在写入文件夹下创建一个目录
                os.mkdir(path2)
                # 递归调用
                copy(path1, path2)

            else:
                # 打开读取文件
                with open(path1, 'rb') as stream:
                    # 读取内容
                    con = stream.read()
                    # 打开写入文件
                    with open(path2, 'wb') as writing:
                        # 写入文件内容
                        writing.write(con)
    else:
        print('目录错误！')


# 复制文件夹
old_path = r'E:\古诗\a'
new_path = r'E:\古诗\b'
copy(old_path, new_path)