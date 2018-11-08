# chardet 主要用于字符串的编码和解码 如果我们不知道这个字符串用什么编码的 解码就很困难
# 当我们拿到一个bytes时，就可以对其检测编码,用chardet检测编码，只需要一行代码
import chardet

print(chardet.detect(b'hello world!!'))

# {'encoding': 'ascii', 'confidence': 1.0, 'language': ''}
# 检测出的编码是ascii，注意到还有个confidence字段，表示检测的概率是1.0

data = '离离原上草,一岁一枯荣'.encode('gbk')
print(chardet.detect(data))

# {'encoding': 'GB2312', 'confidence': 0.7407407407407407, 'language': 'Chinese'}
# 检测的编码是GB2312，注意到GBK是GB2312的超集，两者是同一种编码，检测正确的概率是74%，language字段指出的语言是'Chinese'

data = '离离原上草,一岁一枯荣'.encode('utf-8')
print(chardet.detect(data))
# {'encoding': 'utf-8', 'confidence': 0.99, 'language': ''}

data = '最新の主要ニュース'.encode('euc-jp')
print(chardet.detect(data))

# {'encoding': 'EUC-JP', 'confidence': 0.99, 'language': 'Japanese'}
# 用chardet检测编码，使用简单。获取到编码后，再转换为str，就可以方便后续处理
