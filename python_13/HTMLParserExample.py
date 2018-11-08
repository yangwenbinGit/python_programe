# HTMLParser
# 如何实现HTML的解析,python提供了HTMLParser来非常方便的解析HTML
from html.parser import HTMLParser
from  html.entities import name2codepoint
from urllib import request

class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print('<%s>' % tag)

    def handle_endtag(self, tag):
        print('</%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('<%s/>' % tag)

    def handle_data(self, data):
        print(data)

    def handle_comment(self, data):
        print('<!--', data, '-->')

    def handle_entityref(self, name):
        print('&%s;' % name)

    def handle_charref(self, name):
        print('&#%s;' % name)

# parser = MyHTMLParser()
# parser.feed('''<html>
# <head></head>
# <body>
# <!-- test html parser -->
#     <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
# </body></html>''')


# feed()方法可以多次调用，也就是不一定一次把整个HTML字符串都塞进去，可以一部分一部分塞进去。
#
# 特殊字符有两种，一种是英文表示的&nbsp;，一种是数字表示的&#1234;，这两种字符都可以通过Parser解析出来。
#
# 利用HTMLParser，可以把网页中的文本、图像等解析出来。

# 找一个网页，例如https://www.python.org/events/python-events/，用浏览器查看源码并复制，然后尝试解析一下HTML，输出Python官网发布的会议时间、名称和地点。
# 我们现在要抓取python官网的分布的名称,时间和地点
from html.parser import HTMLParser
from html.entities import name2codepoint
from urllib import request
import re

class MyHTMLParserPython(HTMLParser):
    def __init__(self):
        super(MyHTMLParserPython,self).__init__()
        self.__parsedata='' #设置一个空状态

    def handle_starttag(self, tag, attrs):
        if ('class','event-title') in attrs:
            self.__parsedata='name' #设置爬取名称状态
        if tag=='time':
            self.__parsedata='time'
        if ('class','say-no-more') in attrs:
            self.__parsedata='year'
        if ('class','event-location') in attrs:
            self.__parsedata='location'

    def handle_endtag(self,tag):
        if tag == 'h3' or tag == 'span':
            self.__parsedata=''

    def handle_data(self, data):
        if  self.__parsedata=='name':
            print('会议名称:%s'%data)

        if  self.__parsedata=='time':
            print('会议时间:%s'%data)

        if  self.__parsedata=='year':
            if re.match(r'\s\d{4}',data):
                #因为后面还有两组 say-no-more 后面的data却不是年份信息,所以用正则检测一下
                print('会议年份:%s'%data.strip())

        if  self.__parsedata=='location':
            print('会议地点:%s'%data)
            print('----------------------------------')


parser = MyHTMLParserPython()
URL = 'https://www.python.org/events/python-events/'

with request.urlopen(URL, timeout=15) as f:  # 打开网页并取到数据
    data = f.read()
    parser.feed(data.decode('utf-8'))



