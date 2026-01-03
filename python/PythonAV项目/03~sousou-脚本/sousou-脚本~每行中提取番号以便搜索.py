import os
import re

"""
此程序是一个更改文件名的程序。将文本中的绝对路径的文件名，字母改为小写
"""


def txt_list(data):
    """
    逐行读取txt文件，将其变为一个列表
    """
    list_vido_any = []
    list_vido_any.clear()
    with open(data, 'r', encoding='UTF-8') as file:
        # print(file.readline())
        for line in file:
            line = line.rstrip('\n')
            list_vido_any.append(line)
    # print(list_vido_any)
    return list_vido_any


# 写入文本
def mytxt(str):
    # 打开或创建文件
    file = open("sousou~已处理.txt", "a", encoding="utf-8")
    # 写入内容
    file.write(str)
    # 关闭文件
    file.close()


import os.path


def iffile(file_path):
    # 文件路径

    # 判断文件是否存在
    if os.path.exists(file_path):
        print(f"文件 {file_path} 存在。")
        os.remove("sousou~已处理.txt")

    else:
        print(f"文件 {file_path} 不存在。")


# 判断上次遗留文件
iffile("sousou~已处理.txt")

for old_name in txt_list("sousou.txt"):

    pattern = r'[a-zA-Z]{2,10}-\d{3,10}'
    match = re.match(pattern, old_name, flags=0)
    if match:
        video_name = match.group()
        # 拼接
        video_name = video_name + "|"

        # fff = video_name.split("-")
        # print(video_name)
        mytxt(video_name)

# 删除最后一个"|" 便于搜索
with open("sousou~已处理.txt", "r", encoding="utf-8") as file:
    first_line = file.readline()[:-1]
    # print(first_line)

    with open("sousou~已处理.txt", "w", encoding="utf-8") as file2:
        file2.write(first_line)

# 二次追加写入源文件的一些信息
#################################

with open("sousou~已处理.txt", "a", encoding="utf-8") as file:
    file.write("\n" * 3)
    file.write("详细信息：\n")
    file.write("#" * 50)

for old_name in txt_list("sousou.txt"):
    if ("搜寻" not in old_name and
            "搜寻" not in old_name and
            "全部" not in old_name and
            "发布" not in old_name and
            "热门" not in old_name and
            "女优" not in old_name and
            "类别" not in old_name and
            "中文" not in old_name and
            "Terms" not in old_name and
            "Copyright " not in old_name and
            "页" not in old_name and
            "搜寻" not in old_name):
        old_name = old_name + "\n"

        with open("sousou~已处理.txt", "a", encoding="utf-8") as file:
            file.write(old_name)

        file = open("sousou~已处理.txt", "a", encoding="utf-8")

        file.write(old_name)

        print(old_name)
