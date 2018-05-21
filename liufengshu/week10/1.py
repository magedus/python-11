from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr
import smtplib

from_addr='maple_lfs@163.com'
password='xxx'
to_addr='1547973055@qq.com'
smtp_server='smtp.163.com'

msg = MIMEText('<html><body><h1>Hello</h1>' +
    '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
    '</body></html>', 'html', 'utf-8')
# msg=MIMEText('Hello, send by Python...','plain','utf-8')
msg['From']=formataddr((Header('Python爱好者','utf-8').encode(),from_addr))
msg['To']=formataddr((Header('管理员','utf-8').encode(),to_addr))
msg['Subject']=Header('来自SMTP的问候.......','utf-8').encode()



server=smtplib.SMTP(smtp_server,25)
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()
