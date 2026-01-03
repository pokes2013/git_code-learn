# python代码编写汇总



## 01.索引的建立



```python
import os

# # 将文本内的名称转成一个列表
data = "data.txt"        #源文件
# #提取文件名
with open(data,"r", encoding="UTF-8") as f:
    for line in f:
        in_name = os.path.basename(line)
        print(in_name)
        #创建文件
        path = "./suoyin/"
        bname=path+in_name
        out_name =bname.strip('\n')
        print(out_name)
        #
        if os.path.exists(path):
            #目录存在则创建文件
            print("文件创建成功")
            f = open(out_name,"w",encoding="UTF-8")
            f.write(out_name)

        else:
            #不存在则先创建目录
            print("没有suoyin目录，正在创建")
            os.makedirs(path)
            f = open(out_name,"w",encoding="UTF-8")
            f.write(out_name)
```



## 02.检测文件重复



```python

import re, os


def file_name_list(dir):
    """
        遍历dir路径下,所有文件.含子目录，最终结果只显示文件名
    """
    files_list = []
    for parent, dirnames, filenames in os.walk(dir):
        for filename in filenames:
            # print(filename)
            # file_path = os.path.join(parent, filename)    #显示绝对路径
            if filename not in files_list:  # 这里有个去重复的判断
                files_list.append(filename)
    # print(files_list)        #所有文件的绝对路径
    return files_list


def avipath_nameid(inpath):
    """
        提取番号，转换为大写，写入到list列表中
    """
    all_list = file_name_list(inpath)
    list = []
    for vido_name in all_list:
        s = vido_name.split(".")
        ss = s[len(s) - 1]
        if (ss == "mp4" or ss == "MP4" or
                ss == "wmv" or ss == "WMV" or
                ss == "avi" or ss == "AVI" or
                ss == "rmvb" or ss == "rmvb" or
                ss == "rm" or ss == "RM" or
                ss == "mov" or ss == "MOV" or
                ss == "ts" or ss == "TS" or
                ss == "vob" or ss == "VOB" or
                ss == "flv" or ss == "FLV" or
                ss == "m4v" or ss == "M4V" or
                ss == "mkv" or ss == "MKV"):

                result = re.findall(r'[a-zA-Z]{3,10}-\d+', vido_name)
                for fanhao in result:
                    fanhao = fanhao.upper()
                    # print(fanhao)
                    if fanhao not in list:
                        # print(fanhao)
                        list.append(fanhao.upper())
    # print(list)
    return list

# 提取需要检测的路径番号，并转换为大写
vido_list = avipath_nameid(r"e:\\")

# 提取索引路径内的番号，并转换为大写
data_list = avipath_nameid(r"D:\indexes")

# 对比两个列表中的番号，统计次数，如果次数大于1，则重复
for vido_name in vido_list:
    linshi_list = [s for s in data_list if vido_name in s]
    cishu = len(linshi_list)

    if cishu > 1:
        file = open("chongfu_logs.txt", 'a', encoding='UTF-8')
        print(vido_name, "文件重复")
        file.write(vido_name + "警告：文件重复，文件重复，文件重复\n")
        file.close()


input('Press Enter to exit...')
```

### 示例：比较两个列表相同的元素

```python
a = ["Apple", "Banana", "Pear", "Peach"]
b = ["apple", "banana", "pear", "grape"]
 
a = [i.lower() for i in a]
print(a)
b = [i.lower() for i in b]
print(b)


for j in a:
    if j in b:
        print("相同的内容:", j)
```

### 示例：统计一个字符串在列表中出现的次数的函数

```python
# 统计一个字符串在列表中出现的次数的函数
# string_to_count为需要统计次数的字符串
# list_of_strings准备的列表

def count_string_in_list(string_to_count, list_of_strings):
    return sum([s.count(string_to_count) for s in list_of_strings])
 

 
# 示例
list_of_strings = ["apple", "banana", "apple", "cherry", "banana", "apple"]
string_to_count = "apple"
count = count_string_in_list(string_to_count, list_of_strings)
print(f"'{string_to_count}' appears {count} times in the list.")

if count>2 :
	print("chongfu")
```



## 03.更改番号大小写

### 遍历目录下的文件（包含子目录）

```python
def vido_any():
    """
        文件夹下的视频文件，包含子目录 ，显示为绝对路径
    """
    list_vido_any = []
    for vido in os.walk(os.getcwd()):
        for j in vido[2]:
            # i[0]是当前文件夹的绝对路径，j是文件名
            path = os.path.join(vido[0], j)

            s = path.split(".")
            ss = s[len(s) - 1]
            if ss == "mp4" or ss == "avi" or ss == "wmv" or ss == "vm4":
                # print(path)
                list_vido_any.append(path)

    return list_vido_any
```





### 文件名重组

分解源文件名，然后把番号字母部分转为大写，然后再次拼接番号。完成之后还需要拼接路径，拼接成绝对路径。

```python
def up_name(vido_name):
    """
        绝对路径，文件名切片，番号部分转大写，处理完成之后再次拼接成绝对路径
    """

    # 从路径中提取文件名
    path = vido_name.split("\\")
    path_name = path[-1]

    # 处理文件名，提取文件名中的番号部分

    wzzb = path_name.find('-')
    # 截取字母
    str_fenge_qian = path_name[:wzzb]
    # 转大写
    str_fenge_qian = str_fenge_qian.upper()
    # 截取分隔符后面的字符
    str_fenge_hou = path_name[wzzb:]
    # 拼接最终效果
    zz_name = str_fenge_qian + str_fenge_hou
    # 文件路径提取
    path_no_name = os.path.dirname(vido_name)
    # 拼接成绝对路径：
    zz_path = path_no_name + "\\" + zz_name
    # 返回值
    # print(zz_path)
    return zz_path
```



### 函数外部分

使用if判断一下包含"-"，不然会把所有视频含字母都改成大写，判断类型还是不够完善，后续改进。

```
for old_name in vido_any():

    if "-" in old_name:
        result = up_name(old_name)
        # print(result)
        os.renames(old_name, result)
        print("更改成功\n"+old_name+"\n" + result+"\n"*1)
```



后续改进，利用正则表达式，以下这个是日期的过滤

```
[2][0-9].[0-1][1-9].[1-3][0-9]
```







### 最终效果

```python
import os
from os import path

def vido_any():
    """
        文件夹下的视频文件，包含子目录 ，显示为绝对路径
    """
    list_vido_any = []
    for vido in os.walk(os.getcwd()):
        for j in vido[2]:
            # i[0]是当前文件夹的绝对路径，j是文件名
            path = os.path.join(vido[0], j)

            s = path.split(".")
            ss = s[len(s) - 1]

            if (ss == "mp4" or ss == "MP4" or
                    ss == "wmv" or ss == "WMV" or
                    ss == "avi" or ss == "AVI" or
                    ss == "rmvb" or ss == "rmvb" or
                    ss == "rm" or ss == "RM" or
                    ss == "mov" or ss == "MOV" or
                    ss == "ts" or ss == "TS" or
                    ss == "vob" or ss == "VOB" or
                    ss == "flv" or ss == "FLV" or
                    ss == "m4v" or ss == "M4V" or
                    ss == "mkv" or ss == "MKV"):

                # print(path)
                list_vido_any.append(path)

    return list_vido_any


def up_name(vido_name):
    """
        绝对路径，文件名切片，番号部分转大写，处理完成之后再次拼接成绝对路径
    """

    # 从路径中提取文件名
    path = vido_name.split("\\")
    path_name = path[-1]

    # 处理文件名，提取文件名中的番号部分

    wzzb = path_name.find('-')
    # 截取字母
    str_fenge_qian = path_name[:wzzb]
    # 转大写
    str_fenge_qian = str_fenge_qian.upper()
    # 截取分隔符后面的字符
    str_fenge_hou = path_name[wzzb:]
    # 拼接最终效果
    zz_name = str_fenge_qian + str_fenge_hou
    # 文件路径提取
    path_no_name = os.path.dirname(vido_name)
    # 拼接成绝对路径：
    zz_path = path_no_name + "\\" + zz_name
    # 返回值
    # print(zz_path)
    return zz_path


for old_name in vido_any():

    if "-" in old_name:
        result = up_name(old_name)
        # print(result)
        os.renames(old_name, result)
        print("更改成功\n"+old_name+"\n" + result+"\n"*1)
```







## 欧美部分的过滤

### 统计点出现的次数

```
def count_char(str, char):
    count = 0
    for c in str:
        if c == char:
            count += 1
    return count



string = "BLACKED 19.09.02 JIA LISSA AND STACY CRUZ 4K-chongfu_ok.mp4"
character = "."

cishu = count_char(string, character)
print(cishu)

```

以这个思路，写了下面的智能代码，判断是否为欧美。

### 最终效果

```python
import os


def count_letters(s):
    """
    统计字符串中的字母
    """

    # 移除字符串中的空格
    s = s.replace(" ", "")
    # 转换为小写统计
    s = s.lower()
    # 统计每个字母出现的次数
    letter_count = {}
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        letter_count[letter] = s.count(letter)
    # 返回总计数
    return sum(letter_count.values())


def vido_any():
    """
        文件夹下的视频文件，包含子目录 ，显示为绝对路径
    """
    list_vido_any = []
    # for vido in os.walk(os.getcwd()):
    for vido in os.walk(r"E:\avfilm\stacy.cruz"):

        for j in vido[2]:
            # i[0]是当前文件夹的绝对路径，j是文件名
            path = os.path.join(vido[0], j)

            s = path.split(".")
            ss = s[len(s) - 1]

            if (ss == "mp4" or ss == "MP4" or
                    ss == "wmv" or ss == "WMV" or
                    ss == "avi" or ss == "AVI" or
                    ss == "rmvb" or ss == "rmvb" or
                    ss == "rm" or ss == "RM" or
                    ss == "mov" or ss == "MOV" or
                    ss == "ts" or ss == "TS" or
                    ss == "vob" or ss == "VOB" or
                    ss == "flv" or ss == "FLV" or
                    ss == "m4v" or ss == "M4V" or
                    ss == "mkv" or ss == "MKV"):
                # print(path)

                # # 统计字母次数,字母次数超过一定次数则视为不规则,例如欧美
                total_letters = count_letters(path)
                if total_letters > 30:
                    list_vido_any.append(path)

    return list_vido_any


for video_path in vido_any():
    # 从绝对路径中提取完整文件名
    video_name = os.path.basename(video_path)
    # 文件路径提取,用于后面拼接
    video_dir = os.path.dirname(video_path)
    # 截取文件名的扩展名MP4
    video_name_kz = video_name.split(".")[-1]
    # 不带扩展名的文件名abc-123
    video_name_notkz = os.path.splitext(video_name)[0]

    # print(video_name_notkz)

    if "[欧美]" in video_name_notkz:
        video_name_notkz = video_name_notkz.replace("[欧美]", "")
        video_name_notkz = video_name_notkz + "[欧美]."
        new_name_path = video_dir + "\\" + video_name_notkz + video_name_kz
        # print(new_name)
        os.renames(video_path, new_name_path)
        print("更改成功\n" + video_path + "\n" + new_name_path + "\n" * 1)
    else:
        video_name_notkz = video_name_notkz + "[欧美]."
        new_name_path = video_dir + "\\" + video_name_notkz + video_name_kz
        os.renames(video_path, new_name_path)
        # print(new_name_path)

        print("更改成功\n" + video_path + "\n" + new_name_path + "\n" * 1)
```



## 正则表达式的应用

参考这个：https://blog.csdn.net/z099164/article/details/125552308

方法1：返回字符串

```python
import re

text = "abc-123-UC-hahashduasdhaskdhsakdhaksd"
pattern = r'[a-zA-Z]{3,10}-\d+-[a-zA-Z]+'

# 只从字符串的最开始与pattern进行匹配
match = re.match(pattern, text, flags=0)
if match:
    print(match.group())
else:
    pass


# 运行结果：
# abc-123-UC
```

方法2：返回一个列表

```
import re

text = "abc-123-UC-hahashduasdhaskdhsakdhaksd"

result = re.findall(r'[a-zA-Z]{2,10}-\d+', text)
print(result)


# 运行结果：
# ['abc-123']
```



##  过滤的优化函数



```python
def key_filter(data_list, key_list):
    """
    这是一个关键字过滤的函数.
    data_list是需要处理元数据；
    key_list是需要排除的关键字列表
    然后你就可以得到一个过滤之后的list
    """

    for pc_str in key_list:
        for video in data_list:
            if pc_str in video: data_list.remove(video)
            # print(data)
    return data_list


data_list = ["欧美1231212121212", "韩国1231212121212", "abc-123", "abc-456", "abc-567"]
key_list = ["欧美", "韩国"]
pokes = key_filter(data_list, key_list)

print(pokes)


#运行结果：

# ['abc-123', 'abc-456', 'abc-567']
```



### 爬取网页源代码

```python
def html():
    url = input("请输入你的网址:")
    # url = "https://avmoo.online/cn/series/5019cd7b9d64f152"
    # print(url)
    url = url.replace("https", "http")

    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
        "Cookie": "your cookie"}

    response = requests.get(url, headers=header)

    if response.status_code == 200:
        html_content = response.text
        # print(html_content)
        with open("yuadaima.txt", 'w', encoding='UTF-8') as fff:
            fff.write(html_content)
```





## 日志系统

```python
def mytxt(str):

    # 打开或创建文件
    file=open("b.csv","a",encoding="utf-8")
    # 写入内容
    file.write(str+"\n")
    # 关闭文件
    file.close()
    
    
# mytxt("haha")
# mytxt("hehe")
# mytxt("huhu")


def mydoc(str):
    with open("b.csv","a",encoding="utf-8") as file:
        # with语句需要加入换行
        file.write(str+"\n")

mydoc("haha1")
mydoc("hehe2")
mydoc("huhu3")
```



## 常用文件路径切片

因为自己对路径切片这一块不是很熟悉，所以浪费了不少时间，这个是重点。

```python
    
    #绝对路径
    video_path=r“E:\avfilm\stacy.cruz”
    # 从绝对路径中提取完整文件名
    video_name = os.path.basename(video_path)
    # 文件路径提取,用于后面拼接
    video_dir = os.path.dirname(video_path)
    # 截取文件名的扩展名MP4
    video_name_kz = video_name.split(".")[-1]
    # 不带扩展名的文件名abc-123
    video_name_notkz = os.path.splitext(video_name)[0]
```



### 去掉某个字符串之前或者之后的内容

```
name=name.split("<",1)[0]
```

### 将列表直接转为字符串

```
sousuo = '|'.join(list_id_any)
```







### 读取txt进行改名

案例1：

```python
import os

"""
此程序是一个更改文件名的程序。将文本中的绝对路径的文件名，字母改为小写
"""


def txt_list():
    """
    逐行读取txt文件，将其变为一个列表
    """
    list_vido_any = []
    list_vido_any.clear()
    with open('data.txt', 'r', encoding='UTF-8') as file:
        # print(file.readline())
        for line in file:
            line = line.rstrip('\n')
            list_vido_any.append(line)
    # print(list_vido_any)
    return list_vido_any


for old_name in txt_list():
    # print(old_name)
    now_name = old_name.lower()
    # print(now_name)
    os.renames(old_name, now_name)
    print("更改成功：\n" + old_name + "\n" + now_name + "\n"*2)
    
```



案例2：

```python
import os

"""
此程序是一个更改文件名的程序。将文本中的绝对路径的文件名，字母改为小写
"""


def txt_list():
    """
    逐行读取txt文件，将其变为一个列表
    """
    list_vido_any = []
    list_vido_any.clear()
    with open(r'D:\systemdoc\desk\666\data.txt', 'r', encoding='UTF-8') as file:
        # print(file.readline())
        for line in file:
            line = line.rstrip('\n')
            list_vido_any.append(line)
    # print(list_vido_any)
    return list_vido_any


for old_name in txt_list():
    # 得到源文件名和路径
    print(old_name)

    # 替换其中的文本
    new_name = old_name.replace("[动漫][动漫]", "[动漫]")
    #执行修改
    os.renames(old_name, new_name)
    print("更改成功：\n" + old_name + "\n" + new_name + "\n"*2)

  
```



## 列表直接转为字符串

```python
list1 = ['a', 'b', 'c']
string1 = ''.join(list1)
print(string1)  # 输出: 'abc'
 
string2 = '-'.join(list1)
print(string2)  # 输出: 'a-b-c'
```



### 截取两个字符串之间的内容

```python
def extract_string_between_symbols(text, start_symbol, end_symbol):
    pattern = f"{start_symbol}(.*?){end_symbol}"
    match = re.search(pattern, text)
    if match:
        return match.group(1)
    else:
        return None
```







爬取项目



提取多页avmoo的网页地址和页码名称

```python
def get_duoye_url_list(url):
    aburl_list = []
    com = "https://avmoo.online/"
    url = url.replace("https", "http")
    # print(url)

    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
        "Cookie": "your cookie"}

    response = requests.get(url, headers=header)
    if response.status_code == 200:
        html_content = response.text

        # 页码和章节提取，这里需要注意的是re.findall提取标签之间的内容，没有标签是不行的，返回的结果是一个list
        yema_list = re.findall('<a name="numbar"  href=".*?">.*?</a>', html_content)

        for yema in yema_list:
            # print(yema)
            yema_url = extract_string_between_symbols(yema, '/', '">')
            zhangjie = extract_string_between_symbols(yema, ">", "<")

            aburl = com + yema_url
            aburl_list.append(aburl)
            # print(yema_url)
            # print(zhangjie)
            # print(aburl)
    else:
        print("无法访问")
    return aburl_list
```















最终成品备份：爬取专辑页面信息

```python
import re

import requests


def extract_string_between_symbols(text, start_symbol, end_symbol):
    pattern = f"{start_symbol}(.*?){end_symbol}"
    match = re.search(pattern, text)
    if match:
        return match.group(1)
    else:
        return None


def get_duoye_url_list(url):
    aburl_list = []
    com = "https://avmoo.online/"
    url = url.replace("https", "http")
    # print(url)

    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
        "Cookie": "your cookie"}

    response = requests.get(url, headers=header)
    if response.status_code == 200:
        html_content = response.text

        # 页码和章节提取，这里需要注意的是re.findall提取标签之间的内容，没有标签是不行的，返回的结果是一个list
        yema_list = re.findall('<a name="numbar"  href=".*?">.*?</a>', html_content)

        for yema in yema_list:
            # print(yema)
            yema_url = extract_string_between_symbols(yema, '/', '">')
            zhangjie = extract_string_between_symbols(yema, ">", "<")

            aburl = com + yema_url
            aburl_list.append(aburl)
            # print(yema_url)
            # print(zhangjie)
            # print(aburl)
    else:
        print("无法访问")
    return aburl_list


# get_duoye()

def html_danye(url,xrfs):
    """
    获取网页源代码，写入到yuadaima.txt
    xrfs为写入方式
    """
    # url = input("请输入你的网址:")
    # url = "https://avmoo.online/cn/series/5019cd7b9d64f152"
    # print(url)
    htmlurl = url.replace("https", "http")

    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
        "Cookie": "your cookie"}

    response = requests.get(htmlurl, headers=header)

    if response.status_code == 200:
        html_content = response.text
        # print(html_content)
        with open("yuadaima.txt", xrfs, encoding='UTF-8') as fff:
            fff.write(html_content)


def tiqu_yuandaima():
    list_title = []
    list_vido_info = []
    list_id_any = []
    with open("yuadaima.txt", 'r', encoding='UTF-8') as file:
        print(file.readline())
        for line in file:
            line = line.rstrip('\n')
            if "<title>" in line:
                title = extract_string_between_symbols(line, "<title>", "</title>")
                list_title.append(title)

            if "<span>" in line:
                # name = extract_string_between_symbols(line, "<span>", "</span>")
                name = extract_string_between_symbols(line, "<span>", "<")
                # name = name.split("<", 1)[0]
                print(name)
                id_fanhao = extract_string_between_symbols(line, "<date>", "</date>")
                date = extract_string_between_symbols(line, "/ <date>", "</date></span>")
                id_name = id_fanhao + "~" + name + "~" + date
                list_vido_info.append(id_name)

                id_pokes = id_name.split("~")[0:1]
                id_pokes = ''.join(id_pokes)
                list_id_any.append(id_pokes)

    # 写入title的信息
    title = ''.join(list_title)
    with open("yuadaima-已处理.txt", 'a', encoding='UTF-8') as file:
        # print(title)
        file.write(title)
        file.write("\n" * 2)

    # 写入搜索的信息
    sousuo = '|'.join(list_id_any)
    with open("yuadaima-已处理.txt", 'a', encoding='UTF-8') as file:
        print(sousuo)
        file.write(sousuo)
        file.write("\n" * 3)
        file.write("*" * 60)
        file.write("\n" * 3)

    # 写入每一行的详细信息
    for avinfo in list_vido_info:
        if "【VR】" not in avinfo:
            with open("yuadaima-已处理.txt", 'a', encoding='UTF-8') as file:
                print(avinfo)
                file.write(avinfo + "\n")


# url = input("请输入网址：")
# url="https://avmoo.online/cn/series/6b127c02eff776a4"
# url = "https://avmoo.online/cn/series/ee211f0c5b9207c6"
url = "https://avmoo.online/cn/series/6b127c02eff776a4"

yemalist = get_duoye_url_list(url)
if len(yemalist) > 0:
    print(yemalist)
    print("多页处理中，请稍后")
    #     # 多页追加写入到yuandaima.txt
    for url in yemalist:
        html_danye(url,"a")
    tiqu_yuandaima()
else:
    print("只有1页，正在处理")
    html_danye(url,"w")
    tiqu_yuandaima()

# yemalist = get_duoye_url_list(url)
# print(yemalist)
# https://avmoo.online/cn/series/6b127c02eff776a4

```





## 遍历文件











### 包含子目录

```python
import os


def video_scan(pathss=os.getcwd()):
    """
         此函数是遍历视频文件，遍历出的结果包含目录和子目录，并生成一个list
    """
    list_vido_any = []
    # 列表中的字母须小写
    kzhan_list = ["mp4", "avi", "wmv", "rmvb", "mov", "mkv"]
    # 列表中的字母转为大写
    up_kzhan_list = [item.upper() for item in kzhan_list]
    for vido in os.walk(pathss):
        for j in vido[2]:
            # 遍历所得的所有文件，包含子目录的文件，i[0]是当前文件夹的绝对路径，j是文件名
            path = os.path.join(vido[0], j)

            s = path.split(".")   # 以点为分隔符，分割文件名和扩展名，s为路径+文件名，不含扩展名
            ss = s[len(s) - 1]   # ss为扩展名

            # 小写循环写入
            for kzhan in kzhan_list:
                if ss == kzhan:
                    list_vido_any.append(path)
            # 大写循环写入
            for up_kzhan in up_kzhan_list:
                if ss == up_kzhan:
                    list_vido_any.append(path)

    return list_vido_any
```



### 不包含子目录

```python

方法1：
def get_video(videopath):
    """
         此函数是遍历视频文件，请输入您的路径，遍历出的结果包含子目录，并生成一个list
    """
    
    # 定义视频文件扩展名列表
    video_extensions = ['mp4', 'avi', 'mov', 'mkv', 'wmv', 'flv']
    # 准备一个空的列表用来存储视频文件
    video_list = []

    # 遍历当前目录下的所有文件
    for filename in os.listdir(videopath):
        # 获取文件扩展名
        extension = filename.split('.')[-1].lower()
        # 检查文件是否为视频文件
        if extension in video_extensions:
            video_list_ALL.append(filename)

    return video_list


get_video(r"e:\\")

方法2

def get_videofile(path):

    # 常见视频格式的文件扩展名
    video_extensions = ['.mp4', '.avi', '.mov', '.wmv', '.mpg', '.mkv', '.flv']

    # 获取当前目录下的所有文件
    current_directory_files = os.listdir(path)

    # 过滤出视频文件
    video_files_list = [f for f in current_directory_files if os.path.splitext(f)[1].lower() in video_extensions]
    return video_files_list

方法3：最完美的


import os

def get_video(pathss = os.getcwd()):
    """
    遍历当前目录下的视频文件作为输入文件，并且拼接出：输出文件
    :param pathss: 工作目录
    :return: 返回一个字典
    """
    file_list = os.listdir(pathss)
    my_dict = {}
    kzhan_list = ["mp4", "avi", "wmv", "rmvb", "mov", "mkv"]

    for vido_path in file_list:
        ss = vido_path.split(".")[-1].lower()   # 以点为分隔符取扩展名，并统一转为小写
        for kzhan in kzhan_list:
            if ss == kzhan:
                videoname_list = vido_path.split('.')   #由于文件名中有点，扩展名中也有点，所有以下两行修复类似 abc-123.hevc.mp4
                del videoname_list[-1]      #删除最后一个元素.mp4
                notkuozhan_video_name = '.'.join(videoname_list)  #将list再次以点拼接，并转换成str
                out_videos = notkuozhan_video_name + "_h264" + ".mp4"
                my_dict.setdefault(vido_path, out_videos)   #以键值对写入字典
    #
    print(my_dict)
    return my_dict

get_video(pathss=r"e:\\")



```



## 字典的遍历

```
for key, value in video_dict.items():
    print(key, value)
```



## OS模块

提取文件名前缀

例如：abc-124.mp4，可以提取abc-123

```
os.path.splitext(name_str)[0]
```

替换字符

```
str.replace(" ", "~")
```









```python
import os



# abspath 绝对路径

path = os.path.abspath(__file__)  # 当前运行python文件的绝对路径，abspath绝对路径
print(path)
# 运行结果：
# D:\systemdoc\desk\python模块OS\demo001.py


# dirname 上一级目录
root_path = os.path.dirname(__file__)  # 当前运行python文件的上一级目录，即当前运行 python文件的所在目录
print(root_path)
# 运行结果：
# D:\systemdoc\desk\python模块OS


# 路径拼接

file_path = os.path.join(root_path, 'pokes', 'day')
print(file_path)
# 运行结果：
# D:\systemdoc\desk\python模块OS\pokes\day


# 判断目录是否存在，不存在则创建
if not os.path.exists(file_path):   # exists 判断文件是否存在
    os.makedirs(file_path)      # makedirs支持递归创建
    print('目录不存在，已经创建')
# 运行结果：
# 目录不存在，已经创建

*************************************************************


# 遍历当前目录下的文件
import os

root_path = os.path.dirname(__file__)
name_list = os.listdir(root_path)  # listdir 仅遍历1级目录和文件，并且运行结果中目录和文件是混在一起的
print(name_list)

# isdir判断是不是目录
for file in name_list:
    if not os.path.isdir(file):  # 除去目录剩下的都是文件
        print(file)

```







