import os
import shutil
from datetime import datetime
import time
from tqdm import tqdm


def backup_network_data(source_path, dest_path):
    """
    备份网络服务器数据到本地，支持增量备份

    参数:
        source_path (str): 源路径 (网络服务器路径)
        dest_path (str): 目标路径 (本地路径)
    """
    # 记录开始时间
    start_time = datetime.now()
    print(f"备份开始时间: {start_time.strftime('%Y-%m-%d %H:%M:%S')}")

    # 确保目标目录存在
    os.makedirs(dest_path, exist_ok=True)

    # 获取源目录中的所有文件和目录
    try:
        all_files = []
        for root, dirs, files in os.walk(source_path):
            for file in files:
                src_file = os.path.join(root, file)
                # 转换为相对路径
                rel_path = os.path.relpath(src_file, source_path)
                all_files.append((src_file, rel_path))
    except Exception as e:
        print(f"访问源目录出错: {e}")
        return False

    # 创建进度条
    with tqdm(total=len(all_files), desc="备份进度", unit="文件") as pbar:
        copied_files = 0
        skipped_files = 0
        error_files = 0

        for src_file, rel_path in all_files:
            dest_file = os.path.join(dest_path, rel_path)

            # 检查是否需要复制（增量备份）
            need_copy = True
            if os.path.exists(dest_file):
                src_mtime = os.path.getmtime(src_file)
                dest_mtime = os.path.getmtime(dest_file)
                if src_mtime <= dest_mtime:
                    need_copy = False

            if need_copy:
                try:
                    # 确保目标目录存在
                    os.makedirs(os.path.dirname(dest_file), exist_ok=True)

                    # 复制文件
                    shutil.copy2(src_file, dest_file)
                    copied_files += 1
                except Exception as e:
                    print(f"\n复制文件 {src_file} 出错: {e}")
                    error_files += 1
            else:
                skipped_files += 1

            # 更新进度条
            pbar.update(1)
            pbar.set_postfix({
                '已复制': copied_files,
                '已跳过': skipped_files,
                '错误': error_files
            })

    # 记录结束时间
    end_time = datetime.now()
    duration = end_time - start_time
    print(f"\n备份完成时间: {end_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"总耗时: {duration}")
    print(f"统计: 已复制 {copied_files} 个文件, 跳过 {skipped_files} 个未修改文件, {error_files} 个错误")

    return True


if __name__ == "__main__":
    # 配置源路径和目标路径
    SOURCE_PATH = r"\\192.168.1.141\04-工程"
    DEST_PATH = r"E:/DATA/ceshi/"

    print("网络服务器数据备份工具")
    print(f"源路径: {SOURCE_PATH}")
    print(f"目标路径: {DEST_PATH}")

    # 执行备份
    success = backup_network_data(SOURCE_PATH, DEST_PATH)

    if success:
        print("备份成功完成!")
    else:
        print("备份过程中出现错误!")

    # 防止窗口立即关闭（如果是双击运行）
    input("按回车键退出...")