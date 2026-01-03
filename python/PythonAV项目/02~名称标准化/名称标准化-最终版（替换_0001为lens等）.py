import os


class video_rename:

    def __init__(self, task_batch):

        self.task_batch = task_batch

    # 遍历视频文件
    def video_scan(self, pathss=os.getcwd()):
        """
             此函数是遍历视频文件，遍历出的结果包含目录和子目录，并生成一个list
        """
        list_vido_any = []
        # 列表中的字母须小写
        kzhan_list = ["mp4", "avi", "wmv", "rmvb", "mov", "mkv"]
        # 列表中的字母转为大写
        up_kzhan_list = [item.upper() for item in kzhan_list]
        for vido in os.walk(pathss):
            for j in vido[2]:
                # 遍历所得的所有文件，包含子目录的文件，i[0]是当前文件夹的绝对路径，j是文件名
                path = os.path.join(vido[0], j)

                s = path.split(".")  # 以点为分隔符，分割文件名和扩展名，s为路径+文件名，不含扩展名
                ss = s[len(s) - 1]  # ss为扩展名

                # 小写循环写入
                for kzhan in kzhan_list:
                    if ss == kzhan:
                        list_vido_any.append(path)
                # 大写循环写入
                for up_kzhan in up_kzhan_list:
                    if ss == up_kzhan:
                        list_vido_any.append(path)

        return list_vido_any

    # 重命名替换字符
    def rename_str(self, abspath, oldstr, newstr):
        # # 视频所在目录
        # video_absdir = os.path.dirname(abspath)
        # print(video_absdir)
        #
        # # 从绝对路径中提取文件名替换
        # video_name = os.path.basename(abspath)
        # if oldstr in video_name:
        #     video_name = video_name.replace(oldstr, newstr)  # 替换
        #     # 拼接新文件名
        #     # newvideo_abspath = video_absdir + "\\" + video_name
        #     newvideo_abspath = os.path.join(video_absdir, video_name)
        #     print(newvideo_abspath)

        # 文件所在目录
        video_absdir = os.path.dirname(abspath)
        # 源文件的名称
        video_name = os.path.basename(abspath)

        if oldstr in video_name:
            print(video_absdir)
            print(video_name)

            # 替换后文件名称
            video_name2 = video_name.replace(oldstr, newstr)
            print(video_name2)

            # 替换后的绝对路径
            new_video_abspath = os.path.join(video_absdir, video_name2)
            print(new_video_abspath)

            os.rename(abspath, new_video_abspath)

    # 循环处理
    def forlist(self, video_scan, oldstr, newstr):
        new_list = []
        for benci_video in video_scan:
            self.rename_str(benci_video, oldstr, newstr)





pc1 = video_rename("001")

path = r"\\10.10.30.99\d"
pc1_videos_list = pc1.video_scan(path)

pc1.forlist(pc1_videos_list,'_0001', '_lens')
pc1.forlist(pc1_videos_list,'~-', '~')
pc1.forlist(pc1_videos_list,'-1.', '.')
pc1.forlist(pc1_videos_list, '_0001', '_lens')
pc1.forlist(pc1_videos_list, '-0001', '_lens')
pc1.forlist(pc1_videos_list, '_lens_lens', '_lens')
pc1.forlist(pc1_videos_list, '~hevc', '_HEVC')
pc1.forlist(pc1_videos_list, 'uncensored', 'U')
pc1.forlist(pc1_videos_list, 'UNCENSORED', 'U')
pc1.forlist(pc1_videos_list, 'Uncensored', 'U')
pc1.forlist(pc1_videos_list, '-H265', '_HEVC')
pc1.forlist(pc1_videos_list, '-h265', '_HEVC')
pc1.forlist(pc1_videos_list, '.-', '~')
pc1.forlist(pc1_videos_list, '.-h264', '-h264')
pc1.forlist(pc1_videos_list, '~cpu264', '_ok')
pc1.forlist(pc1_videos_list, '-cpu', '_ok')
pc1.forlist(pc1_videos_list, '_neenc_ok', '_ok')


# 报错是因为并发在改文件名，多运行几次