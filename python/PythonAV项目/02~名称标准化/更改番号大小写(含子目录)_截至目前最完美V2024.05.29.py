import os
from os import path


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

                # # 统计字母次数,字母次数超过一定次数则视为不规则,例如欧美
                total_letters = count_letters(path)
                if "-" in path and total_letters < 90:
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
    return zz_path


for old_name in vido_any():
    """
        判断部分还需要完善
    """

    result = up_name(old_name)
    # os.renames(old_name, result)
    print("更改成功\n" + old_name + "\n" + result + "\n" * 1)
