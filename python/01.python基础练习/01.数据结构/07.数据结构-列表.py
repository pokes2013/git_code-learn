# 05.数据结构-列表

lst=[40,41,42,43,44]
print(lst)
print(lst[1])
lst.append(100)      #新增
print(lst)

lst[1]=410           #修改，可以理解为替换
print(lst)
lst.remove(42)       #删除
print(lst)
print('---------------------------------')

##遍历列表
for i in range(0,len(lst)):
    print(lst[i])

print('---------------------------------')

for item in lst:
    print(item)

