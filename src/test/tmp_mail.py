import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

 
# 第三方 SMTP 服务
mail_host = "smtp.163.com"      # SMTP服务器
mail_user = "test_mail_pk"      # 用户名
mail_pass = "pk123321"          # 授权密码，非登录密码
 
sender = 'test_mail_pk@163.com'       # 发件人邮箱(最好写全, 不然会失败)
receivers = ['test_mail_pk@163.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

content = '我用Python'
title = '人生苦短'  # 邮件主题
 
def sendEmail():
    message = MIMEText(content, 'plain', 'utf-8')  # 内容, 格式, 编码
    message['From'] = "{}".format(sender)
    message['To'] = ",".join(receivers)
    message['Subject'] = title

    try:
        smtpObj = smtplib.SMTP_SSL(mail_host)
        # smtpObj = smtplib.SMTP_SSL(mail_host, 465)  # 启用SSL发信, 端口一般是465
        smtpObj.login(mail_user, mail_pass)  # 登录验证
        smtpObj.sendmail(sender, receivers, message.as_string())  # 发送
        print("mail has been send successfully.")
        smtpObj.quit()
    except smtplib.SMTPException as e:
        print(e)
 
def send_email2(SMTP_host, from_account, from_passwd, to_account, subject, content):
    email_client = smtplib.SMTP(SMTP_host)
    email_client.login(from_account, from_passwd)
    # create msg
    msg = MIMEText(content, 'plain', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')  # subject
    msg['From'] = from_account
    msg['To'] = to_account
    email_client.sendmail(from_account, to_account, msg.as_string())
    email_client.quit()

def send_email_file():

    message = MIMEMultipart()
    message['From'] = "{}".format(sender)
    message['To'] = ",".join(receivers)
    message['Subject'] = title

    # 发送的文本文件
    part1 = MIMEText("ddddd", 'plain', 'utf-8')  
    message.attach(part1)

    # 构造附件1
    zipname = "data/city.xlsx"
    part2 = MIMEText(open(zipname, 'rb').read(), 'base64', 'utf-8')
    part2["Content-Type"] = 'application/octet-stream'
    part2["Content-Disposition"] = 'attachment; filename=%s' % (zipname)
    message.attach(part2)

    try:
        smtpObj = smtplib.SMTP_SSL(mail_host)
        # smtpObj = smtplib.SMTP_SSL(mail_host, 465)  # 启用SSL发信, 端口一般是465
        smtpObj.login(mail_user, mail_pass)  # 登录验证
        smtpObj.sendmail(sender, receivers, message.as_string())  # 发送
        print("mail has been send successfully.")
        smtpObj.quit()
    except smtplib.SMTPException as e:
        print(e)
 

if __name__ == '__main__':
    # sendEmail()
    send_email_file()
    # receiver = '***'
    # send_email2(mail_host, mail_user, mail_pass, receiver, title, content)