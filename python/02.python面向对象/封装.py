class Student1:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def show(self):
        print(f'我叫{self.__name},我今年{self.__age}岁了')


if __name__ == '__main__':
    # 程序运行没有报错，但是 运行结果不符合实际情况，年龄被赋予了不正确的值
    stu = Student1("小美", -23)
    stu.show()


print("-"*60)

class Student2:
    def __init__(self, name):
        self.__name = name

    # @property是一个装饰器
    # 用@property修饰过之后可以将方法当成属性来使用，使用时不需要加括号
    @property
    def age(self):  # 设置只读属性
        return self.__age

    # 设置赋值操作
    @age.setter
    def age(self, value):
        if value < 0 or value > 130:
            print("警告：输入的年龄不再正确范围之内，正确范围应该为0-130之间，默认值为18")
            self.__age = 18  # 超出0-130，则设置默认显示值18
        else:
            self.__age = value

    def show(self):
        print(f'我叫{self.__name},我今年{self.__age}岁了')


if __name__ == '__main__':
    stu = Student2("小美")
    stu.age = -23
    print(stu.age)  # 用@property修饰过之后age方法，可以当成属性来使用，使用时不需要加括号

