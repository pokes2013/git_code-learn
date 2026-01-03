#匿名函数
#作用：简化函数定义

# 平时定义函数是这样定义的
def add(a,b):
    s = a + b
    return s





# 案例：求和

s = lambda a, b: a + b
result = s(1, 2)
print(result)


# # 匿名函数作为参数

def func(x, y, func):
    s = func(x,y)
    print(s)

# 调用
func(6, 8, lambda a, b: a + b)
