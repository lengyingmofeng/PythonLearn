# @作者 : 叶枫
# @文件 : 自定义列表.py 
# @时间 : 2020/10/14 16:33 
# @版本 ：1.0
# @功能描述：
class MyList:
    def __init__(self, data=None):
        self.data = []
        if data is None:
            self.data = []
        else:
            self.data = data

    def __getitem__(self, index):
        # 让本类的对象支持下标访问：my_list1[0]
        if isinstance(index, int):
            return self.data[index]
        elif type(index) is slice:
            print("切片的起始值：", index.start)
            print("切片的结束值：", index.stop)
            print("切片的步长", index.step)
            return self.data[index]

    def __setitem__(self, index, value):
        self.data[index] = value

    def __contains__(self, item):
        print("判断传入的", item, "是否在列表中的")
        return self.data.__contains__(item)

    def append(self, item):
        self.data.append(item)

    def pop(self, index=-1):
        # 默认删除并返回最后一个
        return self.data.pop(index)

    def __delitem__(self, index):
        del self.data[index]

    def __str__(self):
        return str(self.data)


if __name__ == '__main__':
    my_list1 = MyList([x for x in range(10)])
    print(my_list1)
    my_list1[0] = 1111
    print(my_list1[0], my_list1)
    print(my_list1[0:10:2])
    print("删除并返回最后一个元素：", my_list1.pop())
    print(my_list1)

    del my_list1[-1]                # 必须定义__delitem__

    print(my_list1)