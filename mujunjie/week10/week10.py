#1、使用python给自己qq邮箱发送一份邮件
 
import smtplib
from email.mime.text import MIMEText
from email.header import Header
 
def mail(sender,receivers,subject,content,frm,to,log_pass,mail_addr:str="smtp.exmail.qq.com",mail_port:int=465):
    sender = sender#真实发件人邮箱 
    receivers = [ receivers ] #真实接收邮件人邮箱
 
# 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
    message = MIMEText(content, 'plain', 'utf-8')
    message['From'] = Header(frm, 'utf-8')   # 标题显示发件人
    message['To'] =  Header(to, 'utf-8')        #标题显示收件人 
    message['Subject'] = Header(subject, 'utf-8')#邮件标题
    smtpObj = smtplib.SMTP_SSL(mail_addr,mail_port)  #腾讯邮箱测试，需要SSL连接 
    smtpObj.login(sender,log_pass)  #登录邮箱 
    smtpObj.sendmail(sender, receivers, message.as_string()) #发送邮箱 三个参数，发件人邮箱，收件人邮箱，消息内容处理 
    print ("邮件发送成功")
 #发件人地址，收件人地址，标题，内容，标题显示发件人地址，标题显示收件人地址，密码，smtp地址，smtp端口
'''mail("#","#","测试","测试函数","AAA","BBB","D6Kp7t5JKtEcNJqD")'''
class sendmail:
    def __init__(self,sender,receivers,subject,content,frm,to,log_pass,mail_add:str="smtp.exmail.qq.com",mail_port:int=465):
        self.sender=sender
        self.receivers = [receivers]
        self.message = MIMEText(content,'plain', 'utf-8')
        self.message['From'] = Header(frm,'utf-8')
        self.message['To'] = Header(to,'utf-8')
        self.message['Subject'] = Header(subject,'utf-8')
        self.log_pass = log_pass
        self.mail_add = mail_add
        self.mail_port = mail_port
    def send_mail(self):
        smtpObj = smtplib.SMTP_SSL(self.mail_add,self.mail_port)
        smtpObj.login(self.sender,self.log_pass)
        smtpObj.sendmail(self.sender,self.receivers,self.message.as_string())
        print(1111)

#c = sendmail("#","qq.com","测试","测试类","AAA","BBB","D6Kp7t5JKtEcNJqD")
#c.send_mail()



#2、实现一个函数获取一个目录下所有以.py结尾的文件（包含目录下的子目录中的.py文件）
#温馨提示：请童鞋们于本周日前完成作业
import pathlib
#lst = []
def path(dir,lst = []):
#    global lst
    pth = pathlib.Path(dir)
    if not pth.is_dir():
        print ("not dir")
        return
    for i in pth.iterdir():
        if str(i).endswith(".py"):
            lst.append(i)
        if i.is_dir():
            path(i, lst)
    return lst
print(path("/tmp"))



