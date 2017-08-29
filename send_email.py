# -*- coding: utf-8 -*-
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
def sendemail(filename):
    sender = '97544234@qq.com'#发送邮件
    receiver = '97544234@qq.com'#接收邮件
    smtpserver ='smtp.qq.com'
    password = '****'
    subject='测试'
    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = Header(subject, 'utf-8')
    msgRoot.attach(MIMEText('测试测试', 'plain', 'utf-8'))
    att = MIMEText(open('bug.pdf', 'rb').read(), 'base64', 'utf-8')
    att["Content-Type"] = 'application/octet-stream'
    att["Content-Disposition"] = 'attachment; filename='+filename
    msgRoot.attach(att)
    smtp = smtplib.SMTP_SSL(smtpserver, 465)
    #smtp.connect(smtpserver)
    smtp.login(sender,password)
    smtp.sendmail(sender, receiver, msgRoot.as_string())
    smtp.quit()
    print 'email has send out !'
if __name__=="__main__":
    sendemail('bug.pdf')