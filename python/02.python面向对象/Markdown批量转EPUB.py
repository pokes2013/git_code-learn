# 测试结果：
# 可以批量转换，但是图片没有被内嵌



import os
import subprocess

directory = r'D:\project2024\gitbook2024\AV_gitbook\AVdoc'

for filename in os.listdir(directory):
    if filename.endswith('.md'):
        input_path = os.path.join(directory, filename)
        output_path = os.path.join(directory, filename.replace('.md', '.epub'))
        subprocess.run(['pandoc', input_path, '-o', output_path])

