import os, sys


def dx_name(str_name):
    # 定位分隔符
    wzzb = str_name.find("-")

    # 截取字母
    str_fenge_qian = str_name[:wzzb]

    # 转大写
    str_fenge_qian = str_fenge_qian.upper()

    # 截取分隔符后面的字符
    str_fenge_hou = str_name[wzzb:]

    # 拼接最终效果

    zz_name = str_fenge_qian + str_fenge_hou
    return zz_name


def file_name_list(dir):
    """
    遍历dir路径下,所有文件.含子目录，最终结果只显示文件名
    """
    files_list = []
    for parent, dirnames, filenames in os.walk(dir):
        for filename in filenames:
            # print(filename)
            file_path = os.path.join(parent, filename)  # 显示绝对路径
            # print(file_path)
            if file_path not in files_list:  # 这里有个去重复的判断
                files_list.append(file_path)
    print(files_list)  # 所有文件的绝对路径
    return files_list


# file_name_list(r"D:\code\python\10.前缀号大写")


shuaixuan_list = []
geshi_list = [".mp4", ".MP4", ".AVI", ".avi", ".kvm", ".KVM", "-"]
all_list = file_name_list(os.getcwd())
for hzstr in geshi_list:
    sxhvido_list = [s for s in all_list if hzstr in s]
    for sxh_vide in sxhvido_list:
        if sxh_vide not in shuaixuan_list:
            if "-" in sxh_vide:  # 必须包含“-”
                if "欧美" or "法国" not in sxh_vide:  # 继续过滤
                    shuaixuan_list.append(sxh_vide)

# print(shuaixuan_list)


for vido in shuaixuan_list:
    print(vido)
    xname = dx_name(vido)
    os.renames(vido, xname)

    f = open("upname_logs.txt", "a", encoding="UTF-8")
    f.write(vido + " 更新为：" + xname + "\n")
    f.close()
