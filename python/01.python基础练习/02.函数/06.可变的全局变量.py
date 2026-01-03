#可变的全局变量


list = [1,2,4,6]

def func():
    list.append(8)
    print(list)

func()