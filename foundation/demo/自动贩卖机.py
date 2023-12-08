m = ['1', '5', '10']
pay = 0
money = 0
while True:
    choose = input("请选择您需要的物品：1:泡面 2:矿泉水 3:饼干 4:辣条,5可乐，按Q退出\n请选择：")
    if choose in items.keys():
        money = money + float(items[choose])
        break
    elif choose == "Q":
        print("退出饮料选择")
        break
    else:
        print("输入错误")
while True:
    pay = input("请选择面值是 1/5/10的纸币或硬币进行购买\n请重新输入：")
    if pay in m:
        pay = int(pay)
        if pay == money:
            print("投入的金额正好")
            break
        if pay > money:
            print("你购买了{}元的商品,已投币{}，还找零{}".format(money, pay, pay - money))
            break
        if pay < money:
            print("你购买了{}元的商品，已投币{}，还需投币{}".format(money, pay, money - pay))
            pay2th = money - pay
            while True:
                pay = input("请继续投币，请选择面值是 1/5/10的纸币或硬币进行购买\n请输入：")
                if pay in m:
                    pay = int(pay)
                    if pay == pay2th:
                        print("投入的金额正好")
                        break
                    if pay > pay2th:
                        print("已投币{}，还找零{}".format(pay, pay - pay2th))
                        break
                    if pay < pay2th:
                        pay2th = pay2th - pay
                        print("已投币{}，还需投币{}".format(pay, pay2th))
                        continue
                else:
                    print("输入错误")
            break
    else:
        print("请重新输入")
