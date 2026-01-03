# 全局变量和局部变量


name = 'pokes'

# # 案例1

def func1():
    print(name)


# # 案例2

# def func2():
#     name = 'spokes'
#     print(name)

# func2()

# # 案例3

def func2():
    global name
    name = 'spokes'
    print(name)

func2()
func1()


