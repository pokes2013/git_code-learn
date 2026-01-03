class Student:
    # 类属性
    school = "中心学校"

    # 初始化方法
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 实例属性的调用
    def show(self):
        print(f'我叫{self.name},今年{self.age}岁了！')

    # 类方法
    @classmethod
    def classff(cls):
        print("这是类方法，不能调用实例属性和实例方法")

    # 静态方法
    @staticmethod
    def staticff():
        print("这是静态方法，不能调用实例属性和实例方法")


stu = Student("小明", 16)
print(stu.name, stu.age, stu.school,Student.school)
stu.show()
stu.classff()
stu.staticff()

# 通过类名调用类方法和静态方法
Student.classff()  #调用类方法
Student.staticff()  #调用静态方法
# Student.show() 但是不能调用类中的普通方法，要想调用必须先创建对象
