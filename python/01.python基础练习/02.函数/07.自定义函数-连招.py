# 初识函数

#自定义函数

def lianzhao():
    print('直拳')
    print('勾拳')
    print('摆拳')
    print('肘击')

# 调用
lianzhao()

# 感觉打得不够狠！我想连续多次使用连招，我们可以加入循环

def lianzhaocishu(cishu):
    for i in range(cishu):
        print('直拳')
        print('勾拳')
        print('摆拳')
        print('肘击+凌空一脚')


# 调用
lianzhaocishu(5)