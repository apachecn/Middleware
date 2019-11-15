import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class MailSender(object):

    def __init__(self, mail_host='smtp.xxx.com', mail_user='xxx', mail_pass='xxx',
            mail_receivers=['xxx@xxx.com'], mail_postfix='xxx.com') :
        # 第三方 SMTP 服务
        self.mail_host = mail_host                                              # 设置服务器
        self.mail_user = mail_user                                              # 用户名
        self.mail_sender = "%s<%s@%s>" % (mail_user, mail_user, mail_postfix)   # 发件箱的后缀
        if "alibaba" in self.mail_host:
            self.mail_user = "%s@%s" % (mail_user, mail_postfix)                # 用户名
        self.mail_pass = mail_pass                                              # 密码
        self.mail_postfix = mail_postfix                                        # 发件箱的后缀
        self.mail_receivers = mail_receivers                                    # 邮件接收人

    def send_mssage(self, title, content, zipname=""):
        if zipname != "":
            # message = MIMEMultipart
            message = MIMEMultipart('alternative')
        else:
            message = MIMEText(content, 'plain', 'utf-8')  # 内容, 格式, 编码

        message['From'] =  "{}".format(self.mail_sender)
        message['To'] = ",".join(self.mail_receivers)
        message['Subject'] = title
 
        if zipname != "":
            # 发送的文本文件
            part_text = MIMEText(content, 'plain', 'utf-8')  
            message.attach(part_text)
            # 构造附件
            part_zip = MIMEText(open(zipname, 'rb').read(), 'base64', 'utf-8')
            part_zip["Content-Type"] = 'application/octet-stream'
            part_zip["Content-Disposition"] = 'attachment; filename=%s' % (zipname.split("/")[-1])
            message.attach(part_zip)
        try:
            if "alibaba" in self.mail_host: 
                client = smtplib.SMTP()
                client.connect(self.mail_host, 25)
            else:
                client = smtplib.SMTP_SSL(self.mail_host)
                # client = smtplib.SMTP_SSL(self.mail_host, 465)  # 启用SSL发信, 端口一般是465
            client.login(self.mail_user, self.mail_pass)  # 登录验证
            client.sendmail(self.mail_sender, self.mail_receivers, message.as_string())  # 发送
            print("mail has been send successfully.")
            client.quit()
            return True
        except Exception as e:
            print("Failed", e)
            return False


# if __name__ == '__main__':
#     mail_host = 'smtp.163.com'
#     mail_user = 'test_mail_pk'
#     # mail_pass='pk123456', 
#     # pc 密码
#     mail_pass = 'pk123321'
#     mail_postfix = '163.com'
#     mail_receivers = ['test_mail_pk@163.com']

#     mail = MailSender(mail_host, mail_user, mail_pass, mail_receivers, mail_postfix)
#     status = mail.send_mssage('我是谁', "ddd", "data/poetry.txt")

#     if status:
#         print("发送成功")
#     else:
#         print("发送失败")
