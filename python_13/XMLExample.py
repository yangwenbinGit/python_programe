# 操作XML的方式DOM或者SAX
# 操作XML有两种方法：DOM和SAX。DOM会把整个XML读入内存，解析为树，因此占用内存大，解析慢，优点是可以任意遍历树的节点。SAX是流模式，边读边解析，占用内存小，解析快，缺点是我们需要自己处理事件。
# 在Python中使用SAX解析XML非常简洁，通常我们关心的事件是start_element，end_element和char_data，准备好这3个函数，然后就可以解析xml了
# 举个例子，当SAX解析器读到一个节点时：
#
# <a href="/">python</a>
# 会产生3个事件：
#
# start_element事件，在读取<a href="/">时；
#
# char_data事件，在读取python时；
#
# end_element事件，在读取</a>时

from xml.parsers.expat import ParserCreate
from urllib import request
import json

class DefaultSaxHandler(object):
    def start_element(self, name, attrs):
        print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))

    def end_element(self, name):
        print('sax:end_element: %s' % name)

    def char_data(self, text):
        print('sax:char_data: %s' % text)

xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''

handler = DefaultSaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml)

# 需要注意的是读取一大段字符串时，CharacterDataHandler可能被多次调用，所以需要自己保存起来，在EndElementHandler里面再合并。
#
# 除了解析XML外，如何生成XML呢？99%的情况下需要生成的XML结构都是非常简单的，因此，最简单也是最有效的生成XML的方法是拼接字符串：
#
def getXml():
    L = []
    L.append(r'<?xml version="1.0"?>')
    L.append(r'<root>')
    L.append('some & data')
    L.append(r'</root>')
    return ''.join(L)
print(100*'==')
print(getXml())
# 如果要生成复杂的XML呢？建议你不要用XML，改成JSON。

# 请利用SAX编写程序解析Yahoo的XML格式的天气预报，获取天气预报：
result ={}
result['forecast'] = []

class parseXml(object):

    def start_element(self, name, attrs):
            print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))
            if 'city' in str(attrs):
                print(attrs)
                value =str(attrs).split(',')[1]
                print(value)
                result['city'] =value.split(':')[1].strip(' ').strip("'")
            if 'date' and 'high' and 'low' in str(attrs):
                print(attrs)
                information = {}
                information['date'] = attrs['date']
                information['high'] = attrs['high']
                information['low'] = attrs['low']
                result['forecast'].append(information)


    def end_element(self, name):
            print('sax:end_element: %s' % name)


    def char_data(self, text):
            print('sax:char_data: %s' % text)



URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=xml'
with request.urlopen(URL,timeout=5) as f:
    data = f.read()
handler = parseXml()
parser = ParserCreate()
parser.StartElementHandler =handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(data.decode('utf-8'))
print(100 * '===')
print(result)
assert result['city'] == 'Beijing'   # 断言如果存在的话就不会报错

# 这是结果
# {'forecast': [{'date': '05 Nov 2018', 'high': '52', 'low': '33'}, {'date': '06 Nov 2018', 'high': '54', 'low': '34'}, {'date': '07 Nov 2018', 'high': '55', 'low': '31'}, {'date': '08 Nov 2018', 'high': '56', 'low': '36'}, {'date': '09 Nov 2018', 'high': '59', 'low': '35'}, {'date': '10 Nov 2018', 'high': '56', 'low': '31'}, {'date': '11 Nov 2018', 'high': '55', 'low': '34'}, {'date': '12 Nov 2018', 'high': '56', 'low': '36'}, {'date': '13 Nov 2018', 'high': '53', 'low': '38'}, {'date': '14 Nov 2018', 'high': '53', 'low': '38'}], 'city': 'Beijing'}
