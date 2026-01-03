# 函数的返回值return


def add(a,b):
    s = a + b
    return s,'hello','python'

x = add(4,5)   
print(x)

print(x[0])


# return后的语句不在执行
# 返回值必须用变量接住
# 返回值如果是多个，返回结果为元组