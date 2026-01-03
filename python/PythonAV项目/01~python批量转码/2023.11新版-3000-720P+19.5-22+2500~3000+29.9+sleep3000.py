import os, sys, time, datetime

# 思路：用cmd命令将视频文件过滤出来，并写入到一个TXT文本文件中，然后读取txt的每一行去执行

# 遇到问题
# 此方法已经成功，但是txt读取和写入时候的编码问题很麻烦，具体如下：
# 1.bat脚本生成的txt编码是ANSI,导致读取每一行的时候不能识别汉字；
# 2.然后是后面的日志也出现了问题

# 解决问题：
# 1.编码最终还是选择了ANSI编码，暂时没发现什么问题，后续估计会出现问题
# 2.日志也是ANSI编码

# 改进：时间系统改进一下
# 1、很直观的看出来转码用了多少分钟


# 1.创建和检验目录是否存在，如果存在则跳过，不存在则创建


# 开始之前先删除上次遗留的日志
os.system("del logs.txt")
os.system("del data_0.txt")
os.system("del data.txt")


def floders(floder_name):
    isExists = os.path.exists(floder_name)
    if not isExists:
        os.makedirs(floder_name)


# 提取当前目录内的视频文件并写入到data.txt
txtfile = "dir /b *.ts,*.avi,*.mp4,*.wmv,*.flv,*.mkv,*.rmvb,*.rm,*.mov > data.txt"
# txtfile = "dir /b > data_0.txt"
os.system(txtfile)

# # 将txt编码转为UTF-8
# with open("data_0.txt", "r", encoding='GB2312') as f:
#     text = f.read()  # 读取文件内容
# text_utf8 = text.encode('utf-8')    #将文本编码为UTF-8
# with open('data.txt', 'w', encoding='utf-8') as f:
#     f.write(str(text_utf8))  #将编码后的文本写入新的文件

# 申明工作目录
path = os.getcwd() + "\\"

f = open("data.txt", 'r', encoding='GB2312', errors='ignore')
f_list = (f.readlines())
f_list = (map(str.strip, f_list))  # 去除换行,生成新的list
for input_video in f_list:
    # 格式化文件名
    i_name = os.path.splitext(input_video)[0]
    # i_kzm=os.path.splitext(input_video)[1]
    input_video = '"' + input_video + '"'
    print(input_video)
    output_video = '"' + i_name + "_ok" + ".mp4\""
    print(output_video)

    # 转码

    floders("OK")
    floders("source_data")
    bit = "-qmin 19.5 -crf 22.0 -maxrate 2500k -bufsize 3000k"  # 码率控制
    vido_filter = "-vf scale=1280:-2"  # 过滤器
    speed = "-preset veryfast"  # 转码速度

    start_time = time.time()
    zhuanma = ("ffmpeg -i {infile} "
               "-vcodec h264 {sudo} "
               "-tune:v ssim {malu} "
               "-r 29.97 {lujing} {outfile} && "
               "move {outfile} OK >nul && "
               "move {infile} source_data>nul"
               .format(infile=input_video,
                       sudo=speed,
                       malu=bit,
                       lujing=vido_filter,
                       outfile=output_video))
    print(zhuanma)
    isRUN = os.system(zhuanma)
    print("*" * 100)  # 分割线
    print(path + output_video, '转换成功')  # 输出转换成功的提示

    # 记录结束时间
    end_time = time.time()
    took = (end_time - start_time) / 60
    took = int(took)
    took = str(took)
    # print("所需时间:", took,"分钟")

    # 日志系统，日志文件在视频目录中

    file = open("logs.txt", 'a', encoding='utf-8')
    file.write(str(datetime.datetime.now()) + "\n")  # 当前时间日期转为字符串才能用
    file.write(input_video + "\n")
    file.write("所需时间：" + took + "\n")
    file.write("-" * 100 + "\n")
    file.close()

    # 休息5分钟

    xiuxi = 300
    while xiuxi > 0:
        print("程序休息300秒倒计时：", xiuxi, "秒")
        xiuxi -= 1
        time.sleep(1)
        os.system('cls')
