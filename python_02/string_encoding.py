#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# python的字符串和编码
# 最新的Python 3版本中，字符串是以Unicode编码的
print('包含中文的str')

# 对于单个字符的编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符
print(ord('A'))    # 65
print(ord('z'))    # 122
print(chr(66))     # B
print(chr(25991))  # 文
print('\u4e2d\u6587')  # 中文

# Python对bytes类型的数据用带b前缀的单引号或双引号表示 b''   b'ABC' 表示的是bytes字节类型
# 要注意区分'ABC'和b'ABC'，前者是str，后者虽然内容显示得和前者一样，但是后者是bytes类型,bytes的每个字符都只占用一个字节。
# 以Unicode表示的str通过encode()方法可以编码为指定的bytes
print('ABC'.encode('ascii'))    # 纯英文的str可以用ASCII编码为bytes
print('中文'.encode('utf-8'))   # 含有中文的str可以用UTF-8编码为bytes
# print('中文'.encode('ascii'))   # 含有中文的str无法用ASCII编码，因为中文编码的范围超过了ASCII编码的范围，Python会报错


# 将字节流bytes转换为str 需要用decode()方法
print(b'ABC'.decode('ascii'))    # ABC
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))  # 中文

# 如果bytes中包含无法解码的字节，decode()方法会报错：
# print(b'\xe4\xb8\xad\xff'.decode('utf-8'))

# 如果bytes中只有一小部分无效的字节，可以传入errors='ignore'忽略错误的字节
print(b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore'))

# len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数
print(len(b'ABC'))
print(len(b'\xe4\xb8\xad\xe6\x96\x87'))
print(len('中文'.encode('utf-8'))) # 6   1个中文字符经过UTF-8编码后通常会占用3个字节，而1个英文字符只占用1个字节
print(len('yangwenbin')) # 10

# 在Python中，采用的格式化字符串方式和C语言是一致的，用%实现
# %运算符就是用来格式化字符串的。在字符串内部，%s表示用字符串替换，%d表示用整数替换，有几个%?占位符，后面就跟几个变量或者值，顺序要对应好。如果只有一个%?，括号可以省略
print('Hello,%s' % 'world')
print('Hi, %s, you have $%d.' % ('Michael', 1000000))

# 占位符	替换内容
# %d	整数
# %f	浮点数
# %s	字符串
# %x	十六进制整数
# 格式化整数和浮点数还可以指定是否补0和整数与小数的位数
# %02d 表示有2位 然后第一位用0补齐了  3-01  %.2f表示小数点后2位  3.14
print('%d-%02d' % (3, 1))
print('%.2f' % 3.1415926)

# 如果你不太确定应该用什么，%s永远起作用，它会把任何数据类型转换为字符串：
print('Age: %s. Gender: %s' % (25, True))   # Age: 25. Gender: True

# 有些时候，字符串里面的%是一个普通字符怎么办？这个时候就需要转义，用%%来表示一个%
print('growth rate: %d %%' % 7)   # growth rate: 7 %

# 另一种格式化字符串的方法是使用字符串的format()方法，它会用传入的参数依次替换字符串内的占位符{0}、{1}……
print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))     # Hello, 小明, 成绩提升了 17.1%

