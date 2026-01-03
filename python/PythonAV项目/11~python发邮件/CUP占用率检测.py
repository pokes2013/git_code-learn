# coding=utf-8
import time
import psutil
import os

import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# email 用于构建邮件内容
from email.mime.text import MIMEText

# 构建邮件头
from email.header import Header


# 发送右键模块
def fs_mail(server_name):
    sender_email = "pokes@126.com"
    sender_password = "AZLDSVDDNWFMWUCQ"

    server = smtplib.SMTP_SSL("smtp.126.com", 465)
    server.login(sender_email, sender_password)

    cpuz = psutil.cpu_percent(interval=1.0)  # cpu占用率
    memoryz = psutil.virtual_memory().percent  # 内存占用率
    deskd = psutil.disk_usage("d:\\").percent
    deske = psutil.disk_usage("e:\\").percent
    systime = time.strftime("%H:%M:%S", time.localtime())

    receiver_emails = ["pokes@163.com", "175239577@qq.com"]
    for receiver_email in receiver_emails:
        msg = MIMEMultipart("alternative")
        msg["Subject"] = "{}告警通知".format(server_name)
        msg["From"] = sender_email
        msg["To"] = receiver_email
        html = """
            <h1>告警通知</h1>
            <h2>当前时间:{}</h2>
            <h2>server:{}</h2>
            <h2>CPU占用率:{}%</h2>
            <h2>D盘空间占用率:{}%</h2>
            <h2>E盘空间占用率:{}%</h2>
            
            """.format(
            systime, server_name, cpuz, deskd, deske
        )
        msg.attach(MIMEText(html, "html"))
        server.sendmail(sender_email, receiver_email, msg.as_string())

    server.quit()


cpuz = psutil.cpu_percent(interval=1.0)  # cpu占用率
memoryz = psutil.virtual_memory().percent  # 内存占用率
deskd = psutil.disk_usage("d:\\").percent
deske = psutil.disk_usage("e:\\").percent
if deskd > 90 or deske > 90:
    fs_mail("xizai_server")
    print("邮件已经发送")

