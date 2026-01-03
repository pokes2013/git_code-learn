import os
import subprocess
import time


class zhuancode:

    # 视频所在目录
    def __init__(self, videopath):
        self.videopath = videopath

    # 遍历目录中的视频文件, 格式化输出文件名，并将输入文件和输出文件生成一个字典
    def get_videofiles(self):
        """
        遍历当前目录下的视频文件(不包含子目录)，并且生成一个list,
        :param video_path:视频目录
        :return: videos是生成的视频文件列表
        """
        # 常见的视频文件扩展名
        video_extensions = ['.mp4', '.avi', ".rmvb", '.mkv', '.mov', '.wmv']

        # 获取当前目录下的所有文件
        current_directory_files = os.listdir(self.videopath)

        # 新建空list,用于存放遍历结果
        videos_dict = {}

        # 遍历文件，找到视频文件
        for input_video in current_directory_files:
            extension = os.path.splitext(input_video)[1]  # 获取文件扩展名
            if extension.lower() in video_extensions:
                # print(file)
                input_videojg = os.path.splitext(input_video)[0]  # abc-123
                out_video = input_videojg + '_ok' + ".mp4"
                videos_dict.setdefault(input_video, out_video)

        return videos_dict

    # 格式化输出文件名，并将输入文件和输出文件生成一个字典

    # 720P转码
    def zhuanma720(self, input_video, output_video, speed="veryfast", crf="23", maxrate="2000k", bufsize="3000k",
                   fenbianlv="1280:-2"):
        """
        这是一个视频转码的函数，默认转码分辨率720P，可以自行修改

        :param input_video: 输入文件
        :param output_video: 输出文件
        :param speed: 转码速度
        :param crf: 视频质量默认23
        :param maxrate: 平均码率默认2000K
        :param bufsize: 振幅码率默认3000K
        :param fenbianlv: 分辨率，默认1280*720
        :return: 耗时,状态码,开始时间,结束时间啊
        """
        cmd = (
            "ffmpeg -i {input_video} -vcodec h264 -preset {speed} -crf {crf} -maxrate {maxrate} -bufsize {bufsize} -vf scale={fenbianlv} -r 29.97 {output_video}".format(
                input_video=input_video, speed=speed, crf=crf, maxrate=maxrate, bufsize=bufsize, fenbianlv=fenbianlv,
                output_video=output_video))
        start_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        star = time.time()  # 开始时间，需要截取，后续会写入日志中
        # result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        result = subprocess.run(cmd)
        end = time.time()  # 结束时间会写入日志
        end_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        haoshi = int((end - star) / 60)
        return haoshi, result.returncode, start_time, end_time

    # 转码 - 原始分辨率
    def zhuanma_source(self, input_video, output_video, speed="veryfast", crf="23", maxrate="2000k", bufsize="3000k"):
        """

        这是一个视频转码的函数，默认分辨率和原视频相同

        :param input_video: 输入文件
        :param output_video: 输出文件
        :param speed: 转码速度
        :param crf: 视频质量默认23
        :param maxrate: 平均码率默认2000K
        :param bufsize: 振幅码率默认3000K
        :return: 耗时,状态码,开始时间,结束时间啊
        """
        cmd = (
            "ffmpeg -i {input_video} -vcodec h264 -preset {speed} -crf {crf} -maxrate {maxrate} -bufsize {bufsize} -r 29.97 {output_video}".format(
                input_video=input_video, speed=speed, crf=crf, maxrate=maxrate, bufsize=bufsize,
                output_video=output_video))
        start_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        star = time.time()  # 开始时间，需要截取，后续会写入日志中
        # result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        result = subprocess.run(cmd)
        end = time.time()  # 结束时间会写入日志
        end_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        haoshi = int((end - star) / 60)
        return haoshi, result.returncode, start_time, end_time

    # 日志
    def vlog(self, txts, name='logs.txt'):
        with open(name, "a", encoding="UTF-8") as f:
            f.write(txts)
            # print(txts)
            f.write('\n')

    # 移动文件
    def move_file(self, inputvideo, outvideos):
        if not os.path.exists("ok"):
            os.makedirs("ok")
        if not os.path.exists("source_data"):
            os.makedirs("source_data")

        os.system("move {} {} >nul".format(inputvideo, 'source_data'))
        os.system("move {} {} >nul".format(outvideos, 'ok'))

    # 获取视频时长
    def get_videoinfo(self, file_path):
        command = ['ffprobe', '-v', 'error', '-show_entries',
                   'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1', file_path]
        try:
            # 运行ffprobe命令
            result = subprocess.check_output(command, stderr=subprocess.STDOUT)
            # 输出结果是视频的时长，单位为秒
            duration_seconds = float(result.decode().strip())
            return duration_seconds / 60
        except subprocess.CalledProcessError as e:
            return "无法获取时长"


# 创建一个VideoCoding类的对象，用于转码
# dft = zhuancode(os.getcwd())
dft = zhuancode(r"F:\AV2021\00.2024.2.17-老家传输")
# 获取当前目录下的视频文件,生成输出文件，并生成一个dict
get_dict = dft.get_videofiles()

print("1、3000分辨率")
print("2、原始分辨率")
print("3、960分辨率")
print("4、1080分辨率")
print("5、二次压缩平均码率1300")
print("6、退出程序")

num = input("请选择分辨率：")

if int(num) == 1:
    # 720分辨率转码
    for invideo, outideo in get_dict.items():

        # 转码开始，返回状态、耗时，结束时间
        zmresult = dft.zhuanma720(invideo, outideo, speed="veryfast", crf="23", maxrate="2000k", bufsize="3000k",fenbianlv="1280:-2")
        # 转码结束后检测是否成功，返回0则转码成功
        if zmresult[1] == 0:
            # 获取视频时长
            video_duration = dft.get_videoinfo(invideo)
            # 转码完成之后转移文件
            dft.move_file(invideo, outideo)
            # 将转码信息写入日志文件
            dft.vlog(f'开始时间:{zmresult[2]} | {invideo} | 视频时长：{int(video_duration)}分钟 | 转码耗时：{zmresult[0]}分钟 | 结束时间:{zmresult[3]} | 转换成功')
        else:
            print("警告：转码失败")
            # 转码失败信息写入日志文件
            dft.vlog(f'警告： {invideo} | 转码失败！！！！')
            continue

elif int(num) == 2:
    # 原始分辨率转码
    for invideo, outideo in get_dict.items():

        # 转码开始，返回状态、耗时，结束时间
        zmresult = dft.zhuanma_source(invideo, outideo, speed="veryfast", crf="19", maxrate="1300k", bufsize="2000k")
        # 转码结束后检测是否成功，返回0则转码成功
        if zmresult[1] == 0:
            # 获取视频时长
            video_duration = dft.get_videoinfo(invideo)
            # 转码完成之后转移文件
            dft.move_file(invideo, outideo)
            # 将转码信息写入日志文件
            dft.vlog(
                f'开始时间:{zmresult[2]} | {invideo} | 视频时长：{int(video_duration)}分钟 | 转码耗时：{zmresult[0]}分钟 | 结束时间:{zmresult[3]} | 转换成功')
        else:
            print("警告：转码失败")
            # 转码失败信息写入日志文件
            dft.vlog(f'警告： {invideo} | 转码失败！！！！')
            continue
elif int(num) == 3:
    # 720分辨率转码
    for invideo, outideo in get_dict.items():

        # 转码开始，返回状态、耗时，结束时间
        zmresult = dft.zhuanma720(invideo, outideo, speed="veryfast", crf="23", maxrate="1300k", bufsize="2000k",
                                  fenbianlv="960:540")
        # 转码结束后检测是否成功，返回0则转码成功
        if zmresult[1] == 0:
            # 获取视频时长
            video_duration = dft.get_videoinfo(invideo)
            # 转码完成之后转移文件
            dft.move_file(invideo, outideo)
            # 将转码信息写入日志文件
            dft.vlog(
                f'开始时间:{zmresult[2]} | {invideo} | 视频时长：{int(video_duration)}分钟 | 转码耗时：{zmresult[0]}分钟 | 结束时间:{zmresult[3]} | 转换成功')
        else:
            print("警告：转码失败")
            # 转码失败信息写入日志文件
            dft.vlog(f'警告： {invideo} | 转码失败！！！！')
            continue
elif int(num) == 4:
    # 1080分辨率转码
    for invideo, outideo in get_dict.items():

        # 转码开始，返回状态、耗时，结束时间
        zmresult = dft.zhuanma720(invideo, outideo, speed="veryfast", crf="23", maxrate="3500k", bufsize="2000k",
                                  fenbianlv="1920:1080")
        # 转码结束后检测是否成功，返回0则转码成功
        if zmresult[1] == 0:
            # 获取视频时长
            video_duration = dft.get_videoinfo(invideo)
            # 转码完成之后转移文件
            dft.move_file(invideo, outideo)
            # 将转码信息写入日志文件
            dft.vlog(
                f'开始时间:{zmresult[2]} | {invideo} | 视频时长：{int(video_duration)}分钟 | 转码耗时：{zmresult[0]}分钟 | 结束时间:{zmresult[3]} | 转换成功')
        else:
            print("警告：转码失败")
            # 转码失败信息写入日志文件
            dft.vlog(f'警告： {invideo} | 转码失败！！！！')
elif int(num) == 5:
    # 原始分辨率转码
    for invideo, outideo in get_dict.items():

        # 转码开始，返回状态、耗时，结束时间
        zmresult = dft.zhuanma_source(invideo, outideo, speed="veryfast", crf="19", maxrate="1300k", bufsize="2000k")
        # 转码结束后检测是否成功，返回0则转码成功
        if zmresult[1] == 0:
            # 获取视频时长
            video_duration = dft.get_videoinfo(invideo)
            # 转码完成之后转移文件
            dft.move_file(invideo, outideo)
            # 将转码信息写入日志文件
            dft.vlog(
                f'开始时间:{zmresult[2]} | {invideo} | 视频时长：{int(video_duration)}分钟 | 转码耗时：{zmresult[0]}分钟 | 结束时间:{zmresult[3]} | 转换成功')
        else:
            print("警告：转码失败")
            # 转码失败信息写入日志文件
            dft.vlog(f'警告： {invideo} | 转码失败！！！！')
            continue

else:
    print("输入有误，程序退出")
