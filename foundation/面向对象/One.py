# @作者 : 叶枫
# @文件 : One.py 
# @时间 : 2020/10/17 18:32 
# @版本 ：1.0
# @功能描述:
class Dog:
    def __init__(self, foot, weight, height):
        self.foot = foot
        self.weight = weight
        self.height = height


if __name__ == '__main__':
    dog = Dog(4, 14, 30)
    print(" foot属性值为：", dog.foot, "\n", "weight属性值为：", dog.weight, "kg\n", "height属性值为：", dog.height, "cm")
