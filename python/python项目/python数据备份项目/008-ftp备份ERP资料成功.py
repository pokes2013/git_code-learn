
# 缺点就是每次都是完全备份，并非增量备份，占用带宽，备份时间比较长



import os
import ftplib
import socket
import logging
from datetime import datetime


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


def download_from_ftp(host, username, password, remote_path, local_path, port=6000, timeout=30):
    """
    从FTP服务器下载文件或目录（针对特殊端口配置的版本）

    参数:
        host: FTP服务器地址(IP或域名)
        username: FTP用户名
        password: FTP密码
        remote_path: 远程路径
        local_path: 本地保存路径
        port: FTP控制端口(默认6000)
        timeout: 连接超时时间(秒)
    """
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

        logging.info(f"尝试连接FTP服务器: {host}:{port}")

        try:
            # 创建FTP连接，设置超时
            ftp = ftplib.FTP()
            ftp.connect(host, port, timeout=timeout)
            ftp.login(username, password)

            # 设置被动模式，并指定被动模式端口范围
            ftp.set_pasv(True)

            # 对于某些FTP服务器，可能需要设置被动模式端口范围
            # 注意：标准ftplib不直接支持设置被动端口范围，这里只是示例
            # 如果连接失败，可能需要使用更底层的socket控制

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
                    logging.info(f"正在下载文件: {remote_path} (大小: {size}字节)")

                    # 确保本地目录存在
                    local_dir = os.path.dirname(local_path)
                    if local_dir and not os.path.exists(local_dir):
                        os.makedirs(local_dir)

                    # 下载文件
                    with open(local_path, 'wb') as f:
                        ftp.retrbinary(f'RETR {remote_path}', f.write)

                    logging.info(f"文件下载成功: {local_path}")
                    return True
                except ftplib.error_perm:
                    # 是目录
                    logging.info(f"正在下载目录: {remote_path}")

                    # 确保本地目录存在
                    os.makedirs(local_path, exist_ok=True)

                    # 递归下载目录
                    download_ftp_directory(ftp, remote_path, local_path)

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


def download_ftp_directory(ftp, remote_dir, local_dir):
    """递归下载FTP目录"""
    try:
        # 获取目录列表
        items = []
        try:
            ftp.cwd(remote_dir)
            items = ftp.nlst()
        except ftplib.error_perm as e:
            logging.error(f"无法列出目录: {remote_dir} (错误: {str(e)})")
            return

        for item_name in items:
            if item_name in ('.', '..'):
                continue

            remote_path = f"{remote_dir}/{item_name}".replace('//', '/')
            local_path = os.path.join(local_dir, item_name)

            try:
                # 尝试获取大小，判断是文件还是目录
                try:
                    ftp.size(remote_path)
                    # 是文件
                    with open(local_path, 'wb') as f:
                        ftp.retrbinary(f'RETR {remote_path}', f.write)
                    logging.info(f"下载文件: {remote_path} -> {local_path}")
                except ftplib.error_perm:
                    # 是目录
                    os.makedirs(local_path, exist_ok=True)
                    download_ftp_directory(ftp, remote_path, local_path)

            except ftplib.all_errors as e:
                logging.error(f"下载项目时出错: {remote_path} - {str(e)}")

    except Exception as e:
        logging.error(f"下载目录时出错: {remote_dir} - {str(e)}")
        raise


if __name__ == "__main__":
    # 示例配置 - 请修改为您的实际FTP信息
    FTP_CONFIG = {
        'host': '192.168.1.22',
        'username': 'pokes',
        'password': '4501596',
        'remote_path': '/',
        'local_path': 'd:/downloads/erp_ftp_bak',
        'port': 6000,  # 使用您的特殊控制端口
        'timeout': 60
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

    if success:
        print("下载操作成功完成!")
    else:
        print("下载过程中出现错误，请查看日志文件 ftp_download.log")