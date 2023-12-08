# @作者 : 叶枫
# @文件 : 密码加密.py 
# @时间 : 2020/10/14 20:35 
# @版本 ：1.0
# @功能描述:

password = input("密码加密：")
password = password.upper()
password = list(password)
list1 = []
for i in range(len(password)):
    if password[i] == " ":
        list1.append(password[i])
    elif ord(password[i]) <= 90 - 3:
        list1.append(chr(ord(password[i]) + 3))
        result = ''.join(list1)
    else:
        list1.append(chr(ord(password[i]) - 23))
        result = ''.join(list1)
print(result)
