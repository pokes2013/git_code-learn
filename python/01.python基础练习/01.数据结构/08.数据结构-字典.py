#数据结构-字典
# key键，value值，一一对应，不能一对多。而且键不能重复。好似一对不能分开得夫妻。

dict_size={'41':10,'42':8,'43':2}

# 打印所有
print(dict_size)

# 打印具体得某个值
print(dict_size['41'])

#添加元素
dict_size['44']=100   #添加元素是通过“=”赋值得形式
print(dict_size)

#修改元素
dict_size['44']=1000
print(dict_size)

#删除
#删除是键值成对删除
del dict_size['42']
print(dict_size)
# -----------------------
#遍历
for i in dict_size:
    print(i,dict_size[i])

# 运行结果：
# 41 10
# 43 2
# 44 1000