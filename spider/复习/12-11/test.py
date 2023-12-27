# @作者 : 叶枫
# @文件 : test.py 
# @时间 : 2021/12/11 21:37
# @版本 ：1.0
# @功能描述:

# a = [{"sex": "男", "age": 20}, {"sex": "女", "age": 16}]
#
# for i in a:
#     i['name'] = "tom"
# print(a)


s = "1234567890s"
if len(s) != 11 or not s.isdigit():
    print("密码有误")
    exit(0)
print(s)