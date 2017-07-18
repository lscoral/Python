# -*- coding: utf-8 -*-

# import packages
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.utils import parseaddr,formataddr

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

# def senmail function
def sendmail(sender,receivers,user,pwd,subject,txt,files):
    message = MIMEMultipart()
    message['From'] = _format_addr('<%s>' %(sender))
    message['To'] = Header('; '.join(receivers),'utf-8')
    message['Subject'] = Header(subject,'utf-8')

    message.attach(MIMEText(txt,'plain','utf-8'))

    # 构造附件
    for f in files:
        att = MIMEText(open(f, 'rb').read(), 'base64', 'utf-8')
        att["Content-Type"] = 'application/octet-stream'
        # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        att["Content-Disposition"] = 'attachment; filename={0}'.format(files[f])
        message.attach(att)

    try:
        smtpObj = smtplib.SMTP_SSL('smtp.exmail.qq.com:465')
        smtpObj.login(user,pwd)
        smtpObj.sendmail(sender,receivers,message.as_string())
        smtpObj.quit
        print ("邮件发送成功")
    except smtplib.SMTPException:
        print ("Error: 无法发送邮件")

if __name__ == '__main__':
    sendmail(sender,receivers,user,pwd,subject,txt,files)

# example:
# sender = '***'
# receivers = ['***','***']
# user ='***'
# pwd = '***'
# subject = '***'
# txt = '***'
# files = {r'C:/Users/lscor/Desktop/test.csv':'test.csv',r'C:/Users/lscor/Desktop/f.csv':'test.csv'}
#
# sendmail(sender,receivers,user,pwd,subject,txt,files)
