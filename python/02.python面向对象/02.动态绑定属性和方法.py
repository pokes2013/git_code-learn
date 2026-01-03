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


# 对象的创建
stu1 = Student("小明", 16)
stu2 = Student("小红", 15)

print(stu1.name, stu1.age)
print(stu2.name, stu2.age)

# 动态绑定属性
stu1.sex = "男"
stu2.sex = "女"
print(stu1.name, stu1.age, stu1.sex)
print(stu2.name, stu2.age, stu2.sex)


# 动态绑定方法
def introduce():
    print("我是一个普通函数，我被动态绑定成为stu2的对象方法！")


# 绑定方法，introduce不能有括号
stu2.pokes = introduce

# 调用绑定的动态方法,调用要加上括号
stu2.pokes()  # 我是一个普通函数，我被动态绑定成为stu2的对象方法！
