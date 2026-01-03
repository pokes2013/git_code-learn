class Person:
    def eat(self):
        print("人吃东西")


class Cat:
    def eat(self):
        print("猫吃鱼")


class Dog:
    def eat(self):
        print("狗吃骨头")


# 上面三个类共同的特点就是：都有eat方法


def fun(pokes):
    pokes.eat()


if __name__ == '__main__':
    per = Person()
    cat = Cat()
    dog = Dog()

    # 传入的参数是什么类型，就调用什么类型的方法
    fun(per)
    fun(cat)
    fun(dog)
