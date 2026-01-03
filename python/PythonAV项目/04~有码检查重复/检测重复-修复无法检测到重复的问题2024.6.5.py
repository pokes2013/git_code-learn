import os
import re


def file_video_list(dir):
    """
        遍历dir路径下,所有视频文件.含子目录，最终结果只显示文件名
    # """
    files_list = []
    for parent, dirnames, filenames in os.walk(dir):
        for filename in filenames:
            # print(filename)
            # file_path = os.path.join(parent, filename)    #显示绝对路径
            # if filename not in files_list:  # 这里有个去重复的判断

            s = filename.split(".")
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
                if ("制作" not in filename and "合集" not in filename and
                        "两个" not in filename and "合并" not in filename and
                        "作品" not in filename and "都要" not in filename):
                    filename = filename.upper()
                    files_list.append(filename)
    # print(files_list)        #所有文件的绝对路径
    return files_list


def get_id(video_list):  # txt提取番号
    """
    输入视频列表，提取ID后，最终返回一个列表files_list
    注意提取的列表没有扩展名，类似：['SKY-157', 'RGD-155', 'ABW-129']
    """
    files_list = []

    for video in video_list:

        # 从路径中提取文件名，类似：IPZ-762-U字幕制作合计.mp4
        video_name = os.path.basename(video)
        # print(video_name)

        # 正则过滤出番号，类似：IPZ-762-U
        pattern = r'[a-zA-Z]{2,10}-\d{3,10}'
        match = re.match(pattern, video_name, flags=0)
        if match:
            video_name = match.group()
            # 这里转换大写并去重，之后写入上面的空列表中files_list
            files_list.append(video_name)
    return files_list


def find_duplicates(lst):
    """
    当前需要检测的目录有重复时，跟索引没有关系
    """
    # 使用set来过滤掉重复元素，然后找出原列表中的重复元素
    unique_elements = set(lst)
    return [item for item in lst if item in unique_elements and lst.count(item) > 1]


# 当前目录下所有视频文件list

video_list1 = file_video_list(r"E:\\")
video_list2 = file_video_list(r"f:\\")
video_list3 = file_video_list(r"\\10.10.30.97\d")
video_list4 = file_video_list(r"\\10.10.30.97\e")
video_list5 = file_video_list(r"\\10.10.30.97\f")
video_list6 = file_video_list(r"\\10.10.30.98\d")
video_list7 = file_video_list(r"\\10.10.30.98\e")
video_list8 = file_video_list(r"\\10.10.30.98\f")
video_list9 = file_video_list(r"\\10.10.30.99\d")
video_list10 = file_video_list(r"\\10.10.30.99\e")

videos_all_list = (video_list1 + video_list2 + video_list3 + video_list4 + video_list5
                   + video_list6 + video_list7 + video_list8 + video_list9 + video_list10)

# 当前目录下所有视频文件的id_list
id_list = get_id(videos_all_list)
# print(video_list)

# 检测自身的重复,并生成列表
zi_video_db_list = find_duplicates(id_list)

# 列表去重
new_zi_video_db_list = list(set(zi_video_db_list))
print(new_zi_video_db_list)

for videos in new_zi_video_db_list:

    if "SIS-037" not in videos and \
            "TG-2022" not in videos and \
            "IPZ-762" not in videos and \
            "JUSD-671" not in videos and \
            "OFJE-212" not in videos and \
            "FCDSS-021" not in videos:
        # "FCDSS-021" not in videos and \
        # "AKA-014" not in videos and \
        # "RED-208" not in videos and \
        # "EYAN-007" not in videos and \
        # "RED-192" not in videos and \
        # "JOB-001" not in videos and \
        # "JOB-008" not in videos and \
        # "MXGS-102" not in videos and \
        # "UFD-061" not in videos and \
        # "BF-014" not in videos and \
        # "RED-208" not in videos:

        print(videos, "警告：文件重复，文件重复！！！！！")
        with open("cf_logs2024.6.5.csv", "a", encoding="utf-8") as file:
            # with语句需要加入换行
            file.write(videos + "\n")
