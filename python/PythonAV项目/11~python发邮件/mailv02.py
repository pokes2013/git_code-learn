import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sender_email = "pokes@126.com"
sender_password = "AZLDSVDDNWFMWUCQ"

server = smtplib.SMTP_SSL("smtp.126.com", 465)
server.login(sender_email, sender_password)

receiver_emails = ["pokes@163.com", "175239577@qq.com"]
for receiver_email in receiver_emails:
    msg = MIMEMultipart("alternative")
    msg["Subject"] = "告警通知"
    msg["From"] = sender_email
    msg["To"] = receiver_email
    html = """
        <h1>告警通知</h1>
        <h2>CPU占用率高达90%以上，请加紧处理！</h2>
    """
    msg.attach(MIMEText(html, "html"))
    server.sendmail(sender_email, receiver_email, msg.as_string())

server.quit()
