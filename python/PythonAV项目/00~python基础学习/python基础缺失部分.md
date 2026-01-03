



# python基础缺失部分



## 一、字符串操作

### 1、字符串的切片
#### 通过下标截取

```python
my_str = "%pokes$@163&.com*"
value1 = my_str[2]  # 正向下标从0开始
value2 = my_str[-5]  # 反向下标从-1开始

print(value1)   #运行结果是“o”
print(value2)   #运行结果是“.”
```

字符串分割，语法：string[end: step]
- start 头下标,开始,，以0开头
- end 尾下标,结尾
- step 步长

```python
str = "abc-123-如果我是DJ你会爱我吗.mp4"
str = str[0:7]           #默认步长是1，可以不写
print(str)
# 结果：abc-123
```
```python
str = "abc-123-如果我是DJ你会爱我吗.mp4"
str = str[0:-9]           #负数是从右往左截取
print(str)
# 结果：abc-123-如果我是DJ
```
```python
str = "abc-123-如果我是DJ你会爱我吗.mp4"
str = str[8:]           #不写右边就是一直到结尾
print(str)
# 结果：如果我是DJ你会爱我吗.mp4
```

#### index方法

查找特定字符串的下标索引值

```python
my_str = "%pokes$@163&.com*"
value3 = my_str.index("pokes")
print(value3)   

#运行结果是“1”
注意：1是"pokes"起始下标，即p所在的下标位置
```

#### replace方法

字符串替换

语法：变量.replace(“被替换的内容”，“替换后的内容”[，次数])
```python
str2= "ithahahaaa and ithehehehe"
new_str2 = str2.replace("it","pokes")    #将it替换成pokes
print(new_str2)        

#运行结果：pokeshahahaaa and pokeshehehehe
```

过滤掉顿号
```python
str1 = "212、Python用replace()函数删除制定  符号"
str2 = str1.replace('、', '')      #可以这样理解，把顿号替换为空
print(str2)
```
#### split方法

分割字符串

关键字split，语法格式：变量.split('分隔符',次数)
```python
str3= "abc-123-C-爱丽丝-遥远的故事.pdf"
new_str3 = str3.split(".")
print(new_str3)
new_str4 = str3.split("-")
print(new_str4)
```
运行结果：
![在这里插入图片描述](https://img-blog.csdnimg.cn/14348eb02c9a45fc95ece75765358910.png)
```python
str = "abc-123-如果我是DJ你会爱我吗.mp4"
str = str.split('-')          #次数不写，则默认为最大次数
print(str)
结果：['abc', '123', '如果我是DJ你会爱我吗.mp4']
```

#### strip方法：

去除字符串两端的空格和回车符

strip 两头 ，lstrip头， rstrip尾。去掉两头的空格，注意不包含中间的空格

```python
str5= "     heihei hehe haha    "
new_str5=str5.strip()   #不传参数，默认去除两端的空格和回车符
print(new_str5)
```

连续的过滤字符
```python
s = "   %pokes$@163&.com*   "

ss = s.strip().strip("%").lstrip('$').rstrip().rstrip('*')
print(ss)
```
运行结果
![在这里插入图片描述](https://img-blog.csdnimg.cn/9dc956f0c09d4474807e596299c24f56.png)
详情参考：`https://blog.csdn.net/csdn15698845876/article/details/73469234`



#### count方法

统计字符串中某字符出现的次数

```python
str6= "heihei hehe haha"
cishu = str6.count("he")
print(cishu)

#运行结果：4
```
#### len方法

统计字符串的长度

```python
str6= "heihei hehe haha"
num=len(str6)
print(num)
```

#### find方法

字符串查找

find方法检测字符串中是否包含子字符串str ，如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内，如果指定范围内如果包含指定索引值，如果不包含索引值，返回-1。返回的是需要查找的字符串的下标
变量.find(“要查找的内容”，[开始位置，结束位置])
```python
str = "abc-123-如果我是DJ你会爱我吗.mp4"
str = str.find('DJ')
print(str)
结果:12         #返回的是需要查找的字符串的下标,不包含则返回-1
```
![在这里插入图片描述](https://img-blog.csdnimg.cn/03ff7a0dc6ec4fb9a995f89a2b93ec0b.png)

### 2、字符串判断
#### 判断字符串是否只包含数字
内置函数

```python
str_1 = "123"
str_2 = "Abc"
str_3 = "123Abc"

print(str_1.isdigit())
print(str_2.isdigit())
print(str_3.isdigit())
```
运行结果
![在这里插入图片描述](https://img-blog.csdnimg.cn/3832085e2c55480693150b61f9ec692a.png)

txdpy模块

这个模块不是很出名，查了都没找到结果。不过很好用
使用前先安装模块`pip install txdpy`，用法演示：
```python
from txdpy import is_num,is_chinese,is_letter,is_Bletter,is_Sletter,is_num_letter

s1='s1'
s2='ss'
s3='s三'
s4='SSSS'
s5='测试'
s6='6666'
s7='测试777'
 
#是否为纯数字
print(is_num(s6))
print(is_num(s7))
#是否为纯汉字
print(is_chinese(s5))
print(is_chinese(s7))
#是否为纯字母
print(is_letter(s1))
print(is_letter(s2))
#是否为纯大写字母
print(is_Bletter(s4))
print(is_Bletter(s2))
#是否为纯小写字母
print(is_Sletter(s4))
print(is_Sletter(s2))
#是否为只包含字母、数字、数字字母混合，不含其他除字母和数字以外的任何字符
print(is_num_letter(s1))
print(is_num_letter(s4))
```
#### 判断字符串中包含特殊符号

```python
input_psd = input("请输入字符串")
# 判断是否有特殊字符

string = "~!@#$%^&*()_+-*/<>,.[]\/"
for i in string:
    if i in input_psd:
        print("您的输入包含特殊字符")

```
或者导入 python 内置模块 re
```python
import re
input_psd = input("请输入字符串")
test_str = re.search(r"\W",input_psd)
if test_str==None:
    print("没有没有真没有特殊字符")
else:
    print("该文本包含特殊字符")

```
re模块，过滤字符

```python
import re

str1 = "  12312313Python用replace()函数删除制定  符号  "
str2 = re.sub('([^\u4e00-\u9fa5])', '', str1)		#只保留汉字
print(str2) 


# 只保留字符串中的汉字和数字

str2 = re.sub('([^\u4e00-\u9fa5\u0030-\u0039])', '', str1)
print(str2) 
```
常用字符unicode的编码范围：

- 数字：\u0030-\u0039
- 汉字：\u4e00-\u9fa5
- 大写字母：\u0041-\u005a
- 小写字母：\u0061-\u007a
- 英文字母：\u0041-\u007a

注：更多的编码范围可参考另博主的整理：`https://blog.csdn.net/weixin_34206263/article/details/112031865`

#### 知识点：计算机提问而得到的任何回答都是字符串类型

==由计算机提问而得到的任何回答都是字符串类型==

```python
age=input('你几岁了？')
print(age)
print(type(age))
age=int(age)     #数据类型转换
print(type(age))
```
#### 字符串字母大小写转换和判断
- capitalize，#将字符串得第一个字符转换成大写
- title，每个单词得首字母大写
- istitle #判断每个单词得首字母是否大写
- upper 全部转换成大写
- lower 全部转换成小写
```python
message = 'zhaorui is a beautiful girl!'

# capitalize

msg = message.capitalize()   #将字符串得第一个字符转换成大写
print(msg)

# title
msg = message.title()      #每个单词得首字母大写
print(msg)


# istitle

cmd = msg.istitle()           #判断每个单词得首字母是否大写
print(cmd)

spokes = message.istitle()    #判断每个单词得首字母是否大写
print(spokes)

# upper 全部转换成大写

msg = message.upper()
print(msg)

# lower 全部转换成小写
msg = message.lower()
print(msg)
print(len(msg))          #计算字符串长度
```
### 3、字符串比较

```python
s1='abc'
s2="abc"
#
# # 内容比较
print(s1 == s2)
print(s1 is s2)

pokes1 = input('请输入：')
pokes2 = input('请输入：')
#
print(pokes1 == pokes2)
```
### 4、过滤掉某个字符

#### 过滤掉单个字符

```python
str1 = "212、Python用replace()函数删除制定  符号"
str2 = str1.replace('、','')		#过滤掉顿号
print(str2)
```

#### 过滤掉多个符号
```python
def zifu(str, x, y, z):
    strin = str.replace(x, '') .replace(y, '').replace(z, '')
    print(strin)

zifu("pokes，@163.com,kkkkk", "，", ",", "163")
```



### 5、控制流语句

#### IF判断

#### 银行取款案例.数据类型转换

只要是input接受用户输入的都是字符串类型

```python
balance=1000    #银行卡余额
money=input('请输入取款金额：')
money=int(money)

if money<=balance:
    balance=balance-money
    print('取款成功,当前余额为：'+str(balance))   #str(balance)将int类型转换str类型，不转无法拼接
else:
    print('操作失败，余额不足，当前余额为：'+str(balance))
```



#### for循环

```python

for ch in 'python':
    print(ch)

for i in range(1,10):
    print(i)
    
```

#### while循环

```python
a=1
while a<=5:
    print(a)
    a=a+1
```



### 6、列表的操作

```python
# 声明两个列表变量
list1 = ['Python', 'PHP', 'Java', 'Bash']
list2 = ['JavaScript是客户端脚本语言',
         'PHP是服务器端脚本语言',
         'Java是一种编程语言',
         'Kotlin是一种静态编程语言']

# 根据第一个列表过滤第二个列表
filter_data = [x for x in list2 if all(y not in x for y in list1)]

# 在过滤前和过滤后打印列表数据
print("第一个列表的内容:", list1)
print("第二个列表的内容:", list2)
print("过滤后的第二个列表的内容:", filter_data)

运行结果：
第一个列表的内容: ['Python', 'PHP', 'Java', 'Bash']
第二个列表的内容: ['JavaScript是客户端脚本语言', 'PHP是服务器端脚本语言', 'Java是一种编程语言', 'Kotlin是一种静态编程语言']
过滤后的第二个列表的内容: ['Kotlin是一种静态编程语言']
```



### 7、本文的操作

读取

```python 
# 文件的读取


file=open('a.txt','r',encoding='UTF-8')
print(file.readlines())
file.close()

file=open(r'D:\code\python\03.module\a.txt','r',encoding='UTF-8')
print(file.readlines())
file.close()

# 文件的写入
file=open('b.txt','w')
file.write('helloworld')
file.close()


with open("D:/code/python/04.文件操作/ceshi.txt","r", encoding="UTF-8") as f:
    for line in f:
        print(line)
```



### 8、函数的操作

### 9、常用模块

#### os文件路径

待写

#### excel表的操作

待写

#### MySQL操作

待写



## 二、python项目实战演练



### 01.写入日志函数

```python
def write_txt(str,txt_name):

    file = open(txt_name, 'a', encoding='UTF-8')
    file.write(str)
    file.close()
```

### 02.过滤掉一个列表中的非法字符
```python
def guolvhaha(lists):
    """
    过滤掉一个列表中的非法字符
    """
    # lists = ["woshinidaye$123456", "abc-123456", "woshinidaye-123456欧美", "woshinidaye三级.123456"]
    ffstr_list = ["欧美", "国产", "韩国", "香港", "$"]  # 将这些视为非法字符
    nowlist = []
    for vido in lists:
        # print(vido)
        for ffstr in ffstr_list:  # 遍历出需要过滤的字符
            if (ffstr in vido) or ("-" not in vido):  # 满足一个条件就跳过本次循环
                # print(vido,"buguize")
                continue
            else:
                # print(vido)
                if vido not in nowlist:
                    nowlist.append(vido)
                    return nowlist


lists = ["woshinidaye$123456", "abc-123456", "woshinidaye-123456欧美", "woshinidaye.123456"]
heihei = guolvhaha(lists)
print(heihei)
```
### 03.建立文件索引
```python
# 这是一个用于创建索引的函数的集合
# 作者：pokes@163.com

import os


def bl_txt_line(txt_data):
    """
    用于遍历txt文件每行的内容,并且去重
    """

    # 读取文本txt_data中的内容files
    with open(txt_data, "r", encoding="UTF-8") as files:  # 打开txt_data返回文件对象files
        in_name_list = []
        for line in files:
            in_name = os.path.basename(line)  # 从files遍历出每行的内容line
            in_name = in_name.strip('\n')  # 遍历出来的内容自带一个换行，这里我们不需要所以要去掉

            if in_name not in in_name_list:  # 这里有个去重复的判断
                in_name_list.append(in_name)
            else:
                print(in_name, "文件貌似重复，请二次确认")
    return in_name_list


def cj_floder(floder_name):
    """
    用于创建和检测目录是否存在，不存在则创建，存在则pass。
    """

    isexists = os.path.exists(floder_name)
    if not isexists:
        os.makedirs(floder_name)


# cj_floder("suoyin")

def cj_vido_file(str_name, sy_path):
    """
    一个用于创建视频索引的函数。
    :param str_name: 创建索引视频的名称，它是一个字符串
    :param sy_path: 创建索引视频的目录，它是一个字符串。需要注意的是：sy_path目录必须存在，不存在或不给sy_path传参，则索引会创建在py文件默认的工作目录。
    """
    suoyin_path = sy_path + "\\" + str_name  # 路径的拼接
    print(suoyin_path)
    file_mp4 = open(suoyin_path, "w", encoding="UTF-8")
    file_mp4.write(suoyin_path)


# 下面将调用上面所写的函数来执行
txt_file = "data.txt"  # 存放内容的txt文档
sy_floder = "suoyin"  # 用于存放索引的目录名

cj_floder(sy_floder)  # 调用创建目录的函数
sy_list = bl_txt_line(txt_file)  # 调用读取txt文档的函数，结果是一个list

for vido in sy_list:  # 利用for循环进行遍历
    cj_vido_file(vido, sy_floder)  # 调用创建索引函数
    print(vido, "文件索引创建成功")

```

### 04.遍历文件.不含子目录
```python
import os


def file_list(path, extension):
    """
        遍历path下,某个类型的文件,并生产一个list.注意不含子目录
    """
    files_list = os.listdir(path)  # 当前目录所有文件的序列
    vido_list = [s for s in files_list if extension in s]
    return vido_list


deome = file_list(r"F:\2020课程整理-最终版\python\黑马程序员python教程8天python从入门到精通", ".mp4")
print(deome)

```

### 05.遍历文件.含子目录
```python
import os


def file_name_list(dir_path):
    """
        遍历dir路径下,所有文件.含子目录，最终结果只显示文件名
    """
    files_list = []
    for parent, dirnames, filenames in os.walk(dir_path):
        for filename in filenames:
            # print(filename)
            # file_path = os.path.join(parent, filename)    #显示绝对路径
            if filename not in files_list:  # 这里有个去重复的判断
                files_list.append(filename)
    print(files_list)  # 所有文件的绝对路径


def file_path_lists(dir_path):
    """
        遍历dir路径下,所有文件.含子目录，最终结果显示绝对路径
    """
    files_list = []
    for parent, dirnames, filenames in os.walk(dir_path):
        for filename in filenames:
            file_path = os.path.join(parent, filename)  # 显示绝对路径
            if filename not in files_list:  # 这里有个去重复的判断
                files_list.append(file_path)
    print(files_list)  # 所有文件的绝对路径


file_name_list(r"F:\2020课程整理-最终版\python\黑马程序员python教程8天python从入门到精通")
# deome=scaner_file(r"E:\转码项目")
# print(deome)

```

### 06.提取当前目录内的ID.数字字母混合
```python
# 提取当前目录内的番号

import os
from txdpy import is_num, is_chinese, is_letter, is_Bletter, is_Sletter, is_num_letter


def avfile_name_id_draw(input_file_neme):
    """
    这是一个电影ID提取的程序
    :param input_file_neme: 输入你的文件的name
    :return: 返回截取后的new_name
    """

    # 过滤非法字符
    ffstr_list = ["欧美", "国产", "韩国", "香港",  "$"]  # 将这些视为非法字符
    for ffstr in ffstr_list:  # 遍历出需要过滤的字符
        if ffstr in input_file_neme: sys.exit()  # 如果出现非法字符，则程序退出

    # 如果没有“-”,则退出处理
    if "-" not in input_file_neme: sys.exit()  # 判断是否包含分隔符

    # 过滤字符
    input_file_neme = input_file_neme.replace(',', '').replace('，', '').replace(' ', '').replace('VIP-', '')
    wzzb = input_file_neme.find('-')
    # print(wzzb)

    # 分隔符之前的字符处理
    str_fenge_qian = "解决调用局部或临时遍历井盖问题"
    numb1 = 0
    while numb1 < wzzb - 1:
        str_fenge_qian = input_file_neme[numb1:wzzb]
        if is_num_letter(str_fenge_qian):  # 判断是否仅包含数字和字母，没有顺序。这一步排除特殊符号,需要安装这个库txdpy
            break
        numb1 += 1

    # 分隔符之后的字符处理
    str_fenge_hou = "解决调用局部或临时遍历井盖问题"
    numb2 = wzzb + 2
    while numb2 < 30:
        str_fenge_hou = input_file_neme[wzzb + 1:numb2]
        if is_num(str_fenge_hou):
            pass
        else:
            str_fenge_hou = input_file_neme[wzzb + 1:numb2 - 1]
            # print("纯数字是:" + str_fenge_hou)
            break
        numb2 += 1
        str_fenge_hou = input_file_neme[wzzb + 1:numb2 - 1]

        # 整合显示结果

    outfile_neme = str_fenge_qian + "-" + str_fenge_hou
    return outfile_neme


f=avfile_name_id_draw("12312321abcd-123411-dwjidwjwid.mp4")
print(f)
```


### 07.批量给文件加后缀
```python
import os


def rename(filess_path, hz_str):
    """
        批量给文件加后缀，例如：源文件为abx-123.pdf  目标文件为abx-123_ok.pdf ,我们在源文件名后面加了_ok
    """

    for root, dirs, files in os.walk(filess_path):
        for video in files:
            # 格式化新文件名
            wzzb = video.rfind('.')  # 定位最后一个.的位置
            qz_name = video[:wzzb]  # 截取不含扩展名的文件名
            hz_name = video[wzzb:]  # 扩展名
            result_name = qz_name + hz_str + hz_name
            # 重命名
            os.chdir(filess_path)  # 在对文件重命名之前为其指定路径
            os.rename(video, result_name)
            print(video)


rename(r"\\10.10.30.97\e\欧美-个人专辑", "[欧美]")

```

### 08.批量视频转码
```python
import os, sys, time


# 创建和检验目录是否存在，如果存在则跳过，不存在则创建

def floders(floder_name):
    isExists = os.path.exists(floder_name)
    if not isExists:
        os.makedirs(floder_name)


# 过滤视频文件

def vidos(vido_path):
    file_list = os.listdir(vido_path)  # 当前目录所有文件的序列
    vido_hz_list = [".avi", ".flv", ".m4v", ".mkv", ".mp4", ".mov", ".rm", ".rmvb", ".ts", ".vob", ".wmv"]

    full_list = []  # 先新建一个空的列表full_list，用来存放帅选出来的元素
    for vido_hz in vido_hz_list:
        vido_gg_list = [s for s in file_list if vido_hz in s]  # 循环筛选各个后缀的视频列表
        for vido in vido_gg_list:  # 遍历这个列表
            # print(vido)               #打印测试之后出现了重复，例如：abc-999.rm和abc-999.rmvb，因为后缀中都有rm所以同时会被筛选出来
            if vido not in full_list:  # 去重后放入新建的空列表中
                full_list.append(vido)
    return full_list


# 转码前的准备


dir_path = os.getcwd()

ok_dir = "OK"
source_dir = "source_data"

floders(ok_dir)
floders(source_dir)

# 遍历最终列表full_list得到每个vido文件
for input_vido in vidos(dir_path):
    qianzhui = os.path.splitext(input_vido)[0]  # 这里我们提取文件名，不含扩展名，用于后面输出文件名得格式化
    print(qianzhui)

    # 文件扩展名得提取
    fg_name = os.path.splitext(input_vido)
    houzhui = fg_name[1]
    # print(houzhui)

    output_vido = qianzhui + "_ok" + ".mp4"
    print(output_vido)

    # 转码

    start_time = time.time()

    str_code01 = "ffmpeg"
    str_code02 = " -i {}".format(input_vido)  # 输入文件
    str_code03 = " -vcodec h264"
    str_code04 = " -preset veryfast"  # 转换速度
    str_code05 = " -tune:v ssim"
    str_code06 = " -qmin 18 -crf 22.0 -maxrate 2500k -bufsize 5000k"  # 码率控制
    str_code07 = " -r 29.97"  # 帧率
    str_code08 = " -vf unsharp=5:5:0.06:5:5:0.0,scale=1280:-2"  # 滤镜和分辨率
    str_code09 = " {}".format(output_vido)
    str_code10 = " && move {} {} > nul".format(output_vido, ok_dir)  # 将转换好的文件移动到ok_dir
    str_code11 = " && move {} {} > nul".format(input_vido, source_dir)  # 将源文件移动到source_dir

    str_code_all = str_code01 + str_code02 + str_code03 + str_code04 + str_code05 + \
                   str_code06 + str_code07 + str_code08 + str_code09 + str_code10 + str_code11

    print(str_code_all)
    cmd_run = os.system(str_code_all)

    print("*" * 100)  # 分割线
    print(dir_path + output_vido + '-转换成功')  # 输出转换成功的提示

    # 记录结束时间
    end_time = time.time()
    took = (end_time - start_time) / 60
    took = int(took)
    took = str(took)
    # print("所需时间:", took,"分钟")

    # 日志系统，日志文件在视频目录中

    file = open("logs.txt", 'a', encoding='UTF-8')
    file.write(input_vido + "\n")
    file.write("所需时间：" + took + "\n")
    file.write("-" * 100 + "\n")
    file.close()

    # 休息10分钟

    time.sleep(600)

```



### 09.检测文件是否重复
```python
import os
from pathlib import Path
from txdpy import is_num, is_chinese, is_letter, is_Bletter, is_Sletter, is_num_letter


def avfile_name_id_draw(input_file_neme):
    """
    这是一个AV电影ID提取的程序
    :param input_file_neme: 输入你的文件的name
    :return: 返回截取后的new_name
    """

    if "-" in input_file_neme:  # 判断是否包含分隔符

        # 过滤字符
        #     input_file_neme = input_file_neme.replace(',', '').replace('，', '').replace(' ', '').replace('VIP-', '')
        wzzb = input_file_neme.find('-')
        # print(wzzb)

        # 分隔符之前的字符处理
        str_fenge_qian = "解决调用局部或临时遍历警告问题"
        numb1 = 0
        while numb1 < wzzb - 1:
            str_fenge_qian = input_file_neme[numb1:wzzb]
            if is_num_letter(str_fenge_qian):  # 判断是否仅包含数字和字母，没有顺序。这一步排除特殊符号,需要安装这个库txdpy
                break
            numb1 += 1

        # 分隔符之后的字符处理
        str_fenge_hou = "解决调用局部或临时遍历警告问题"
        numb2 = wzzb + 2
        while numb2 < 30:
            str_fenge_hou = input_file_neme[wzzb + 1:numb2]
            if is_num(str_fenge_hou):
                pass
            else:
                str_fenge_hou = input_file_neme[wzzb + 1:numb2 - 1]
                # print("纯数字是:" + str_fenge_hou)
                break
            numb2 += 1
            str_fenge_hou = input_file_neme[wzzb + 1:numb2 - 1]

            # 整合显示结果

        outfile_neme = str_fenge_qian + "-" + str_fenge_hou
        return outfile_neme


def write_txt(strs, txt_name="logs"):
    """
        将文本写入txt
    """
    file = open(txt_name, 'a', encoding='UTF-8')
    file.write(strs)
    file.close()


def file_list(path, extension):
    """
        遍历path下,某个类型的文件,并生产一个list.注意不含子目录
    """

    files_list = os.listdir(path)  # 当前目录所有文件的序列
    vido_list = [s for s in files_list if extension in s]
    return vido_list


def lisbhstr(instr, datapath):
    """
    判断输入的字符串instr，是否包含在索引datapath目录
    :param instr:的字符串instr
    :param datapath:索引datapath目录
    :return:返回instr字符串在，datapath目录所有文件名中出现的次数
    """

    # 这个是from pathlib import Path模块的方法
    datadir = Path(datapath)
    all_list = [file.name for file in datadir.rglob("*.*")]

    pokes_list = [s for s in all_list if instr in s]  # 找出所有搜索结果
    cishu = len(pokes_list)  # 获取所有元素个数

    if cishu > 0:
        print(pokes_list)
        print(instr, "文件已经存在")
        txt_file = open("logs.txt", 'w', encoding='UTF-8')
        txt_file.write(instr + "文件已经存在\n")
        txt_file.close()
    if cishu > 1:
        print(instr, "文件重复")
        txt_file = open("logs.txt", 'a', encoding='UTF-8')
        txt_file.write(instr + "文件重复重复重复重复重复重复重复重复重复重复\n")
        txt_file.close()
    return cishu


def guolvhaha(lists):
    """
    过滤掉一个列表中的非法字符
    """
    # lists = ["woshinidaye$123456", "abc-123456", "woshinidaye-123456欧美", "woshinidaye三级.123456"]
    ffstr_list = ["欧美", "国产", "韩国", "香港", "三级", "$"]  # 将这些视为非法字符
    nowlist=[]
    for vido in lists:
        # print(vido)
        for ffstr in ffstr_list:  # 遍历出需要过滤的字符
            if ffstr in vido or "-" not in vido:  # 如果出现非法字符，则tiaoguo
                # print(vido,"buguize")
                continue
            else:
                # print(vido)
                if vido not in nowlist:
                    nowlist.append(vido)
                    return nowlist



vido_list = file_list(os.getcwd(), "mp4")  # 需要检查的目录
vido_list = guolvhaha(vido_list)		#过滤非法字符

for vido in vido_list:
    vido = avfile_name_id_draw(vido)  # 当前目录截取后的vido-name
    result = lisbhstr(vido, r"D:\indexes")

```
### 10.过滤列表的字符

```python
def guolvhaha(lists):
    """
    过滤掉一个列表中的非法字符，并生成新的list
    """
    # lists = ["woshinidaye$123456", "abc-123456", "woshinidaye-123456欧美", "woshinidaye三级.123456"]
    ffstr_list = ["欧美", "国产", "韩国", "香港", "$"]  # 将这些视为非法字符
    nowlist = []
    for vido in lists:
        # print(vido)
        for ffstr in ffstr_list:  # 遍历出需要过滤的字符
            if (ffstr in vido) or ("-" not in vido):  # 满足一个条件就跳过本次循环
                # print(vido,"buguize")
                continue
            else:
                # print(vido)
                if vido not in nowlist:
                    nowlist.append(vido)
                    return nowlist


lists = ["woshinidaye$123456", "abc-123456", "woshinidaye-123456欧美", "woshinidaye.123456"]
heihei = guolvhaha(lists)
print(heihei)

```
### 11.删除空目录

```python

import os
import shutil


def path_kong(path_1):
    dirs = os.listdir(path_1)
    # print(dirs)

    for dir in dirs:
        # print(dir)
        path_2 = str(path_1 + "\\" + dir)
        # print(path_2)

        # 判断是否为目录
        if os.path.isdir(path_2):
            # 判断目录是否为空
            if not os.listdir(path_2):
                print(dir, "这个是空目录")
                path_3 = str(path_1 + "\\" + dir)

                # 删除目录，目录必须为空
                pokes=shutil.rmtree(path_3)
                print("目录："+dir+"删除成功")




path_1 = os.getcwd()
path_kong(path_1)
```