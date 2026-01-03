import re, os


# 遍历文件及子文件

def file_list(path, extension):
    """
        遍历path下,某个类型的文件,并生产一个list.注意不含子目录
    """
    files_list = os.listdir(path)  # 当前目录所有文件的序列
    vido_list = [s for s in files_list if extension in s]
    return vido_list


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
    all_list = file_name_list(inpath)
    list = []
    for vido_name in all_list:
        if "mp4" or "mkv" or "avi" in vido_name:
            result = re.findall(r'[a-zA-Z]{2,10}-\d+', vido_name)
            for fanhao in result:
                fanhao = fanhao.upper()
                # print(fanhao)
                if fanhao not in list:
                    # print(fanhao)
                    list.append(fanhao.upper())
    # print(list)
    return list


def avipath_nameid_bt(inpath):
    all_list = file_name_list(inpath)
    list = []
    for vido_name in all_list:
        if "mp4" or "mkv" or "avi" in vido_name:
            result = re.findall(r'[a-zA-Z]{2,10}-\d+', vido_name)
            for fanhao in result:
                fanhao = fanhao.upper()
                # print(fanhao)
                if fanhao not in list:
                    # print(fanhao)
                    list.append(fanhao.upper())
    # print(list)
    return list


# avipath_nameid(r"F:\AV2021\41-已筛选")

bt_list = avipath_nameid_bt(R"BTDATA")  # 需要检查的目录
# print(bt_list)
data_list = avipath_nameid(r"D:\indexes")

for btzz in bt_list:
# print(btzz)
    linshi_list = [s for s in data_list if btzz in s]
    cishu = len(linshi_list)
    if cishu == 1:
        file = open("chongfu_logs.txt", 'a', encoding='UTF-8')
        print(btzz, "文件重复")
        file.write(btzz + "警告：文件重复，文件重复，文件重复\n")
        file.close()

input('Press Enter to exit...')
