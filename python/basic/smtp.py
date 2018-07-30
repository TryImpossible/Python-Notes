#!/usr/bin/python
#coding=utf-8
import smtplib;
from email.mime.text import MIMEText;
from email.header import Header;


sender = 'from@runoob.com';
receivers = ['865068275@qq.com'];
message = MIMEText('Python 郵件發送測試...', 'plain', 'utf-8');
message['From'] = Header('菜鳥教程', 'utf-8');
message['To'] = Header('測試', 'utf-8');

subject = 'Python SMTP 郵件測試';
message['Subject'] = Header(subject, 'utf-8');

try:
    smtpObj = smtplib.SMTP('localhost');
    smtpObj.sendmail(sender, receivers, message.as_string());
    print '郵件發送成功';
except smtplib.SMTPException:
    print 'Error: 無法發送郵件';