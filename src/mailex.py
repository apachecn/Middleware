# coding: utf-8

# 邮件直投（foxmail 客户端的特快专递模式）
# 需要 co.html：内容
# recivers.json：base64 编码的发送列表

import smtplib
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from email.header import Header
from dns import resolver
import re
from bs4 import BeautifulSoup as bs
import base64
import json
import random

def b64decode(s, encoding='utf-8'):
    return base64.b64decode(s.encode(encoding)).decode(encoding)


def format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

def send_mail_ex(sender, reciver, title, co, co_type='plain'):
    try:
    
        domain = re.search(r'@(.+)', reciver).group(1)
        r = resolver.query(domain, 'MX').response.answer
        if len(r) == 0: return (False, '解析失败')
        host = r[0].items[0].to_text().split(' ')[1][:-1]
        
        smtp = smtplib.SMTP(host)

        message = MIMEText(co, co_type, 'utf-8')
        message['From'] = format_addr(sender)
        message['To'] = reciver
        message['Subject'] = Header(title, 'utf-8')
        
        smtp.sendmail(sender, reciver, message.as_string())
        smtp.close()
        
        return (True, '')
    except Exception as ex:
        return (False, str(ex))

def get_title(html):
    root = bs(html, 'lxml')
    if not root.h1: return ''
    return root.h1.text

def main():
    co = open('co.html', encoding='utf-8').read()
    title = get_title(co)
    
    recivers = json.load(open('recivers.json'))
    recivers = random.choices(recivers, k=10000)
    recivers = [b64decode(r) for r in recivers]
    sender = 'Example <admin@mail.example.com>'

    for reciver in recivers:
        r = send_mail_ex(sender, reciver, title, co, 'html')
        if r[0]:
            print(f'{sender} -> {reciver} 成功')
        else:
            print(f'{sender} -> {reciver} 失败：{r[1]}')
    
if __name__ == '__main__': main()
