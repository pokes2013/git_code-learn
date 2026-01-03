# srcfile 需要复制、移动的文件
# dstpath 目的地址

import os
import shutil
from glob import glob


def mycopyfile(srcfile, dstpath):  # 复制函数
    if not os.path.isfile(srcfile):
        print("%s not exist!" % (srcfile))
    else:
        fpath, fname = os.path.split(srcfile)  # 分离文件名和路径
        if not os.path.exists(dstpath):
            os.makedirs(dstpath)  # 创建路径
        shutil.copy(srcfile, dstpath + fname)  # 复制文件
        print("copy %s -> %s" % (srcfile, dstpath + fname))


src_dir = r'\\192.168.1.141\02-销售\*'
dst_dir = r'E:/DATA/ceshi/'  # 目的路径记得加斜杠
src_file_list = glob(src_dir + '*')  # glob获得路径下所有文件，可根据需要修改
for srcfile in src_file_list:
    mycopyfile(srcfile, dst_dir)  # 复制文件

print("程序运行结束，按任意键退出...")
os.system('pause')  # Windows 专用，会显示 "按任意键继续..."