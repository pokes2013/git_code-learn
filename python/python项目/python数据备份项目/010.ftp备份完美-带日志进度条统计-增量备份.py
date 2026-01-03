# ftp备份程序
"""
# 功能:
    # 增量备份，根据文件修改时间进行校验，没有修改就不用下载
    # 有日志，日志在程序目录
    # 程序完成时，有数据统计，按回车键关闭；
    # 备份过程中每个文件显示下载进度条；
# 缺点:
    # ftp密码是明码

# 注意:
    # 只能下载（拉式）
    # 不能上传（不支持推）
    # 不能视作同步，如果想实现同步数据，可以在计划任务里面，进行定时出发，然后把代码结尾的“按回车键推出”去掉；
"""



import os
import ftplib
import socket
import logging
from datetime import datetime
from tqdm import tqdm  # 进度条库

# 全局变量用于统计
total_files = 0
skipped_files = 0
downloaded_files = 0
total_bytes = 0
downloaded_bytes = 0

def setup_logging():
    """配置日志系统"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('ftp_download.log'),
            logging.StreamHandler()
        ]
    )

def get_local_file_mtime(local_path):
    """获取本地文件的修改时间"""
    if os.path.exists(local_path):
        return os.path.getmtime(local_path)
    return 0

def parse_ftp_time(time_str):
    """解析FTP服务器返回的时间字符串"""
    # 示例格式: "20230725123000" -> 年(4)月(2)日(2)时(2)分(2)秒(2)
    if len(time_str) >= 14:
        year = int(time_str[:4])
        month = int(time_str[4:6])
        day = int(time_str[6:8])
        hour = int(time_str[8:10])
        minute = int(time_str[10:12])
        second = int(time_str[12:14])
        return datetime(year, month, day, hour, minute, second).timestamp()
    return 0

class ProgressBarFTP(ftplib.FTP):
    """带进度条的FTP类"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pbar = None

    def retrbinary(self, cmd, callback, blocksize=8192, rest=None, desc=None):
        """重写retrbinary方法以支持进度条"""
        self.voidcmd('TYPE I')
        conn = self.transfercmd(cmd, rest)

        try:
            # 获取文件总大小
            total_size = None
            if cmd.startswith('RETR'):
                resp = self.sendcmd('SIZE ' + cmd[5:])
                if resp.startswith('213'):
                    total_size = int(resp[3:].strip())

            # 初始化进度条
            self.pbar = tqdm(
                total=total_size,
                unit='B',
                unit_scale=True,
                unit_divisor=1024,
                desc=desc,
                leave=False
            )

            # 包装回调函数以更新进度条
            def wrapped_callback(data):
                self.pbar.update(len(data))
                callback(data)

            while True:
                data = conn.recv(blocksize)
                if not data:
                    break
                wrapped_callback(data)

            self.pbar.close()
            self.pbar = None

        finally:
            conn.close()
            return self.voidresp()

def download_from_ftp(host, username, password, remote_path, local_path, port=6000, timeout=30, incremental=True):
    """
    从FTP服务器下载文件或目录（支持增量备份和进度条）

    参数:
        host: FTP服务器地址(IP或域名)
        username: FTP用户名
        password: FTP密码
        remote_path: 远程路径
        local_path: 本地保存路径
        port: FTP控制端口(默认6000)
        timeout: 连接超时时间(秒)
        incremental: 是否使用增量备份模式(默认True)
    """
    global total_files, skipped_files, downloaded_files, total_bytes, downloaded_bytes

    setup_logging()

    try:
        # 首先检查主机名是否可解析
        try:
            socket.getaddrinfo(host, port)
        except socket.gaierror as e:
            logging.error(f"无法解析主机名: {host} (错误: {str(e)})")
            return False
        except Exception as e:
            logging.error(f"主机名解析时发生意外错误: {str(e)}")
            return False

        logging.info(f"尝试连接FTP服务器: {host}:{port} (增量模式: {'开启' if incremental else '关闭'})")

        try:
            # 创建FTP连接，设置超时
            ftp = ProgressBarFTP()
            ftp.connect(host, port, timeout=timeout)
            ftp.login(username, password)
            ftp.set_pasv(True)

            logging.info(f"成功连接到FTP服务器: {host}")

            # 标准化路径
            remote_path = remote_path.replace('\\', '/')
            if not remote_path.startswith('/'):
                remote_path = '/' + remote_path

            # 判断远程路径类型
            try:
                # 尝试获取大小，成功则是文件
                try:
                    size = ftp.size(remote_path)
                    total_files += 1
                    total_bytes += size

                    # 获取远程文件修改时间
                    mdtm = ftp.sendcmd(f"MDTM {remote_path}").split()[1]
                    remote_mtime = parse_ftp_time(mdtm)

                    local_mtime = get_local_file_mtime(local_path)

                    if incremental and remote_mtime <= local_mtime:
                        skipped_files += 1
                        logging.info(f"文件未修改，跳过下载: {remote_path} (远程: {datetime.fromtimestamp(remote_mtime)}, 本地: {datetime.fromtimestamp(local_mtime)})")
                        return True

                    logging.info(f"正在下载文件: {remote_path} (大小: {size}字节, 修改时间: {datetime.fromtimestamp(remote_mtime)})")

                    # 确保本地目录存在
                    local_dir = os.path.dirname(local_path)
                    if local_dir and not os.path.exists(local_dir):
                        os.makedirs(local_dir)

                    # 下载文件（带进度条）
                    filename = os.path.basename(remote_path)
                    with open(local_path, 'wb') as f:
                        ftp.retrbinary(f'RETR {remote_path}', f.write, desc=filename)

                    # 设置本地文件的修改时间为远程文件的时间
                    os.utime(local_path, (remote_mtime, remote_mtime))

                    downloaded_files += 1
                    downloaded_bytes += size
                    logging.info(f"文件下载成功: {local_path}")
                    return True
                except ftplib.error_perm:
                    # 是目录
                    logging.info(f"正在下载目录: {remote_path}")

                    # 确保本地目录存在
                    os.makedirs(local_path, exist_ok=True)

                    # 递归下载目录
                    download_ftp_directory(ftp, remote_path, local_path, incremental)

                    logging.info(f"目录下载完成: {remote_path} -> {local_path}")
                    return True

            except ftplib.error_perm as e:
                logging.error(f"无法访问路径: {remote_path} (错误: {str(e)})")
                return False

        except ftplib.all_errors as e:
            logging.error(f"FTP操作错误: {str(e)}")
            return False
        finally:
            try:
                ftp.quit()
            except:
                pass

    except Exception as e:
        logging.error(f"发生意外错误: {str(e)}")
        return False

def download_ftp_directory(ftp, remote_dir, local_dir, incremental=True):
    """递归下载FTP目录（支持增量备份和进度条）"""
    global total_files, skipped_files, downloaded_files, total_bytes, downloaded_bytes

    try:
        # 获取目录列表（详细格式，包含修改时间）
        items = []
        try:
            ftp.cwd(remote_dir)
            # 使用MLSD命令获取详细文件信息（如果服务器支持）
            try:
                items = []
                for name, facts in ftp.mlsd():
                    if name in ('.', '..'):
                        continue
                    items.append((name, facts))
            except ftplib.error_perm:
                # 如果MLSD不支持，回退到LIST
                lines = []
                ftp.retrlines('LIST', lines.append)
                for line in lines:
                    parts = line.split()
                    if len(parts) < 9:
                        continue
                    name = ' '.join(parts[8:])
                    if name in ('.', '..'):
                        continue
                    # 解析LIST格式的时间（简化处理）
                    time_str = ' '.join(parts[5:8])
                    items.append((name, {'modify': time_str}))
        except ftplib.error_perm as e:
            logging.error(f"无法列出目录: {remote_dir} (错误: {str(e)})")
            return

        for item_name, facts in items:
            remote_path = f"{remote_dir}/{item_name}".replace('//', '/')
            local_path = os.path.join(local_dir, item_name)

            try:
                # 获取修改时间
                remote_mtime = 0
                if 'modify' in facts:
                    remote_mtime = parse_ftp_time(facts['modify'])

                # 判断是文件还是目录
                if 'type' in facts and facts['type'] == 'dir':
                    # 是目录
                    os.makedirs(local_path, exist_ok=True)
                    download_ftp_directory(ftp, remote_path, local_path, incremental)
                else:
                    # 是文件
                    total_files += 1
                    size = 0
                    try:
                        size = ftp.size(remote_path)
                        total_bytes += size
                    except:
                        pass

                    local_mtime = get_local_file_mtime(local_path)

                    if incremental and remote_mtime <= local_mtime:
                        skipped_files += 1
                        logging.info(f"文件未修改，跳过下载: {remote_path} (远程: {datetime.fromtimestamp(remote_mtime)}, 本地: {datetime.fromtimestamp(local_mtime)})")
                        continue

                    # 下载文件（带进度条）
                    try:
                        with open(local_path, 'wb') as f:
                            ftp.retrbinary(f'RETR {remote_path}', f.write, desc=item_name)

                        # 设置本地文件的修改时间为远程文件的时间
                        if remote_mtime > 0:
                            os.utime(local_path, (remote_mtime, remote_mtime))

                        downloaded_files += 1
                        if size > 0:
                            downloaded_bytes += size
                        logging.info(f"下载文件: {remote_path} -> {local_path} (修改时间: {datetime.fromtimestamp(remote_mtime)})")
                    except Exception as e:
                        logging.error(f"下载文件失败: {remote_path} - {str(e)}")

            except ftplib.all_errors as e:
                logging.error(f"下载项目时出错: {remote_path} - {str(e)}")

    except Exception as e:
        logging.error(f"下载目录时出错: {remote_dir} - {str(e)}")
        raise

def format_bytes(size):
    """格式化字节数为易读格式"""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024.0:
            return f"{size:.2f} {unit}"
        size /= 1024.0
    return f"{size:.2f} PB"

if __name__ == "__main__":
    # 重置统计信息
    total_files = 0
    skipped_files = 0
    downloaded_files = 0
    total_bytes = 0
    downloaded_bytes = 0

    # 请修改为您的实际FTP信息
    FTP_CONFIG = {
        'host': '192.168.1.22',
        'username': 'pokes',
        'password': '4501596',
        'remote_path': '/',
        'local_path': 'f:/DATA/server_data_bak',
        'port': 6000,  # 使用您的特殊控制端口
        'timeout': 60,
        'incremental': True  # 启用增量备份
    }

    # 测试主机名解析
    try:
        socket.getaddrinfo(FTP_CONFIG['host'], FTP_CONFIG['port'])
        print(f"主机名解析成功: {FTP_CONFIG['host']}")
    except socket.gaierror as e:
        print(f"错误: 无法解析主机名 {FTP_CONFIG['host']} (错误: {str(e)})")
        print("请检查:")
        print("1. 主机名或IP地址是否正确")
        print("2. 网络连接是否正常")
        print("3. 如果您使用的是主机名，尝试改用IP地址")
        exit(1)

    # 执行下载
    success = download_from_ftp(**FTP_CONFIG)

    # 打印汇总信息
    print("\n" + "="*50)
    print("备份操作汇总:")
    print(f"总文件数: {total_files}")
    print(f"已下载文件: {downloaded_files}")
    print(f"跳过文件(未修改): {skipped_files}")
    print(f"总数据量: {format_bytes(total_bytes)}")
    print(f"实际下载量: {format_bytes(downloaded_bytes)}")
    print("="*50)

    if success:
        print("\n下载操作成功完成!")
        os.startfile(FTP_CONFIG['local_path'])
    else:
        print("\n下载过程中出现错误，请查看日志文件 ftp_download.log")

