# 这是一个Python面试题
# 要求：
# 1、用Python读取名为data.xlsx的文件
# 2、并且以第一列单元格中的内容批量创建txt文件
# 3、创建的txt文件必须放到，当前目录下的pokes文件夹下（当前目录内暂无pokes文件夹）
# 4、将此脚本升级为一个函数，调用可以批量创建MP4、MP3、doc等任意扩展名的文件。

# 学了一个月python的我没搞定，各位帮忙啊



import pandas as pd
from pathlib import Path


def create_file_by_xlsx(suffix: str):
    df = pd.read_excel("data.xlsx", header=None)
    names = df[0].values

    pokes = Path(__file__).parent / "pokes"
    pokes.mkdir(exist_ok=True)

    for n in names:
        f = pokes / f"{n}.{suffix}"
        f.touch()


create_file_by_xlsx("txt")