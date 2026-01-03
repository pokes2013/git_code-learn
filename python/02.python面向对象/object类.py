print(dir(object))
print("-"*100)   # 分割线


# 所有的类都是继承了object类，所以下方的Person类中，括号里面的object可以默认不写
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"大家好，我叫{self.name},今年{self.age}岁了")

    # 重写__str__方法
    def __str__(self):
        return "这个是一个人类，具有name和age两个实例属性"


if __name__ == '__main__':
    per = Person("小美", 20)
    print(dir(per))
    print("-" * 100)  # 分割线
    print(per)  #当直接输出对象名是，默认调用__str__()方法
    print(per.__str__())
