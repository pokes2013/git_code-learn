import os
import shutil
import time
import sys


def get_total_size(path):
    """计算文件或目录的总大小"""
    if os.path.isfile(path):
        return os.path.getsize(path)

    total_size = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size


def print_progress(current, total, filename=None):
    """打印进度信息"""
    percent = (current / total) * 100 if total > 0 else 0
    bar_length = 40
    filled_length = int(bar_length * current // total)
    bar = '█' * filled_length + '-' * (bar_length - filled_length)

    progress_info = f"\r[{bar}] {percent:.1f}% ({current}/{total} bytes)"
    if filename:
        progress_info += f" - {filename}"

    sys.stdout.write(progress_info)
    sys.stdout.flush()



def copy_file_with_progress(src, dst):
    """复制文件并显示进度"""
    file_size = os.path.getsize(src)
    copied = 0

    # 使用 copyfileobj 实现带进度显示的文件复制
    with open(src, 'rb') as fsrc:
        with open(dst, 'wb') as fdst:
            while True:
                buf = fsrc.read(16 * 1024)  # 16KB缓冲区
                if not buf:
                    break
                fdst.write(buf)
                copied += len(buf)
                print_progress(copied, file_size, os.path.basename(src))

    # 复制文件元数据
    shutil.copymode(src, dst)
    shutil.copystat(src, dst)
    print()  # 换行
    print()  # 换行


def copy_dir_with_progress(src, dst):
    """复制目录并显示进度"""
    total_size = get_total_size(src)
    copied_size = 0

    os.makedirs(dst, exist_ok=True)

    for dirpath, dirnames, filenames in os.walk(src):
        relative_path = os.path.relpath(dirpath, src)
        dest_dir = os.path.join(dst, relative_path)
        os.makedirs(dest_dir, exist_ok=True)

        for filename in filenames:
            src_file = os.path.join(dirpath, filename)
            dst_file = os.path.join(dest_dir, filename)

            file_size = os.path.getsize(src_file)
            copied = 0

            # 复制文件内容
            with open(src_file, 'rb') as fsrc:
                with open(dst_file, 'wb') as fdst:
                    while True:
                        buf = fsrc.read(16 * 1024)  # 16KB缓冲区
                        if not buf:
                            break
                        fdst.write(buf)
                        copied += len(buf)
                        copied_size += len(buf)
                        print_progress(copied_size, total_size, filename)

            # 复制文件元数据
            shutil.copymode(src_file, dst_file)
            shutil.copystat(src_file, dst_file)
    print()  # 换行


def main():
    print("网络路径复制工具")
    print("----------------")

    # 输入网络路径和本地路径

    network_path = '\\\\192.168.1.141\\04-工程\\'.strip()
    local_path = 'E:/DATA/ceshi/'.strip()

    # 检查网络路径是否存在
    if not os.path.exists(network_path):
        print(f"\n错误: 网络路径 '{network_path}' 不存在或无法访问")
        time.sleep(10)
        return

    try:
        print("\n开始复制...")
        start_time = time.time()

        if os.path.isfile(network_path):
            copy_file_with_progress(network_path, local_path)
        else:
            copy_dir_with_progress(network_path, local_path)

        elapsed_time = time.time() - start_time
        print(f"\n复制完成! 耗时: {elapsed_time:.2f}秒")
        print("程序将在10秒后自动关闭...")
        time.sleep(10)

    except Exception as e:
        print(f"\n复制过程中发生错误: {str(e)}")
        print("程序将在10秒后自动关闭...")
        time.sleep(10)


if __name__ == "__main__":
    main()