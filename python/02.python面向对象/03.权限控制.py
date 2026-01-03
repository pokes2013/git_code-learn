class Student():
    def __init__(self, name, age, sex):
        # 首尾双下划线，表示特殊的方法，系统定义
        self._name = name  # 以单下划线开头，表示是受保护的成员，只能类本身和子类访问
        self.__age = age  # 以双下划线开头，表示是私有的，只能类本身使用
        self.sex = sex  # 普通的实例属性，在类的外部和类的内部以及子类都可以访问

    def _pokes1(self):  # 表示收保护的方法
        print('子类和本身可以访问')

    def __pokes2(self):  # 私有方法
        print('只有定义的类本身可以访问')

    # 这是一个普通的实例方法，在类的外部使用对象名打点访问
    # #在类的内部，使用seLf打点访问
    def show(self):
        print('普通方法，都可以访问！')


if __name__ == '__main__':
    stu = Student('小明', 16, '男')
    print(stu._name)  # 小明
    # print(stu.__age),报错__age私有，出了这个类就无法访问

    stu._pokes1()
    # stu.__pokes2(),报错__pokes2私有，出了这个类就无法访问
