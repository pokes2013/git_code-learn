# 文件对象的常用方法


# read读取，不加字节数则读取全部
file=open('a.txt','r',encoding='UTF-8')
print(file.read())
file.close()

# readline从文本文件中读取1行

file=open('a.txt','r',encoding='UTF-8')
print(file.readline())
file.close()

# readlines从文本文件中读取多行，并且放到列表中

file=open('a.txt','r',encoding='UTF-8')
print(file.readlines())
file.close()

#write将字符串str内容写入文件
file=open('b.txt','a')        #a追加
file.write('helloworld')      #写入字符串
lst=['java','go','python']
file.writelines(lst)          #写入列表
file.close()

# seek跳过字节读取

a.txt文件内容
中国
美丽


file=open('a.txt','r',encoding='UTF-8')
file.seek(2)        #光标跳过2个字节后读取剩下的注意一个汉字占两个字节，这里写1会报错
print(file.read())
file.close()
# ——————————————————————————————
运行结果：
国
美丽
