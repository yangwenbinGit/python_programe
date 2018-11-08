#!/usr/bin/python3
#-*-coding:UTF-8-*-
#SMTP电子邮件发送附件和内容
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.header import Header
from email.utils import parseaddr,formataddr
#先定义署名格式化函数
def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

#发送人，接收人
sender='420097009@qq.com'
pwd='vcbuejwbgzdqcbdi' #请自行登陆邮箱打开SMTP服务，会自动生成第三方授权码，不是登陆密码！
# receiver='yangwenbin@yjhealth.net'
receiver ='2495905078@qq.com'
#格式化的署名和接收人信息
message=MIMEMultipart()
message['From']=_format_addr('宝宝<%s>'%sender)
message['To']=_format_addr(receiver)
message['Subject']=('送你一个美女！！')
message.attach(MIMEText('<html><body>'
                        +'<h1>Hello</h1>'
                        +'<p>美女照片<img src="cid:Imgid">'
                        +'</body></html>','html','utf-8'))

#MIMEImage，只要打开相应图片，再用read()方法读入数据，指明src中的代号是多少，如这里是'Imgid’，在HTML格式里就对应输入。
with open('timg.jpg','rb') as f:
    mime=MIMEImage(f.read())
    mime.add_header('Content-ID','Imgid')
    message.attach(mime)

#发送邮件！
try:
    # 加密SMTP 这块测试的时候导致发布出去了
    # smtp_server = 'smtp.gmail.com'
    # smtp_port = 587
    # server = smtplib.SMTP(smtp_server, smtp_port)
    # server.starttls()

    smtpobj=smtplib.SMTP_SSL('smtp.qq.com',465)
    smtpobj.login(sender,pwd)
    smtpobj.sendmail(sender,[receiver],message.as_string())
    print('邮件发送成功')
    smtpobj.quit()
except smtplib.SMTPException as e:
    print('邮件发送失败，Case:%s'%e)