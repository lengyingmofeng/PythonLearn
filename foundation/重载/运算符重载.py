# @作者 : 叶枫
# @文件 : 运算符重载.py 
# @时间 : 2020/10/14 16:17 
# @版本 ：1.0


class MyInteger:
    """
    创建一个自定义的整数类型
    """
    def __init__(self, data=0):
        # 如果传入的参数是整数类型，那么直接赋值
        # 如果传入的参数不是整数类型，就判断能否转化成整数，不能转换赋值初值为0
        self.data = 0
        if isinstance(data, int):
            self.data = data
        elif isinstance(data, str) and data.isdecimal():
            self.data = int(data)

    def __add__(self, other):
        # 返回当前对象的副本
        return MyInteger(self.data + other.data)

    def __str__(self):
        return str(self.data)

    def __sub__(self, other):
        return MyInteger(self.data - other.data)


if __name__ == '__main__':
    num1 = MyInteger("abcd")
    num2 = MyInteger(4321)
    num3 = num1 + num2
    num4 = num2 - num1
    print(num3)
    print("num4 = ", num4)
