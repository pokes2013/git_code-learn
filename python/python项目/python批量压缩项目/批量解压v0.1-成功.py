import os, subprocess


def zrar(input_rar):
    cmd = ("WinRAR x -hp4501596 {input_rar}".format(input_rar=input_rar))
    print(cmd)
    subprocess.run(cmd)

# 获取当前目录
current_dir = os.getcwd()

for file in os.listdir(current_dir):
    if file.endswith('.rar'):
        print(file)
        zrar(file)
