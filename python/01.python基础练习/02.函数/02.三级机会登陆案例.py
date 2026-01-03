# 定义一个登陆函数，参数是：username,password
# 函数体：
# 判断参数传过来得username,password是否正确，如果正确则登陆成功，否则打印登陆失败。


#函数的定义


def login(username,password):
    uname='admin123'
    pwd='112233'

    for i in range(2):
        if username == uname and password == pwd:
            print('登陆成功！')
            break
        else:
            username = input('请重新输入用户名：')
            password = input('输入密码：')
    else:
        print('账户已锁定，请稍后再试')

#调用
print('提示：你只有三次机会,密码输入错误超过3次,将锁定账户')
username = input('输入用户名：')
password = input('输入密码：')
login(username,password)