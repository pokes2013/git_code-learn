class Circle:

    def __init__(self, r):
        self.r = r

    # 计算圆的面积	：面积=πr平方
    def get_area(self):
        return 3.14 * (self.r * self.r)

    # 计算圆的周长：2πr
    def get_perimeter(self):
        return 2 * 3.14 * self.r


if __name__ == '__main__':
    r = eval(input("请输入圆的半径："))

    # 创建对象
    c = Circle(r)

    area = c.get_area()
    perimeter = c.get_perimeter()

    print(f"圆的面积", area)
    print(f"圆的周长", perimeter)
