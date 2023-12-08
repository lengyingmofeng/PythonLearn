# @作者 : 叶枫
# @文件 : 画圆.py 
# @时间 : 2020/10/12 20:06 
# @版本 ：1.0
import math
import turtle


class Circle:
    def __init__(self, radius=10, border_color="black", fill_color="SlateBule", x=0, y=0):
        self.radius = radius
        self.border_color = border_color
        self.fill_color = fill_color
        self.x = x
        self.y = y

    def get_perimeter(self):
        """
        返回当前圆的周长
        :return:
        """
        return 2 * math.pi * self.radius

    def get_area(self):
        """
        返回圆的面积
        :return:
        """
        return math.pi * math.pow(self.radius, 2)

    def show(self):
        """
        在控制台打印圆的周长和面积
        :return:
        """
        info = "半径为{}的圆周长为{:2f},面积为{:2f}\n 坐标:({},{})"
        info = info.format(self.radius, self.get_perimeter(), self.get_area(), self.x, self.y)
        print(info)
        return info

    def show1(self):
        """ 在图形界面打印圆"""
        turtle.setup(800, 600)
        turtle.title("根据制定的圆的半径以及坐标、颜色的绘制圆的对象")
        pen = turtle.Pen()
        pen.up()
        pen.goto(self.x, self.y)        # 起笔移动要圆心坐标处
        pen.down()
        pen.color(self.border_color)    # 设置画笔颜色
        pen.circle(self.radius)
        turtle.done()


if __name__ == '__main__':
    circle = Circle(100)
    circle.show()
    circle.show1()
