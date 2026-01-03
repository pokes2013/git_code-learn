class Student:
    def __init__(self, name):
        self.__name = name

    @property  # 通过@property修饰后的方法可以当成属性使用
    def age(self):  # 设置只读属性，
        return self.__age

    @age.setter  # 设置赋值操作
    def age(self, value):
        if value < 0 or value > 130:
            print('年龄不在正确的范围区间内，年龄区间0-130')
            self.__age = 18  # 设置默认值
        else:
            self.__age = value

    def show(self):
        print(f'我叫：{self.__name}今年{self.__age}岁.')


if __name__ == '__main__':
    stu = Student("小明")
    stu.age = -23
    print(stu.age)
    stu.show()

    stu.age = 20
    stu.show()
