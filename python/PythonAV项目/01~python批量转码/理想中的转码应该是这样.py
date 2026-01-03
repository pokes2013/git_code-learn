import os
import subprocess


class get_zhuanma:

    def __init__(self, task_name):
        self.task_name = task_name
        print("批次：", task_name)

    def compress_video(self, select_fbl, input_video_path, output_video_path, speed, crf, maxrate, bufsize):
        """
        使用ffmpeg压缩视频。

        :param input_video_path: 输入视频文件路径。
        :param output_video_path: 输出视频文件路径。
        :param bitrate: 视频码率。

        ffmpeg -i {input_video} -vcodec h264 -preset {veryfast/slow} -crf {18-23} -maxrate {2000K} -bufsize {3000K} -vf scale={1280:-2} -r 29.97 {output_video}


        """

        if select_fbl == 720:

            command_720 = [
                'ffmpeg',
                '-i', input_video_path,
                '-vcodec', 'h264',
                '-preset', f'{speed}',
                '-crf', f'{crf}',  # 设置视频码率
                '-maxrate', f'{maxrate}',  # 设置视频码率
                '-bufsize', f'{bufsize}',  # 设置视频码率
                '-vf', 'scale='f'{1280:-2}',  # 设置视频码率
                '-r', '29.97',
                output_video_path
            ]
            print(command_720)

            subprocess.run(command_720)

        elif select_fbl == 0:

            command_source = [
                'ffmpeg',
                '-i', input_video_path,
                '-vcodec', 'h264',
                '-preset', f'{speed}',
                '-crf', f'{crf}',  # 设置视频码率
                '-maxrate', f'{maxrate}',  # 设置视频码率
                '-bufsize', f'{bufsize}',  # 设置视频码率
                '-r', '29.97',
                output_video_path
            ]
            print(command_source)

            subprocess.run(command_source)

        else:
            return


    def video_scan(self, pathss=os.getcwd()):
        """
             此函数是遍历视频文件，请输入您的路径，遍历出的结果不包含子目录，并生成一个list
        """
        # 当前目录所有文件的序列
        file_list = os.listdir(pathss)
        vido_list = [s for s in file_list if '*' in s]  # 当前目录所有文件

        list_vido_any = []
        # 列表中的字母须小写
        kzhan_list = ["mp4", "avi", "wmv", "rmvb", "mov", "mkv"]

        for vido_path in os.listdir(os.chdir(pathss)):

            # 以点为分隔符，分割文件名和扩展名; s为路径+文件名，不含扩展名
            s = vido_path.split(".")
            # ss为扩展名，这里统一使用小写
            ss = s[len(s) - 1].lower()
            for kzhan in kzhan_list:
                if ss == kzhan:
                    list_vido_any.append(vido_path)

        print(list_vido_any)
        return list_vido_any

    def video_name_pj(self, video_name):
        notkuozhan_video_name = os.path.splitext(video_name)[0]
        out_videos = notkuozhan_video_name + "_h264" + ".mp4"
        return out_videos

    def move_file(self, inputvideo, outvideos):
        if not os.path.exists("ok"):
            os.makedirs("ok")
        if not os.path.exists("source_data"):
            os.makedirs("source_data")

        os.system("move {} {} >nul".format(inputvideo, 'source_data'))
        os.system("move {} {} >nul".format(outvideos, 'ok'))


p1 = get_zhuanma("001")
# 视频文件列表

for video in p1.video_scan():
    in_video = video
    out_videos = p1.video_name_pj(video)
    p1.compress_video(720, in_video, out_videos, 'slow', 23, '2000k', '3000k')
    p1.move_file(in_video, out_videos)


# def compress_video(self, select_fbl, input_video_path, output_video_path, speed, crf, maxrate, bufsize, scale_fbl)中的说明：
# select_fbl：判断参数，输入720则分辨率设置为1280:720,输入0则转码时不更变分辨率
# speed：为转码速率，一般常用的有两个：veryfast，slow
# maxrate：maxrate为最大码率
# bufsize为振幅码率


