# -*- coding: utf-8 -*- 
# @Time : 2020/10/9 20:24 
# @Author : kzl 
# @File : 后宫项目.py
def add(name):
    list2_k = 0  # 妃子是否存在
    for i in range(len(list1)):
        if name != list1[i]:  # 判断妃子名字是否存在
            list2_k = 1
        else:
            print("妃子发现自己的称号和其她妃子称号一样，一气之下表示不嫁了")
            list2_k = 0
            break
    if list2_k == 1:  # 添加妃子
        list1.append(name)
        love.append(100)
        level.append(0)
        for i in range(len(list1) - 1):  # 妃子们的好感度减10
            love[i] -= 10
        Level()
        print("{:10}{:10}{}".format("姓名", "等级", "好感度"))
        for i in range(len(list1)):
            print("{:10}{:10}{:5}".format(list1[i], list2[level[i]], love[i]))


def Play(name):
    look = 0
    for i in range(len(list1)):                 # 查找妃子
        if name == list1[i]:                    # 找到妃子好感度+10
            love[i] += 10
            look = 1
    if look == 0:
        print("皇上真是失误繁忙呀！妃子的名字都记错了")
    else:
        for j in range(len(list1)):                     # 其他妃子好感度-10
            if name != list1[j]:
                love[j] -= 10
        Level()
        print("{:10}{:10}{}".format("姓名", "等级", "好感度"))
        for i in range(len(list1)):
            print("{:10}{:10}{:5}".format(list1[i], list2[level[i]], love[i]))


def dels(name):
    index = 0
    list1_index = 0
    for i in range(len(list1)):
        if name == list1[i]:
            index = i
            list1_index = 1
    if list1_index == 1:
        list1.pop(index)
        love.pop(index)
        for j in range(len(list1)):
            love[j] += 10
        Level()
        print("{:10}{:10}{}".format("姓名", "等级", "好感度"))
        for i in range(len(list1)):
            print("{:10}{:10}{:5}".format(list1[i], list2[level[i]], love[i]))
    else:
        print("虚惊一场，没有该妃子的名称")


def LovePlus(name):
    love_plus = 0
    for i in range(len(list1)):
        if name == list1[i]:
            love[i] += 20
            love_plus = 1
    if love_plus == 1:
        for j in range(len(list1)):
            if name not in list1[j]:
                love[j] -= 10
        Level()
        print("{:10}{:10}{}".format("姓名", "等级", "好感度"))
        for i in range(len(list1)):
            print("{:10}{:10}{:5}".format(list1[i], list2[level[i]], love[i]))
    else:
        print("妃子的名称不存在")


def Level():
    for i in range(len(love)):
        if love[i] > 130:
            level[i] = 1
        elif love[i] > 150:
            level[i] = 2
        elif love[i] > 170:
            level[i] = 3
        elif love[i] > 200:
            level[i] = 4
# def End():
#     for i in range(len(list1)):
#         if

list1 = ["欧阳", "叶枫", "张伟", "小兰"]  # 后宫妃子
list2 = ["夫人", "贵宾", "贵妃", "皇贵妃", "皇后"]  # 关系程度
love = [100, 100, 100, 100]  # 好感度
level = [0, 0, 0, 0]  # 等级
day = 1
print("{:-^72}".format("欢迎来到后宫"))
while day < 7:
    print("{:->36}{}{:-<37}".format("第", day, "天"))
    print("{}\n{}\n{}\n{}".format("1.迎娶新的妃子", "2.看望妃子", "3.将妃子打入冷宫", "4.今天你要独宠哪位妃子"))
    chooei = eval(input("请选择："))
    if chooei == 1:
        name = input("迎娶新的妃子的称号封为:")
        add(name)
    elif chooei == 2:
        name = input("你要去见哪位妃子：")
        Play(name)
    elif chooei == 3:
        name = input("你要将哪位妃子打入冷宫:")
        dels(name)
    elif chooei == 4:
        name = input("你要独宠哪位妃子:")
        LovePlus(name)
    else:
        print("你的输入有误请重新输入")
    day += 1
