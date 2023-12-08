# @作者 : 叶枫
# @文件 : 定义创建类.py 
# @时间 : 2020/10/12 19:25 
# @版本 ：1.0
class Weapon:
    """
    武器类
    """
    def __init__(self, name="默认武器", intro="这家伙很懒，什么描述都没有", power=1, type ="默认类型"):
        self.name = name
        self.intro = intro
        self.power = power
        self.type = type

    def show(self):
        formatter = " 名称：{}\n 说明：{}\n 威力：{}\n 类型：{}\n"
        print(formatter.format(self.name, self.intro, self.power * "★" + (5 - self.power) * "☆", self.type))


if __name__ == '__main__':
    weapon = Weapon("电刀", "从天而降的刀法", 5, "非常腻害")
    weapon.show()
