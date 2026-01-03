class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f'我叫{self.name},我今年{self.age}岁了')


# 子类
# Student类继承Person类
class Student(Person):
    def __init__(self, name, age, stuid):  # stuid，学号
        # 父类中已经定义了name，和age，在这里调用即可
        # 使用super调用父类的初始化方法，也可以使用类名，下面代码使用类名
        super().__init__(name, age)
        self.stuid = stuid  # 学生特有的属性学号赋值

    # 重写父类方法
    # 方法名和父类中的完全相同
    def show(self):
        # 可以调用父类的show方法，也可以重写

        # 调用父类方法
        super().show()
        # 补充自己的个性化的内容
        print(f'我的学号是{self.stuid}')


# 子类
# Doctor类继承Person类
class Doctor(Person):
    def __init__(self, name, age, department):  # department单词，科室
        # 使用类名调用父类的初始化方法
        Person.__init__(self, name, age)
        self.department = department  # 医生特有的属性，科室

    def show(self):
        # 重写父类中的show方法
        print(f'我是{self.name},我今年{self.age}岁了，我的科室是{self.department}')


if __name__ == '__main__':
    # 创建Student类的对象
    stu = Student("小美", 20, "stu0007")
    # 调用父类的show方法
    stu.show()

    # 创建Doctor类的对象
    doctor = Doctor("张医生", 30, "外科")
    # 调用父类的show方法
    doctor.show()
