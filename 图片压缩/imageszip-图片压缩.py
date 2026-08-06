import subprocess
import os


def check_ffmpeg():
    """校验FFmpeg可用性"""
    try:
        subprocess.run(
            ["ffmpeg", "-version"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=True
        )
        return True
    except Exception as e:
        print(f"FFmpeg调用失败：{e}")
        return False

def batch_ffmpeg_compress_1mb(input_folder, max_size=1048576):
    input_folder = os.path.abspath(input_folder)
    # 输出目录和输入目录平级
    parent_dir = os.path.dirname(input_folder)
    out_dir = os.path.join(parent_dir, "outfile")

    print(f"图片输入目录：{input_folder}")
    print(f"压缩输出目录：{out_dir}")

    # 判断outfile是否存在且包含文件
    if os.path.exists(out_dir):
        has_file = False
        for item in os.listdir(out_dir):
            full_item = os.path.join(out_dir, item)
            if os.path.isfile(full_item):
                has_file = True
                break
        if has_file:
            print("outfile输出目录非空！程序终止")
            return
    else:
        os.makedirs(out_dir, exist_ok=True)
        print("已创建同级outfile输出文件夹")

    # 支持图片格式
    img_suffix = (".jpg", ".jpeg", ".png", ".bmp", ".webp", ".heic", ".heif")
    process_count = 0
    all_files = os.listdir(input_folder)
    print(f"输入文件夹总条目数：{len(all_files)}")

    for filename in all_files:
        source_path = os.path.join(input_folder, filename)
        # 跳过文件夹，只处理文件
        if not os.path.isfile(source_path):
            print(f"跳过子文件夹：{filename}")
            continue
        ext = os.path.splitext(filename)[1].lower()
        if ext not in img_suffix:
            print(f"跳过非图片文件：{filename}")
            continue

        process_count += 1
        save_path = os.path.join(out_dir, filename)
        # FFmpeg压缩指令
        ffmpeg_cmd = [
            "ffmpeg",
            "-i", source_path,
            "-b:v", "1048k",
            "-q:v", "6",
            "-y", save_path
        ]
        print(f"\n===== 处理第{process_count}张：{filename} =====")
        result = subprocess.run(
            ffmpeg_cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            encoding="utf-8"
        )
        if result.returncode == 0:
            file_kb = round(os.path.getsize(save_path) / 1024, 2)
            print(f"✅ 压缩成功 | 文件大小：{file_kb} KB")
        else:
            print(f"❌ 压缩失败")
            print(f"FFmpeg报错信息：\n{result.stderr}")

    if process_count == 0:
        print("\n⚠️ 未找到符合格式的图片，请检查图片存放位置与格式")
    else:
        print(f"\n✅ 批量压缩完成，总计处理 {process_count} 张图片")

if __name__ == "__main__":
    if not check_ffmpeg():
        input("FFmpeg异常，按回车退出...")
        exit()

    # 输入文件夹 ./img
    batch_ffmpeg_compress_1mb(r"./img")
    input("\n执行结束，回车关闭窗口")