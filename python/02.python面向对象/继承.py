class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def show(self):
        print(f'我叫{self.__name},我今年{self.__age}岁了')


# 子类
# Student类继承Person类
class Student(Person):
    def __init__(self, name, age, stuid):  # stuid，学号
        # 父类中已经定义了name，和age，在这里调用即可
        # 使用super调用父类的初始化方法，也可以使用类名，下面代码使用类名
        super().__init__(name, age)
        self.stuid = stuid  # 学生特有的属性学号赋值


# 子类
# Doctor类继承Person类
class Doctor(Person):
    def __init__(self, name, age, department):  # department单词，科室
        # 使用类名调用父类的初始化方法
        Person.__init__(self, name, age)
        self.department = department  # 医生特有的属性，科室


if __name__ == '__main__':
    # 创建Student类的对象
    stu = Student("小美", 20, "stu0007")
    # 调用父类的show方法
    stu.show()

    # 创建Doctor类的对象
    doctor = Doctor("张医生", 30, "外科")
    # 调用父类的show方法
    doctor.show()
