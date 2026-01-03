class FatherA():
    def __init__(self, name):
        self.name = name

    def showA(self):
        print(f"我叫{self.name}")


class FatherB():
    def __init__(self, age):
        self.age = age

    def showB(self):
        print(f"我今年{self.age}岁了")


# 这里继承了FatherA和FatherB两个类的方法和属性
class Son(FatherA, FatherB):
    def __init__(self, name, age, gender):  # gender,性别

        # 这是只能使用类名调用父类方法，多继承中不能使用super调用类属性
        FatherA.__init__(self, name)  # 给name赋值
        FatherB.__init__(self, age)  # 给age赋值
        self.gender = gender

    def showS(self):
        print(f"我的性别是{self.gender}")


if __name__ == '__main__':
    son = Son("小美", 20, "女")
    son.showA()  # 调用父类FatherA的方法
    son.showB()  # 调用父类FatherB的方法
    son.showS()  # 调用自己的方法
