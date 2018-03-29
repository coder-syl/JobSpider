# coding=utf-8
import smtplib
from email.mime.text import MIMEText
def sendEmail(msg):
    msg_from = '2522011411@qq.com'  # 发送方邮箱
    passwd = 'gllmvbsubpovebgd'  # 填入发送方邮箱的授权码
    msg_to = '1094754411@qq.com'  # 收件人邮箱

    subject = "python 爬虫状态监控"  # 主题
    content =msg # 正文
    msg = MIMEText(content)
    msg['Subject'] = subject
    msg['From'] = msg_from
    msg['To'] = msg_to
    try:
        s = smtplib.SMTP_SSL("smtp.qq.com", 465) # 邮件服务器及端口号
        s.login(msg_from, passwd)
        s.sendmail(msg_from, msg_to, msg.as_string())
        print("发送成功")
    except Exception as e:
        print("发送失败")
        print(e)