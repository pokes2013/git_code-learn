class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age


# 创建对象并传参
p = Person("小明", 20)

# 重新赋值name
p.set_name("小红")

print(p.get_name(), p.get_age())  # 输出小红,20
