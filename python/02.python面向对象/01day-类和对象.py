class Student:
    school = "北京清华附属中学"  # 类属性

    # 初始化方法
    def __init__(self, name, age):
        self.name = name  # 等号左侧是实例属性，右侧是局部变量
        self.age = age

    # 实例方法
    def show(self):
        print(f"我叫{self.name},今年{self.age}岁了")

    # 静态方法
    @staticmethod
    def sm():
        print("这是一个静态方法")
        # 注意：类方法不能调用实例属性和实例方法

    # 类方法

    @classmethod
    def cm(cls):
        print("这是一个类方法")
        # 注意：类方法不能调用实例属性和实例方法


# 创建对象
stu = Student("tom", 18)
# 说明：创建对象时程序会自动调用初始化方法，所以传入的参数数量和类型完全取决于初始化方法，即：init函数。

# 实例属性调用
print(stu.name, stu.age)

# 类属性调用
print(stu.school)  # 使用对象调用类属性
print(Student.school)  # 使用类调用类属性

# 实例方法的调用
stu.show()

# 静态方法调用
Student.sm()

# 类方法调用
Student.cm()
