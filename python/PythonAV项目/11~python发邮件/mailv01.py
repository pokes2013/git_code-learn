# smtplib 用于邮件的发信动作
import smtplib

# email 用于构建邮件内容
from email.mime.text import MIMEText

# 构建邮件头
from email.header import Header


# 创建 SMTP 对象
smtp = smtplib.SMTP()
# 连接（connect）指定服务器
smtp.connect("smtp.126.com", port=465)
# 登录，需要：登录邮箱和授权码
smtp.login(user="pokes@126.com", password="AZLDSVDDNWFMWUCQ")

# 构造MIMEText对象，邮箱正文内容，第一个参数为内容，第二个参数为格式(plain 为纯文本)，第三个参数为编码
message = MIMEText("python邮件发送测试...", "plain", "utf-8")
# 邮件头信息
message["From"] = Header("告警信息", "utf-8")  # 发件人的昵称
message["To"] = Header("管理员", "utf-8")  # 收件人的昵称
message["Subject"] = Header("Python 告警信息-测试", "utf-8")  # 定义主题内容
# print(message)

smtp.sendmail(
    from_addr="pokes@126.com", to_addrs="ysd1315@sina.com", msg=message.as_string()
)


server.quit()
