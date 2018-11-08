# urllib提供了一系列用于操作URL的功能。主要用于爬虫抓取访问网站
# urllib的request模块可以非常方便地抓取URL内容，也就是发送一个GET请求到指定的页面，然后返回HTTP的响应
# 对豆瓣的一个URLhttps://api.douban.com/v2/book/2129650进行抓取，并返回响应：
from urllib import request,parse

#Get
with request.urlopen('https://www.baidu.com/') as f:
    data = f.read()
    print('Status:',f.status,f.reason)
    for k,v in f.getheaders():
        print('%s:%s' %(k,v))
    print('Data:',data.decode('utf-8'))

# 响应头信息
# Status: 200 OK
# Accept-Ranges:bytes
# Cache-Control:no-cache
# Content-Length:227
# Content-Type:text/html
# Date:Mon, 05 Nov 2018 06:43:57 GMT
# Etag:"5bd7d86c-e3"
# Last-Modified:Tue, 30 Oct 2018 04:05:00 GMT
# P3p:CP=" OTI DSP COR IVA OUR IND COM "
# Pragma:no-cache
# Server:BWS/1.1
# Set-Cookie:BD_NOT_HTTPS=1; path=/; Max-Age=300
# Set-Cookie:BIDUPSID=54A1A568C14596CC939D85F7B97C05CF; expires=Thu, 31-Dec-37 23:55:55 GMT; max-age=2147483647; path=/; domain=.baidu.com
# Set-Cookie:PSTM=1541400237; expires=Thu, 31-Dec-37 23:55:55 GMT; max-age=2147483647; path=/; domain=.baidu.com
# Strict-Transport-Security:max-age=0
# X-Ua-Compatible:IE=Edge,chrome=1
# Connection:close

# 响应的json数据
# Data: <html>
# <head>
# 	<script>
# 		location.replace(location.href.replace("https://","http://"));
# 	</script>
# </head>
# <body>
# 	<noscript><meta http-equiv="refresh" content="0;url=http://www.baidu.com/"></noscript>
# </body>
# </html>

# 如果我们要想模拟浏览器发送GET请求，就需要使用Request对象，通过往Request对象添加HTTP头，我们就可以把请求伪装成浏览器  模拟iPhone 6去请求豆瓣首页
req = request.Request('http://www.douban.com/')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
with request.urlopen(req) as f:
    print('Status:',f.status,f.reason)
    for k,v in f.getheaders():
        print('%s:%s'%(k,v))
    print('Data:',f.read().decode('utf-8'))


# Post
# 如果要以POST发送一个请求，只需要把参数data以bytes形式传入。
print('Login to weibo.cn...')
email = input('Email: ')
passwd = input('Password: ')
login_data = parse.urlencode([
    ('username', email),
    ('password', passwd),
    ('entry', 'mweibo'),
    ('client_id', ''),
    ('savestate', '1'),
    ('ec', ''),
    ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
])

req = request.Request('https://passport.weibo.cn/sso/login')
req.add_header('Origin', 'https://passport.weibo.cn')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

with request.urlopen(req, data=login_data.encode('utf-8')) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))

# Handler
# 如果还需要更复杂的控制，比如通过一个Proxy去访问网站，我们需要利用ProxyHandler来处理，示例代码如下：
proxy_handler =request.ProxyHandler({'http': 'http://www.example.com:3128/'})
proxy_auth_handler = request.ProxyBasicAuthHandler()
proxy_auth_handler.add_password('realm', 'host', 'username', 'password')
opener = request.build_opener(proxy_handler, proxy_auth_handler)
with opener.open('http://www.example.com/login.html') as f:
    print('Data:',f.read().decode('utf-8'))