#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 需要先执行pip install zmail安装模块，仅支持Python3

import zmail

# 邮件内容
mail_content = {
    'subject': 'Mail test,good luck!',
    'content': 'This message from zmail!',
    'attachments': '/tmp/hello.txt',
}

# 使用163的smtp服务器
server = zmail.server('abc@163.com','your_password')

def send_mail(receiver):
    server.send_mail(receiver,mail_content)

# 发送邮件,如果有多个收件人,请使用列表方式传参
send_mail('10000@qq.com')

