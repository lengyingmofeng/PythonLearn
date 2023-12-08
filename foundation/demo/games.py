import random

times = 1  # 回合
distance = random.randint(6, 12)     # 距离
thief, police = 0, 0    # 小偷和警察
row = 0     # 步数
print('------------------小游戏------------------')
print("1.小偷， 2.警察， 请选择：")
role = eval(input())
while True:
    if role == 1:
        print("你选择的是小偷，你选择与警察的距离为", distance, "格")
        thief = distance
        break
    elif role == 2:
        print("你选择的是警察，你选择与小偷的距离为", distance, "格")
        thief = distance
        break
    else:
        role = eval(input("你输入的有误请重新输入"))
print("------------------游戏开始------------------")
while times <= 10:  # 回合次数
    row = 0  # 步数
    print("{}{}{}".format("---------------当前回合为", times, "-----------------"))
    die = eval(input("按数字1掷骰:"))
    while die != 1:
        die = eval(input("输入有误，请重新输入"))
    tel = random.randint(1, 6)  # 生成骰子的数值
    k = 0               # 存放骰子为6的次数
    while tel == 6:     # 如果掷骰为6
        row += tel      # 给步数加上
        if k == 2:      # 是否投了两次6
            k = 0
            row += random.randint(1, 5)
            break
        tel = random.randint(1, 6)  # 则在投一次
        row += tel
        k += 1
    row += tel
    if role == 1:   # 判断你选择的角色
        thief += row
        police += 3
        print("警察前进了3格", "小偷前进了", row, "格 两人之间的距离为", thief - police)
    else:
        thief += 2
        police += row
        print("警察前进了", row, "格" "小偷前进了2格 两人之间的距离为", thief - police)
    if police >= thief:  # 判断警察的步数是否大于小偷的步数，如果大于则说明小偷被抓
        if role == 1:   # 再次判断你的角色
            print("很不幸你被警察抓住")
            break
        else:
            print("恭喜你成功抓住小偷")
            break
    times += 1

print("------------------游戏结束------------------")
if role == 1:
    print("------------恭喜你没有被警察抓到--------------")