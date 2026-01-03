import os
import re


# 遍历所有文件
def file_name_list(dir):
    """
        遍历dir路径下,所有文件.含子目录，最终结果只显示文件名
    """
    files_list = []
    for parent, dirnames, filenames in os.walk(dir):
        for filename in filenames:
            # print(filename)
            # file_path = os.path.join(parent, filename)    #显示绝对路径
            # if filename not in files_list:  # 这里有个去重复的判断
            files_list.append(filename)
    # print(files_list)        #所有文件的绝对路径
    return files_list


# 从list中过滤出视频文件

def video_list(full_list):
    videos = []

    for video in full_list:
        s = video.split(".")
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
            videos.append(video)

    return videos


# 提取番号
def get_id(video_list):  # txt提取番号
    """
    输入视频列表，提取ID后，最终返回一个列表files_list
    注意提取的列表没有扩展名，类似：['SKY-157', 'RGD-155', 'ABW-129']
    """
    files_list = []

    for video in video_list:

        if "两个" not in video_list or "制作" not in video_list or "都要" not in video_list:

            # 从路径中提取文件名，类似：IPZ-762-U字幕制作合计.mp4
            video_name = os.path.basename(video)
            # print(video_name)

            # 正则过滤出番号，类似：IPZ-762-U
            pattern = r'[a-zA-Z]{2,10}-\d{3,10}'
            match = re.match(pattern, video_name, flags=0)
            if match:
                video_name = match.group()
                # 这里转换大写并去重，之后写入上面的空列表中files_list
                if video_name not in files_list:
                    video_name.upper()
                    files_list.append(video_name)
    return files_list


# 判断文件夹是否存在
def if_folder(path_name):  # 判断文件夹是否存在

    """
    判断文件夹是否存在，如果不存在则递归创建
    """

    if os.path.exists(path_name):
        # 目录存在则开始创建索引文件
        print(path_name, "路径已存在")
    else:
        # 创建多级路径的方法，目录不存在则先创建
        os.makedirs(path_name)
        print(path_name, "路径已创建")


# 日志系统
def mydoc(str):
    with open("data.csv", "a", encoding="utf-8") as file:
        # with语句需要加入换行
        file.write(str + "\n")


def chuang(path, sy_folder):
    # 获取所有文件list
    file_list = file_name_list(path)
    # 获取视频文件list
    video_lists = video_list(file_list)
    # 获取番号列表
    video_id = get_id(video_lists)

    sy_path = r"D:\indexes"

    save_path_name = sy_path + "\\" + sy_folder

    if_folder(save_path_name)

    for video in video_id:
        path_pokes = sy_path + "\\" + sy_folder + "\\" + video + ".mp4"

        # 写入文件
        with open(path_pokes, "w", encoding="UTF-8") as file:
            file.write(video)
            print(path_pokes, "写入成功")



# 调用
chuang(r"e:\\", "ALL")
chuang(r"F:\AV2021", "ALL")
chuang(r"\\10.10.30.97\d", "ALL")
chuang(r"\\10.10.30.97\e", "ALL")
chuang(r"\\10.10.30.97\f", "ALL")
chuang(r"\\10.10.30.98\d", "ALL")
chuang(r"\\10.10.30.98\e", "ALL")
chuang(r"\\10.10.30.98\f", "ALL")
chuang(r"\\10.10.30.99\d", "ALL")
chuang(r"\\10.10.30.99\e", "ALL")

print("索引创建完成")
