class Student():
    def __init__(self, name, age, gender):
        self._name = name  # 以单下划线开头,表示受保护的成员，只允许类本身和子类进行访问
        self.__age = age  # 双下划线表示私有的成员,只允许定义该方法的类本身访问，即使是类方法也不能访问
        self.gender = gender  # 普通实例属性

    def _fun1(self):
        print("子类和本身可以访问")

    def __fun2(self):
        print("只有所属类可以访问")

    def show(self):
        print("普通方法，谁都可以调用")
        self._fun1()
        self.__fun2()
        print(self._name)
        print(self.__age)


if __name__ == '__main__':
    stu = Student("小美", 20, "女")
    print(stu._name)  # 可以调用，因为调用他的是类本身
    # print(stu.__age)   #程序报错，仅允许类本身访问，即使是类方法也不能访问
    print(stu.gender)  # 普通类属性，随便调用

    stu._fun1()  # 类本身和子类可以访问，所以显示正常
    # stu.__fun2()   程序报错
