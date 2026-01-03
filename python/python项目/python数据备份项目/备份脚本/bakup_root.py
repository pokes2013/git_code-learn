
import os
from zipfile import ZipFile, ZIP_DEFLATED
from datetime import datetime


def zip_directory_with_date(directory_path, output_dir):
    # 生成带日期时间的文件名（格式：webapps_YYYYMMDD_HHMM.zip）
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")  # 例如 20240715_1530
    zip_name = f"webapps_{timestamp}.zip"
    output_zip_path = os.path.join(output_dir, zip_name)

    # 创建压缩文件
    with ZipFile(output_zip_path, 'w', ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, start=directory_path)
                zipf.write(file_path, arcname)

    print(f"备份完成：{output_zip_path}")


# 调用示例
zip_directory_with_date(
    directory_path=r'D:\Program Files\s7\webapps',
    output_dir=r'E:\data_bak\ROOT'  # 确保此目录存在！
)