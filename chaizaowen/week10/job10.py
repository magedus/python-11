
#实现一个函数获取一个目录下所有以.py结尾的文件（包含目录下的子目录中的.py文件）

from pathlib import Path

def findpy(path):
    p = Path(path)
    yield from p.rglob('*.py')

pysuffix = findpy('dir1')
for i in pysuffix:
    print(i)


#使用python给自己qq邮箱发送一份邮件

import smtplib
from email.mime.text import MIMEText

def send_mail(from_addr, to_addrs, content):
    msg = MIMEText(content, 'plain', 'utf-8')
    msg['From'] = 'chaizaowen@163.com'
    msg['to'] = '409631012@qq.com'
    msg['Subject'] = 'do homework'

    try:
        # s = None
        s = smtplib.SMTP()
        s.connect('smtp.163.com')
        s.login('chaizaowen@163.com', '*')
        s.sendmail(from_addr, to_addrs, msg.as_string())
    except smtplib.SMTPException as e:
        print('Error:', e)
    finally:
        # if s is not None:
        #     s.quit()
        try:
            s.quit()
            # print(s)
        except:
            pass

if __name__ == '__main__':
    content = '''
    this is a test email.
    '''
    send_mail('chaizaowen@163.com', '409631012@qq.com', content)