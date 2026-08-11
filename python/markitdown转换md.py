import os
from markitdown import MarkItDown

# ====================== 自定义配置区 ======================
INPUT_DIR = "input"
OUTPUT_DIR = "outfiles"
# 白名单后缀统一小写，程序会自动把文件后缀转小写对比
ALLOW_EXTENSIONS = {".pdf", ".docx", ".doc", ".xlsx", ".xls", ".pptx", ".ppt", ".png", ".jpg", ".jpeg", ".html"}
OVERWRITE = False  # True=覆盖已有md，False=跳过已转换文件
RECURSIVE_SCAN = True  # True递归扫描子文件夹，False仅扫描一级目录
# ==========================================================

# 自动创建输入输出文件夹
os.makedirs(INPUT_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

# 初始化转换实例
md_tool = MarkItDown()


def single_file_convert(source_path: str, target_md_path: str) -> bool:
    """单个文件转换，异常保护"""
    try:
        convert_result = md_tool.convert(source_path)
        with open(target_md_path, "w", encoding="utf-8") as f:
            f.write(convert_result.text_content)
        print(f"✅ 转换成功 | {os.path.basename(source_path)} -> {os.path.basename(target_md_path)}")
        return True
    except Exception as err:
        print(f"❌ 转换失败 | 文件：{source_path} | 错误：{str(err)}")
        return False


def run_batch_convert():
    print("========== MarkItDown 批量转换工具 ==========")
    print(f"输入目录：{INPUT_DIR}")
    print(f"输出目录：{OUTPUT_DIR}")
    print(f"开启递归遍历：{RECURSIVE_SCAN}")
    print(f"允许转换后缀：{','.join(ALLOW_EXTENSIONS)}\n")

    if RECURSIVE_SCAN:
        # 递归遍历所有子目录
        walk_iterator = os.walk(INPUT_DIR)
    else:
        # 仅一级目录封装成walk格式统一处理
        walk_iterator = [(INPUT_DIR, [], os.listdir(INPUT_DIR))]

    for root, _, file_list in walk_iterator:
        for file_name in file_list:
            full_source_path = os.path.join(root, file_name)
            # 跳过文件夹，只处理文件
            if os.path.isdir(full_source_path):
                continue

            # 拆分文件名与后缀，后缀强制转小写
            name_stem, ext_origin = os.path.splitext(file_name)
            ext_lower = ext_origin.lower()

            # 大小写统一后匹配白名单
            if ext_lower not in ALLOW_EXTENSIONS:
                print(f"⏭️ 跳过非指定格式：{file_name}")
                continue

            # 还原目录层级到输出文件夹
            rel_dir = os.path.relpath(root, INPUT_DIR)
            out_sub_folder = os.path.join(OUTPUT_DIR, rel_dir)
            os.makedirs(out_sub_folder, exist_ok=True)
            # 文件名增加 _out 标识：原名称_out.md
            full_md_output = os.path.join(out_sub_folder, f"{name_stem}_out.md")

            # 判断是否跳过已存在文件
            if os.path.exists(full_md_output) and not OVERWRITE:
                print(f"⏭️ 已存在跳过：{file_name}")
                continue

            # 执行转换
            single_file_convert(full_source_path, full_md_output)


if __name__ == "__main__":
    run_batch_convert()
    print("\n========== 全部转换任务执行完成 ==========")