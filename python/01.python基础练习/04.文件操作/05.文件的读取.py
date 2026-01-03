# 文件的读取


# 测试ceshi.txt文件的内容:
# helloword1
# helloword2
# helloword3


# f = open('D:/code/python/04.文件操作/ceshi.txt',"r", encoding='UTF-8')
# print(f)
# print(type(f))      #查看类型


##read方法
# 不指定参数，则以列表方式打印
# print({f.read()})
# 读取两个字符
# print({f.read(2)})
##readlines读取文件的全部行，封装到列表中
# lines = f.readlines()
# print({type(lines)})   ##查看类型
# print(lines)

##readline读取文件的行
# line = f.readline()
# print({type(line)})
# print(line)
# print({f.read()})
# f.close()
# 我们还可以通过循环
# for line in f:
#      print(line)

with open("D:/code/python/04.文件操作/ceshi.txt", "r", encoding="UTF-8") as f:
    for line in f:
        print(line)


# file=open('a.txt','r',encoding='UTF-8')
# print(file.readlines())
# file.close()
