# 视频批量压缩
# 作者：pokes@163.com
# 最后更新时间：2024.6.26
# 程序必须安装python，ffmpeg，ffmpeg必须加入系统环境变量
# 版本v1.0


import os
import subprocess
import time


class video:

    def __init__(self, name):
        self.name = name

    def get_video(self, pathss=os.getcwd()):
        """
        遍历当前目录下的视频文件作为输入文件，并且拼接出：输出文件
        :param pathss: 工作目录
        :return: 返回一个字典
        """
        file_list = os.listdir(pathss)
        my_dict = {}
        kzhan_list = ["mp4", "avi", "wmv", "rmvb", "mov", "mkv"]

        for vido_path in file_list:
            ss = vido_path.split(".")[-1].lower()  # 以点为分隔符取扩展名，并统一转为小写
            for kzhan in kzhan_list:
                if ss == kzhan:
                    videoname_list = vido_path.split('.')  # 由于文件名中有点，扩展名中也有点，所有以下两行修复类似 abc-123.hevc.mp4
                    del videoname_list[-1]  # 删除最后一个元素.mp4
                    notkuozhan_video_name = '.'.join(videoname_list)  # 将list再次以点拼接，并转换成str

                    out_videos = notkuozhan_video_name + "_h264" + ".mp4"
                    my_dict.setdefault(vido_path, out_videos)  # 以键值对写入字典
        print(my_dict)
        return my_dict

    def run_zhuanma(self, fbl, input_video, output_video):
        if fbl == 0:
            cmd = (
                "ffmpeg -i {input_video} -vcodec h264 -preset veryfast -crf 23 -maxrate 2000k -bufsize 3000k -r 29.97 {output_video}".
                format(input_video=input_video, output_video=output_video))
            print("原始分辨率:", cmd)
            subprocess.run(cmd)
        elif fbl == 960:
            cmd = (
                "ffmpeg -i {input_video} -vcodec h264 -preset veryfast -crf 23 -maxrate 1300k -bufsize 3000k -vf scale=960:540 -r 29.97 {output_video}".
                format(input_video=input_video, output_video=output_video))
            print("960P:", cmd)
            subprocess.run(cmd)
        elif fbl == 2000:
            cmd = (
                "ffmpeg -i {input_video} -vcodec h264 -preset veryfast -crf 23 -maxrate 1300k -bufsize 3000k -vf scale=1280:720 -r 29.97 {output_video}".
                format(input_video=input_video, output_video=output_video))
            print("960P:", cmd)
            subprocess.run(cmd)
        elif fbl == 3000:
            cmd = (
                "ffmpeg -i {input_video} -vcodec h264 -preset veryfast -crf 22 -maxrate 2000k -bufsize 3000k -vf scale=1280:720 -r 29.97 {output_video}".
                format(input_video=input_video, output_video=output_video))
            print("3000_720p:", cmd)
            subprocess.run(cmd)
        elif fbl == 4000:
            cmd = (
                "ffmpeg -i {input_video} -vcodec h264 -preset slow -qcomp 0.5 -psy-rd 0.3:0 -aq-mode 2 -aq-strength 0.8 -vf scale=1280:720 -r 29.97 {output_video}".
                format(input_video=input_video, output_video=output_video))
            print("4000超清_720p:", cmd)
            subprocess.run(cmd)
        else:
            print("输入有误")

    def move_file(self, inputvideo, outvideos):
        if not os.path.exists("ok"):
            os.makedirs("ok")
        if not os.path.exists("source_data"):
            os.makedirs("source_data")

        os.system("move {} {} >nul".format(inputvideo, 'source_data'))
        os.system("move {} {} >nul".format(outvideos, 'ok'))

    def xiuxi(self, fen_time=10):

        miao_time = fen_time * 60
        while xiuxi_time > 0:
            print("程序休息300秒倒计时：", miao_time, "秒")
            miao_time -= 1
            time.sleep(1)
            os.system('cls')



p1 = video("3000_720P")
my_dict = p1.get_video()
for key, value in my_dict.items():
    p1.run_zhuanma(4000, key, value)  # fbl可以是：0,960,2000,3000,4000，输入其他都错误
    p1.move_file(key, value)
    p1.xiuxi(30)  # 更新休息的时间单位为分钟

# 测试结果：

# 如果文件名中有多个点，则程序报错【已修复2024.6.26】
# ！！！！！！ 如果文件名中有空格则，程序会报错
