import os,time


# 转码函数
def zhuanma(input_video, output_video, speed="veryfast", crf="23", maxrate="2000k", bufsize="3000k"):
    """
    使用注意事项：
    input_video 输入文件，是一个绝对路径，所以在使用必须保证文件路径存在
    out_video 输出文件，是一个绝对路径，所以在使用必须保证文件路径存在
    speed 转码速度默认采用最快速度
    crf 视频质量默认23
    maxrate 平均码率默认2000K
    bufsize 振幅码率默认3000K

    :return:

        无
    """

    zhuan = (
        "ffmpeg -i {input_video} -vcodec h264 -preset {speed} -crf {crf} -maxrate {maxrate} -bufsize {bufsize} -vf scale=1280:-2 -r 29.97 {output_video}"
        .format(input_video=input_video, speed=speed, crf=crf, maxrate=maxrate, bufsize=bufsize, output_video=output_video))

    print(zhuan)
    os.system(zhuan)



def video_scan(pathss=os.getcwd()):
    """
         此函数是遍历视频文件，请输入您的路径，遍历出的结果不包含子目录，并生成一个list
    """
    # 当前目录所有文件的序列
    file_list = os.listdir(pathss)
    vido_list = [s for s in file_list if '*' in s]  # 当前目录所有MP4文件
    # print(vido_list)

    list_vido_any = []
    # 列表中的字母须小写
    kzhan_list = ["mp4", "avi", "wmv", "rmvb", "mov", "mkv"]

    for vido_path in os.listdir(os.chdir(pathss)):


            # 以点为分隔符，分割文件名和扩展名
            # s为路径+文件名，不含扩展名
            s = vido_path.split(".")
            # ss为扩展名，这里统一使用小写
            ss = s[len(s) - 1].lower()
            for kzhan in kzhan_list:

                if ss == kzhan:
                    list_vido_any.append(vido_path)



    # print(list_vido_any)
    return list_vido_any





# 判断OK文件是否存在

def create_directory_if_not_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


# 判断输出文件夹是否存在，不存在则创建
if_out_dir = "ok"
create_directory_if_not_exists(if_out_dir)

if_source_dir = "source_data"
create_directory_if_not_exists(if_source_dir)

# 获取当前目录下的视频文件
list_vido_any = video_scan()
for i in list_vido_any:

    print(i)
# print(list_vido_any)



# 遍历此列表，逐个处理

for video in list_vido_any:
    # 绝对路径
    video_dir = os.path.dirname(video)
    # 从绝对路径中提取完整文件名
    video_name = os.path.basename(video)
    # 截取文件名的扩展名MP4
    video_name_kz = video_name.split(".")[-1]
    # 不带扩展名的文件名abc-123
    video_name_notkz = os.path.splitext(video_name)[0]

    # 拼接in_video
    # in_video = "'" + video + "'"
    in_video = video_name


    # 拼接out_video
    out_videos = video_name_notkz + "_h264" + ".mp4"


    # 转码

    zhuanma(video, out_videos)

    # 移动文件

    os.system("move {out_videos} {if_out_dir} >nul".format(out_videos=out_videos, if_out_dir=if_out_dir))
    os.system("move {in_video} {if_source_dir} >nul".format(in_video=in_video, if_source_dir=if_source_dir))



    # 休息300秒
    xiuxi = 300
    while xiuxi > 0:
        print("程序休息300秒倒计时：", xiuxi, "秒")
        xiuxi -= 1
        time.sleep(1)
        os.system('cls')
