import os
import subprocess
import datetime
import glob
import time
import logging

# ===== 配置区域 =====
MYSQL_BIN = r"D:\Mysql\mysql_x64\bin\mysqldump.exe"
BACKUP_DIR = r"E:\data_bak\s7_sql_bak"
WINRAR = r"C:\Program Files (x86)\WinRAR\WinRAR.exe"
DB_HOST = "127.0.0.1"
DB_PORT = "3308"
DB_USER = "root"
DB_PASS = "123456"
DB_NAME = "s7"
RETENTION_DAYS = 90
# ===================

def setup_logging():
    """配置日志系统"""
    logging.basicConfig(
        filename=os.path.join(BACKUP_DIR, "backup_log.txt"),
        format="[%(asctime)s] %(message)s",
        level=logging.INFO,
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    logging.getLogger().addHandler(console)

def validate_paths():
    """路径验证与目录创建"""
    if not os.path.exists(WINRAR):
        logging.error(f"[错误] WinRAR未找到，请修改路径：{WINRAR}")
        exit(1)
    
    try:
        os.makedirs(BACKUP_DIR, exist_ok=True)
    except PermissionError:
        logging.error(f"[错误] 无法创建目录{BACKUP_DIR}，请检查权限！")
        exit(1)

def generate_filename():
    """生成带时间戳的文件名"""
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M")
    sql_file = os.path.join(BACKUP_DIR, f"s7_backup_{timestamp}.sql")
    zip_file = os.path.join(BACKUP_DIR, f"s7_backup_{timestamp}.zip")
    return sql_file, zip_file

def mysql_backup(sql_file):
    """执行MySQL备份"""
    cmd = [
        MYSQL_BIN,
        f"-h{DB_HOST}",
        f"-P{DB_PORT}",
        f"-u{DB_USER}",
        f"-p{DB_PASS}",
        DB_NAME,
        f"--result-file={sql_file}"
    ]
    
    try:
        result = subprocess.run(cmd, check=True, stderr=subprocess.PIPE)
        logging.info(f"数据库备份成功：{sql_file}")
    except subprocess.CalledProcessError as e:
        error_msg = e.stderr.decode().strip()
        logging.error(f"[错误] MySQL备份失败：{error_msg}")
        exit(1)

def compress_file(sql_file, zip_file):
    """使用WinRAR压缩文件并删除源文件"""
    cmd = [
        WINRAR,
        "a",          # 添加文件
        "-afzip",     # 指定ZIP格式
        "-df",        # 压缩后删除源文件
        "-ep1",       # 排除基础目录
        "-ibck",      # 后台运行
        zip_file,
        sql_file
    ]
    
    try:
        subprocess.run(cmd, check=True)
        logging.info(f"压缩成功：{zip_file}")
    except subprocess.CalledProcessError:
        logging.error(f"[错误] 压缩失败，请检查WinRAR或文件权限！")
        exit(1)

def clean_old_backups():
    """清理过期备份文件"""
    now = time.time()
    for file in glob.glob(os.path.join(BACKUP_DIR, "*.zip")):
        if os.path.getmtime(file) < now - RETENTION_DAYS * 86400:
            try:
                os.remove(file)
                logging.info(f"已清理过期备份：{os.path.basename(file)}")
            except PermissionError:
                logging.warning(f"权限不足无法删除：{file}")

if __name__ == "__main__":
    setup_logging()
    validate_paths()
    sql_file, zip_file = generate_filename()
    
    mysql_backup(sql_file)
    compress_file(sql_file, zip_file)
    clean_old_backups()
    
    logging.info(f"备份完成：{zip_file}")