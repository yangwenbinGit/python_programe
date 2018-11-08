# SMTP发送邮件

# Python对于SMTP的支持有smtplib和email两个模块,email负责构造邮件,smtplib负责发送邮件
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# 构造MIMEText对象时,第一个参数是邮件正文,第一个参数是MIME的subtype,传入'plain'表示纯文本,最终的MIME就是'text/plain'
# 最后一定要用utf-8编码保证多语言的兼容
msg = MIMEText('hello,send by python...','plain','utf-8')

# 然后，通过SMTP发出去：
# 输入Email地址和口令:

# 420097009@qq.com  发件人邮箱
# vcbuejwbgzdqcbdi   qq邮箱授权码
# yangwenbin@yjhealth.net   收件人邮箱
# 2495905078@qq.com   小雷
# smtp.qq.com       SMTP server

# from_addr = input('From:')
# password = input('Password :')  # 授权码,不是邮箱密码
# # 输入收件人地址:
# to_addr = input('To:')
# # 输入SMTP服务器地址:
# smtp_server = input('SMTP server:')
#
# # 这样正常已经发送出去了,但是发现只有内容
# import smtplib
# server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口是25
# server.set_debuglevel(1)
# server.login(from_addr, password)
# server.sendmail(from_addr, [to_addr], msg.as_string())
# server.quit()

# 仔细观察，发现如下问题：
#
# 邮件没有主题；
# 收件人的名字没有显示为友好的名字，比如Mr Green <green@example.com>；
# 明明收到了邮件，却提示不在收件人中。
# 这是因为邮件主题、如何显示发件人、收件人等信息并不是通过SMTP协议发给MTA，而是包含在发给MTA的文本中的，所以，我们必须把From、To和Subject添加到MIMEText中，才是一封完整的邮件：
# 再发送一遍邮件，就可以在收件人邮箱中看到正确的标题、发件人和收件人：

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

# 这是手动输入的方式
# from_addr = input('From: ')
# password = input('Password: ')
# to_addr = input('To: ')
# smtp_server = input('SMTP server: ')

from_addr = '420097009@qq.com'
password = 'vcbuejwbgzdqcbdi'
to_addr = input('To: ')
smtp_server = 'smtp.qq.com'

# 这是发送的文本邮件
# msg = MIMEText('hello,胖胖别哭哭,send by Python...', 'plain', 'utf-8')

# 这是发送的HTML邮件 将里面的内容修改成html形式,将plain修改成html
msg = MIMEText('<html><body><h1>Hello</h1>' +
    '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
    '</body></html>', 'html', 'utf-8')

msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()

