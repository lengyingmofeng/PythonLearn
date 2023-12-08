import random

times = 5  # 五次方法
secret = random.randint(1, 20)  # 生成一个1~20的数字
print('------------------小游戏------------------')
guess = 0  # 输入要猜的数字
print("不妨猜一下我现在心里想的是哪个数字\n赢了今晚带你去看电影哦：")
while (guess != secret) and (times > 0):  # 如果你输入的数字不等于猜的数字和次数大于0次将继续执行
    temp = input()
    while not temp.isdigit():  # 判读是不是一个正整数
        temp = input("让你输入一个整数，干嘛呢，重来：\n")
    guess = int(temp)
    times = times - 1
    if guess == secret:  # 你输入的数字等于随机生成的数字,游戏结束
        print("哇好棒啊~ 竟然猜对了")
        print("好吧，看在你浪费了这么多努力的份上，晚上加一份米线吧！")
        break
    else:  # 否则判读是大还是小
        if guess > secret:  # 如果你输入的数大于随机生成的数字
            print("哥哥, 大了大了~~~")
        else:  # 小的则打印下面这句
            print("嘿，小了，小了~~~")
    if times > 0:  # 判断次数
        print("再给你一次机会吧: ")
        if times == 1:  # 如果你次数只有一次将提示
            print("这是最后一次机会了啊！")
    else:  # 次数用完没有猜中打印一下两句话
        print("美梦泡汤啦")
        print("游戏结束，不玩啦^_^")
