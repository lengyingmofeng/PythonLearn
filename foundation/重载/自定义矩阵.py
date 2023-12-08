# @作者 : 叶枫
# @文件 : 自定义矩阵.py 
# @时间 : 2020/10/14 16:59 
# @版本 ：1.0
# @功能描述:
class Matrix:
    """矩阵实际上就是封装了二维列表的常见操作"""
    def __init__(self, data=None):
        self.__data = None
        if data is None:
            self.__data = []
        else:
            self.__data = data

    def __getitem__(self, item):
        return self.__data[item]

    def __add__(self, other):
        # 二维列表相加，需求使用双循环将相加的结果存放在第三个列表中
        result = []
        for i in range(len(self.__data)):
            result.append([])
            for j in range(len(self.__data[i])):
                result[i].append(self.__data[i][j] + other[i][j])
        return Matrix(result)

    def __str__(self):
        content = "["
        for item in self.__data:
            content += "\n\t["
            for element in item:
                content += str(element) + ","
            content = content[0:-1]
            content += "]"
        content += "\b\n]"
        return content


import numpy

if __name__ == '__main__':
    mratrix1 = Matrix([[1, 2, 3], [4, 5, 6]])
    mratrix2 = Matrix([[1, 2, 3], [4, 5, 6]])
    mratrix3 = mratrix1 + mratrix2
    print(mratrix3)
    mratrix4 = numpy.mat("1 3 5; 7 9 11")
    maatrix5 = numpy.mat([[1, 2, 3], [4, 5, 6]])
    print(maatrix5 + mratrix4)
    # 创建一个3*3的元素值在2-9之间的数字矩阵
    maatrix6 = numpy.mat(numpy.random.randint(2, 10, size=(3, 3)))
    print(maatrix6)
