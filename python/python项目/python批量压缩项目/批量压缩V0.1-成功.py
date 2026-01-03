import random, os, subprocess


# 处理文件名
def rarname(file_path):
    # 获取文件名（带扩展名）
    file_name_with_extension = os.path.basename(file_path)
    # 获取文件名（不带扩展名）
    file_name_without_extension1 = os.path.splitext(file_name_with_extension)[0]
    chars_to_remove = {'a', 'b'}  # 要移除的字符集合
    file_name_without_extension2 = file_name_without_extension1.replace('_h264','')
    # 获取扩展名
    file_extension = os.path.splitext(file_name_with_extension)[1]
    return file_name_without_extension2


# 文件名加密
def insert_in_abc_part(original_str, insert_str):
    # 找到 "abc" 部分结束的位置（即 '-' 的位置）
    abc_part_end = original_str.find('-')
    if abc_part_end == -1:  # 如果没有 '-'，则整个字符串视为 "abc" 部分
        abc_part_end = len(original_str)

    # 只能在 "abc" 部分的中间插入（索引 1 到 abc_part_end-1）
    possible_positions = list(range(1, abc_part_end))
    if not possible_positions:  # 如果没有可插入的位置（如 "a-123"）
        return original_str

    insert_pos = random.choice(possible_positions)
    return original_str[:insert_pos] + insert_str + original_str[insert_pos:]


# # 示例
# original_str = "abc-123"
# insert_str = "pokes"
# result = insert_in_abc_part(original_str, insert_str)
# print(result)


def zrar(output_rar, input_video):
    cmd = ("WinRAR a -hp4501596 -m0 {output_rar} {input_video}".format(output_rar=output_rar, input_video=input_video))
    subprocess.run(cmd)


# 获取当前目录
current_dir = os.getcwd()

# 遍历当前目录下的文件
for file in os.listdir(current_dir):
    if file.endswith('.txt'):
        # print(file)
        name1 = rarname(file)
        # print(name1)
        name2 = insert_in_abc_part(name1, "POKES") + ".rar"
        print(name2)
        zrar(name2, file)
