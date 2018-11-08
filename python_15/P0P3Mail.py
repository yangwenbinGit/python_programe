# POP3接收邮件
# 通过POP3下载邮件
# POP3协议本身很简单，以下面的代码为例，我们来获取最新的一封邮件内容：

from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr

import poplib

# 420097009@qq.com  发件人邮箱
# vcbuejwbgzdqcbdi   qq邮箱授权码
# yangwenbin@yjhealth.net   收件人邮箱
# 2495905078@qq.com   小雷
# smtp.qq.com       SMTP server
# pop.qq.com        POP3server


# 输入邮件地址, qq邮箱授权码和POP3服务器地址:pop.qq.com
email = input('Email: ')
password = input('Password: ')
pop3_server = input('POP3 server: ')

def guess_charset(msg):
    charset = msg.get_charset()
    if charset is None:
        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        if pos >= 0:
            charset = content_type[pos + 8:].strip()
    return charset

def decode_str(s):
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value

def print_info(msg, indent=0):
    if indent == 0:
        for header in ['From', 'To', 'Subject']:
            value = msg.get(header, '')
            if value:
                if header=='Subject':
                    value = decode_str(value)
                else:
                    hdr, addr = parseaddr(value)
                    name = decode_str(hdr)
                    value = u'%s <%s>' % (name, addr)
            print('%s%s: %s' % ('  ' * indent, header, value))
    if (msg.is_multipart()):
        parts = msg.get_payload()
        for n, part in enumerate(parts):
            print('%spart %s' % ('  ' * indent, n))
            print('%s--------------------' % ('  ' * indent))
            print_info(part, indent + 1)
    else:
        content_type = msg.get_content_type()
        if content_type=='text/plain' or content_type=='text/html':
            content = msg.get_payload(decode=True)
            charset = guess_charset(msg)
            if charset:
                content = content.decode(charset)
            print('%sText: %s' % ('  ' * indent, content + '...'))
        else:
            print('%sAttachment: %s' % ('  ' * indent, content_type))

## qq邮箱pop3得使用SSL安全连接才可以登录
# 连接到POP3服务器:
server = poplib.POP3_SSL(pop3_server,port=995)
# 可以打开或关闭调试信息:
server.set_debuglevel(1)
# 可选:打印POP3服务器的欢迎文字:
print(server.getwelcome().decode('utf-8'))
# 身份认证:
server.user(email)
server.pass_(password)
# stat()返回邮件数量和占用空间:
print('Messages: %s. Size: %s' % server.stat())
# list()返回所有邮件的编号:
resp, mails, octets = server.list()
# 可以查看返回的列表类似[b'1 82923', b'2 2184', ...]
print(mails)
# 获取最新一封邮件, 注意索引号从1开始:
index = len(mails)
resp, lines, octets = server.retr(index)
# lines存储了邮件的原始文本的每一行,
# 可以获得整个邮件的原始文本:
msg_content = b'\r\n'.join(lines).decode('utf-8')
# 稍后解析出邮件:
msg = Parser().parsestr(msg_content)
print_info(msg)
# 可以根据邮件索引号直接从服务器删除邮件:
# server.dele(index)
# 关闭连接:
server.quit()

# 问题总结
# 1.关于那几个参数，弄了半天没有搞懂,有3个参数,第一个参数是要接收的邮箱地址,第二个参数是qq邮箱授权码,这个在qq邮箱设置里面有，可以修改(别的邮箱的话就去找对应的设置),第三个参数的qq邮箱POP3的服务器地址pop.qq.com。
# 2.第二个如果用的是qq邮箱的话,那么需要变成这一句
# server = poplib.POP3_SSL(pop3_server,port=995)
# 因为qq邮箱pop3得使用SSL安全连接才可以登录,不然就会报错的。
# 3.就是当我们登录的时候密码一定是那个授权码，不是你邮箱的密码，如果你用的是qq邮箱密码，就会报错。
# poplib.error_proto: -ERR Please using authorized code to login.
# 是因为qq出于安全的考虑，使用pop协议的时候，需要使用一个16位的密保来进行操作，就是那个授权码


# 下面就是从邮箱收到的邮件信息
# D:\developeCode\pythonCode\venv\Scripts\python.exe
# D: / developeCode / pythonCode / python_15 / P0P3Mail.py

# Email: 420097009 @ qq.com
# Password: vcbuejwbgzdqcbdi
# POP3 server: pop.qq.com

# +OK
# QQMail
# POP3
# Server
# v1
# .0
# Service
# Ready(QQMail
# v2
# .0)
# *cmd * 'USER 420097009@qq.com'
# *cmd * 'PASS vcbuejwbgzdqcbdi'
# *cmd * 'STAT'
# *stat * [b'+OK', b'25', b'1032533']
# Messages: 25.
# Size: 1032533
# *cmd * 'LIST'
# [b'1 589', b'2 1601', b'3 23214', b'4 5373', b'5 11927', b'6 15922', b'7 4678', b'8 1024', b'9 4844', b'10 1562',
#  b'11 87271', b'12 31386', b'13 1588', b'14 2150', b'15 10583', b'16 1581', b'17 13814', b'18 83417', b'19 12644',
#  b'20 11930', b'21 224491', b'22 1767', b'23 202554', b'24 202596', b'25 74027']
# *cmd * 'RETR 25'
# From: 杨文斌 < yangwenbin @ yjhealth.net >
# To: 420097009 < 420097009 @ qq.com >
# Subject: 转发：新员工到岗通知—王丽娜
# part
# 0
# --------------------
# part
# 0
# --------------------
# Text:
#
# ------------------------------------------------------------------
# 发件人：王丽 < wangli @ yjhealth.net >
# 发送时间：2018
# 年10月22日(星期一)
# 10: 31
# 收件人：all < all @ yjhealth.net >
# 主　题：新员工到岗通知—王丽娜
#
# 新员工到岗通知
#
# 序号
# 姓名
# 入职日期
# 职位
# 所属部门
# 指导人
# 办公地
# 手机号
# 邮箱
#
# 1
# 王丽娜
# 2018 / 10 / 22
# UI设计师
# 技术
# 产品部
# 崔彪
# 北京
# 15701202433
# wanglina @ yjhealth.net
#
# 注：
#
# 1、试用期期间，请做好试用期的跟踪与管理工作；
#
# 2、请做好试用期员工的工作指导及员工关怀，让新员工能尽快融入公司，并与公司共发展；
#
# 3、如有任何问题请及时与人力资源部联系。联系人：lily，电话：010 - 57287437.
#
# 人力资源部
#
# 王丽
# lily
# 人事主管
# 优加健保健康科技（北京）有限公司
# 地址：北京市朝阳区朝外大街22号泛利大厦9层906
#
# ...
# part
# 1
# --------------------
# Text: < div
#
#
# class ="__aliyun_email_body_block" > < div  style="clear:both;" > < span  style="font-family:Microsoft Yahei;font-size:14.0px;color:#000000;" > < br > < / span > < / div > < div  style="clear:both;" > < span  style="font-family:Tahoma,Arial,STHeiti,SimSun;font-size:14.0px;color:#000000;" > ------------------------------------------------------------------ < / span > < / div > < div  style="clear:both;" > < span  style="font-family:Tahoma,Arial,STHeiti,SimSun;font-size:14.0px;color:#000000;" > 发件人：王丽 & lt;wangli @ yjhealth.net & gt; < / span > < / div > < div  style="clear:both;" > < span  style="font-family:Tahoma,Arial,STHeiti,SimSun;font-size:14.0px;color:#000000;" > 发送时间：2018年10月22日(星期一) 10:31 <
#
# / span > < / div > < div
# style = "clear:both;" > < span
# style = "font-family:Tahoma,Arial,STHeiti,SimSun;font-size:14.0px;color:#000000;" > 收件人：all & lt;
# all @ yjhealth.net & gt; < / span > < / div > < div
# style = "clear:both;" > < span
# style = "font-family:Tahoma,Arial,STHeiti,SimSun;font-size:14.0px;color:#000000;" > 主　题：新员工到岗通知—王丽娜 < / span > < / div > < div
# style = "clear:both;" > < span
# style = "font-family:Tahoma,Arial,STHeiti,SimSun;font-size:14.0px;color:#000000;" > < br > < / span > < / div > < style > body
# {line - height: 1.5;}p
# {margin - top: .0px;
# margin - bottom: .0
# px;}body
# {font - size: 11.0pt;
# font - family: 微软雅黑;
# color:
# # 000000;line-height:1.5;}body{font-size:10.5pt;font-family:微软雅黑;color:#000000;line-height:1.5;}</style><div ><br ></div><div ><table  border="0" cellpadding="0" cellspacing="0" class="MsoNormalTable" style="margin-left:7.0px;border-collapse:collapse;width:882.0px;">
# < tbody > < tr >
#   < td
# colspan = "9"
# width = "882"
# style = "border:1.0px solid #c00000;background:#e26b0a;padding:.0px 5.4pt;" >
#         < p
#
#
# class ="MsoNormal" style="text-align:center;margin:.0px .0cm;font-size:14.0px;font-family:Calibri,sans-serif;" > < b > < span  style="font-size:21.0px;font-family:微软雅黑,sans-serif;color:white;" > 新员工到岗通知 < / span > < / b > < b > < / b > < / p >
#
# < / td >
# < / tr >
# < tr >
# < td
# width = "45"
# style = "border-right:1.0px solid #c00000;border-bottom:1.0px solid #c00000;border-left:1.0px solid #c00000;border-image:initial;border-top:none;background:#e26b0a;padding:.0px 5.4pt;" >
# < p
#
#
# class ="MsoNormal" style="text-align:center;margin:.0px .0cm;font-size:14.0px;font-family:Calibri,sans-serif;" > < b > < span  style="font-family:微软雅黑,sans-serif;color:white;" > 序号 < / span > < / b > < / p >
#
# < / td >
# < td
# width = "60"
# style = "border-top:none;border-left:none;border-bottom:1.0px solid #c00000;border-right:1.0px solid #c00000;background:#e26b0a;padding:.0px 5.4pt;" >
# < p
#
#
# class ="MsoNormal" style="text-align:center;margin:.0px .0cm;font-size:14.0px;font-family:Calibri,sans-serif;" > < b > < span  style="font-family:微软雅黑,sans-serif;color:white;" > 姓名 < / span > < / b > < / p >
#
# < / td >
