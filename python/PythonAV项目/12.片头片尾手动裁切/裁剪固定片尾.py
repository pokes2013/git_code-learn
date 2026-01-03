
import os, sys,time


# 获取当前目录

path=os.getcwd()

#创建logs文件和目录

source_file = "source_data"
isExists = os.path.exists(source_file)
if not isExists:
    os.makedirs(source_file)
    print (source_file+' 创建成功')

# 过滤视频文件

file_list = os.listdir(path)   #当前目录所有文件的序列
vido_list = [s for s in file_list if '.mp4' in s]   #当前目录所有MP4文件


# 片尾时长
pw_time = 1.8

# 获取视频时长函数
def get_video_times(video_path):
    """
    pip install moviepy
    获取指定的视频时长

    """
    from moviepy.editor import VideoFileClip
    video_clip = VideoFileClip(video_path)
    durantion = video_clip.duration
    video_clip.reader.close()
    video_clip.audio.reader.close_proc()
    return durantion

def time_convert(seconds):
    """
        将秒换成合适的时间，如果超过一分钟就换算成"分钟:秒",如果是小时，就换算成"小时:分钟:秒"单位换算
    """
    print(f'时间换算{seconds}')
    M,H = 60,3600
    if seconds < M:
        return f'00:00:0{seconds}' if seconds < 10 else f'00:00:{str(seconds)}'
    elif seconds < H:
        _M = int(seconds/M)
        _S = int(seconds%M)
        return f'00:{f"0{_M}" if _M < 10 else str(_M)}:{f"0{_S}" if _S < 10 else str(_S)}'
    else:
        _H = int(seconds/H)
        _M = int(seconds%H/M)
        _S = int(seconds%H%M)
        return f'{f"0{_H}" if _H < 10 else str(_H)}:{f"0{_M}" if _M < 10 else str(_M)}:{f"0{_S}" if _S < 10 else str(_S)}'






for vido in vido_list:
    vidotime_miao=get_video_times(vido)                 #调用函数get_video_times获取时长，获取得单位为秒
    vidotime_biaozhun= time_convert(vidotime_miao)      #将获取的时长转换为标准格式，例如：01:26:31
    print(vidotime_biaozhun)
    print(vido,"时长:",vidotime_biaozhun)











# length:时长
# def caijian_pw(pw_time):





