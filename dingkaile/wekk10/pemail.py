import smtplib
from email.mime.text import MIMEText

from_addr = input("input source address: ")
password = input('input password: ')
to_addr = '807985143@qq.com'


msg = MIMEText('hello，test email','plain','utf-8')
smtp_server = 'smtp.163.com'
msg['From'] = from_addr
msg['To'] = to_addr
msg['Subject'] = 'test python email'

server = smtplib.SMTP(smtp_server,25)
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,to_addr,msg.as_string())
server.quit()