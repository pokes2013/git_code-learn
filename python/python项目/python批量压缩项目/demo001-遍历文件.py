import os


def zrar( input_video, output_rar):
    cmd = (
        "WinRAR a -hp4501596 -m0 {output_rar} {input_video}".format(input_video=input_video, output_video=output_video))
    print("原始分辨率:", cmd)
    subprocess.run(cmd)



def rarname(file_path):
    # 获取文件名（带扩展名）
    file_name_with_extension = os.path.basename(file_path)
    # 获取文件名（不带扩展名）
    file_name_without_extension = os.path.splitext(file_name_with_extension)[0]
    # 获取扩展名
    file_extension = os.path.splitext(file_name_with_extension)[1]

    




# 获取当前目录
current_dir = os.getcwd()

# 遍历当前目录下的文件
for file in os.listdir(current_dir):
    if file.endswith('.txt'):
        print(file)


