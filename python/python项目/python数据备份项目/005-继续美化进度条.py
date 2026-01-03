import os
import shutil
import time
import sys


def get_total_size(path):
    """计算文件或目录的总大小（字节）"""
    if os.path.isfile(path):
        return os.path.getsize(path)

    total_size = 0
    for dirpath, _, filenames in os.walk(path):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            total_size += os.path.getsize(filepath)
    return total_size


def print_progress(current, total, filename=None, start_time=None):
    """
    打印动态彩色进度条（单行更新）
    :param current: 已传输字节数
    :param total: 总字节数
    :param filename: 当前文件名（可选）
    :param start_time: 传输开始时间（用于计算速度）
    """
    percent = (current / total) * 100 if total > 0 else 0
    bar_length = 40
    filled_length = int(bar_length * current // total)

    # 颜色渐变：蓝 -> 青 -> 绿
    if percent < 30:
        color = "\033[94m"  # 蓝色
    elif percent < 70:
        color = "\033[96m"  # 青色
    else:
        color = "\033[92m"  # 绿色

    # 构建进度条
    bar = color + '>>' * filled_length + "\033[0m" + '-' * (bar_length - filled_length)

    # 计算传输速度
    speed_info = ""
    if start_time and current > 0:
        elapsed = time.time() - start_time
        speed = (current / (1024 * 1024)) / elapsed if elapsed > 0 else 0
        speed_info = f" \033[93m{speed:.2f} MB/s\033[0m"

    # 构建完整进度信息
    progress_info = (
        f"\r[{bar}] \033[93m{percent:.1f}%\033[0m "
        f"({current / (1024 * 1024):.2f}/{total / (1024 * 1024):.2f} MB)"
        f"{speed_info}"
    )
    if filename:
        progress_info += f" \033[93m|\033[0m \033[96m{filename[:30]}\033[0m"

    sys.stdout.write(progress_info)
    sys.stdout.flush()


def copy_file_with_progress(src, dst):
    """复制文件并显示动态进度条（每个文件完成后换行）"""
    file_size = os.path.getsize(src)
    copied = 0
    start_time = time.time()

    with open(src, 'rb') as fsrc:
        with open(dst, 'wb') as fdst:
            while True:
                buf = fsrc.read(64 * 1024)  # 64KB 缓冲区
                if not buf:
                    break
                fdst.write(buf)
                copied += len(buf)
                print_progress(copied, file_size, os.path.basename(src), start_time)

    # 复制文件元数据
    shutil.copymode(src, dst)
    shutil.copystat(src, dst)
    print("\n")  # 强制换行（关键修改）


def copy_dir_with_progress(src, dst):
    """复制目录并显示动态进度条（每个文件完成后换行）"""
    total_size = get_total_size(src)
    copied_size = 0
    start_time = time.time()

    os.makedirs(dst, exist_ok=True)

    for dirpath, _, filenames in os.walk(src):
        relative_path = os.path.relpath(dirpath, src)
        dest_dir = os.path.join(dst, relative_path)
        os.makedirs(dest_dir, exist_ok=True)

        for filename in filenames:
            src_file = os.path.join(dirpath, filename)
            dst_file = os.path.join(dest_dir, filename)

            file_size = os.path.getsize(src_file)
            copied = 0

            with open(src_file, 'rb') as fsrc:
                with open(dst_file, 'wb') as fdst:
                    while True:
                        buf = fsrc.read(64 * 1024)
                        if not buf:
                            break
                        fdst.write(buf)
                        copied += len(buf)
                        copied_size += len(buf)
                        print_progress(copied_size, total_size, filename, start_time)

            # 复制文件元数据
            shutil.copymode(src_file, dst_file)
            shutil.copystat(src_file, dst_file)
            print("\n")  # 每个文件完成后换行（关键修改）

    print()  # 最终换行


def main():
    print("\033[96m网络路径复制工具\033[0m")
    print("\033[90m" + "=" * 40 + "\033[0m")

    # 输入路径（实际使用时可以改为用户输入）
    network_path = '\\\\192.168.1.141\\04-工程\\'.strip()
    local_path = 'E:/DATA/ceshi/'.strip()

    # 检查网络路径是否存在
    if not os.path.exists(network_path):
        print(f"\n\033[91m错误: 网络路径 '{network_path}' 不存在或无法访问\033[0m")
        time.sleep(5)
        return

    try:
        print(f"\n\033[93m来源:\033[0m {network_path}")
        print(f"\033[93m目标:\033[0m {local_path}")
        print("\n\033[92m开始复制...\033[0m")
        start_time = time.time()

        if os.path.isfile(network_path):
            copy_file_with_progress(network_path, local_path)
        else:
            copy_dir_with_progress(network_path, local_path)

        elapsed_time = time.time() - start_time
        print(f"\n\033[92m复制完成! 耗时: {elapsed_time:.2f}秒\033[0m")
        print("程序将在5秒后自动关闭...")
        time.sleep(5)

    except Exception as e:
        print(f"\n\033[91m复制过程中发生错误: {str(e)}\033[0m")
        print("程序将在10秒后自动关闭...")
        time.sleep(10)


if __name__ == "__main__":
    os.system('')  # 启用 Windows ANSI 颜色支持
    main()