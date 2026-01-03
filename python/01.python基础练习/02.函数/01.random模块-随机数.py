# function（函数）
# 定义函数：随机数产生
# 自动格式化：shift+ctrl+f，format的意思！



import random


def number(a):      #此时得number是形参
    for i in range(a):
        # 生成随机数需要用到 random模块里的randint()函数
        # 括号里两个参数为整数，划定随机生成整数的范围（最小最大值）
        s = random.randint(1,200)         #定义随机数的范围
        print(s)


# 调用
number(5)          #实参，就是具体得值，意思就是我需要几个随机数