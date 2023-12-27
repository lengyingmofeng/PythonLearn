import os


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