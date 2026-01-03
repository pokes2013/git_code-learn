import os

# 当前工作目录
path = os.getcwd()


# 过滤视频文件

def vido_any(kuozhan_list=[".wochanh264"], windows_path=os.getcwd()):
    files_list = os.listdir(windows_path)  # 当前目录所有文件的序列

    list_vido_any = []
    for kuozhan_name in kuozhan_list:

        vido_list_xx = [s for s in files_list if kuozhan_name in s]  # 这里有个bug,不支持大写扩展名
        for filename_xx in vido_list_xx:
            list_vido_any.append(filename_xx)

        kuozhan_name_up = kuozhan_name.upper()  # 修复这个bug
        vido_list_up = [s for s in files_list if kuozhan_name_up in s]  # 转大写搜索，再次写入列表中
        for filename_dx in vido_list_up:
            list_vido_any.append(filename_dx)

    print(list_vido_any)
    return list_vido_any


# 更改后缀扩展名
def upext(video_name, xilie):
    qext = os.path.splitext(video_name)[0]
    hext = os.path.splitext(video_name)[1]
    result = qext + xilie + hext

    os.rename(video_name, result)
    print(video_name,"更改为:",result)


print("请输入你的系列名称，类型为字符串，例如“麻豆”，注意需要加双引号！")
xilie = input("请输入你的系列名称:")
for vido in vido_any():
    vido_new = upext(vido, xilie)
    print(vido_new)
