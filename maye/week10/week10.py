# 1、使用python给自己qq邮箱发送一份邮件
# 2、实现一个函数获取一个目录下所有以.py结尾的文件（包含目录下的子目录中的.py文件）


import smtplib
from email.mime.text import MIMEText
import sys
mail_host = 'xxxxx'
mail_user = 'xxx'
mail_password = 'xxx'
mail_postfix = 'xxxx'
def send_mail(to_list,subject,content):
    me = "zabbix 监控告警平台"+"<"+mail_user+"@"+mail_postfix+">"
    msg = MIMEText(content, 'plain', 'utf-8')
    msg['Subject'] = subject
    msg['From'] = me
    msg['to'] = to_list
    try:
        s = smtplib.SMTP()
        s.connect(mail_host)
        s.login(mail_user,mail_password)
        s.sendmail(me,to_list,msg.as_string())
        s.close()
        return True
    except Exception,e:
        print str(e)
        return False
if __name__ == "__main__":
    send_mail(sys.argv[1], sys.argv[2], sys.argv[3])




'''
    from pathlib import Path
    
    def showfile(path:str='.',sufix='*.py'):
    return [ str(file.name) for file in Path(path).rglob(sufix)]
    
    print(showfile('/Users/mac/Desktop/3.1'))
    '''
