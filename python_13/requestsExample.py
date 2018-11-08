# requests
import requests
r =requests.get('https://www.douban.com/')  # 访问豆瓣首页
print(r.status_code)   # 返回结果码 200
print(r.text)   # 打印页面的所有信息

# 在请求的时候传入一个dict作为params参数
r = requests.get('https://www.douban.com/search', params={'q': 'python', 'cat': '1001'})
print(r.url)   # https://www.douban.com/search?q=python&cat=1001

# requests自动检测编码,可以用encoding属性查看
print(r.encoding)   # utf-8
# 无论响应是文本还是二进制内容，我们都可以用content属性获得bytes对象：
print(r.content)

# 对于特定的响应 例如json可以直接获取
r = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
print(r.json())

# {'query': {'count': 1, 'created': '2017-11-17T07:14:12Z', ...

# 需要传入HTTP Header时，我们传入一个dict作为headers参数
r = requests.get('https://www.douban.com/',
                 headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
print(r.text)

# <!DOCTYPE html>
# <html itemscope itemtype="http://schema.org/WebPage">
#     <head>
#         <meta charset="UTF-8">
#         <title>豆瓣(手机版)</title>
#         <meta name="google-site-verification" content="ok0wCgT20tBBgo9_zat2iAcimtN4Ftf5ccsh092Xeyw" />
#         <meta name="viewport" content="width=device-width, height=device-height, user-scalable=no, initial-scale=1.0, minimum-scale=1.0, maximum-scale=1.0">
#         <meta name="format-detection" content="telephone=no">

r = requests.post('https://accounts.douban.com/login',
                  data={'form_email': 'abc@example.com', 'form_password': '123456'})
print(r.text)

# requests默认使用application/x-www-form-urlencoded对POST数据编码。如果要传递JSON数据，可以直接传入json参数
# url = 'https://accounts.douban.com/login'
# params = {'key': 'value'}
# r = requests.post(url, json=params) # 内部自动序列化为JSON
print(r.headers)
print(r.cookies)


# 传递cookie
# cs = {'token': '12345', 'status': 'working'}
# r = requests.get(url, cookies=cs)