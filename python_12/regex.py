# 正则表达式
# 正则表达式是一种用来匹配字符串的强有力的武器
# 所以我们判断一个字符串是否是合法的Email的方法是：
#     1.创建一个匹配Email的正则表达式；
#     2.用该正则表达式去匹配用户的输入来判断是否合法。

# \d可以用来匹配一个数字，\w可以用来匹配一个字母或数字 .可以匹配任意的字符
# 要匹配变长的字符,在正则表达式中,用*表示任意个字符,用+表示至少一个字符，用?表示0或者1个字符，用{n}表示n个字符，用{n,m}表示n-m个字符
# \s可以匹配一个空格(也包括Tab等空白符) \s+至少有一个空格,例如匹配' ',' '等
s = '\d{3}\s+\d{3-8}'

# 这个正则匹配从左到右我们解读一下：
# \d{3} 表示匹配3个数字 例如'010'
# \s可以匹配一个空格(也包括Tab等空白符),所以\s+表示至少有一个空格.例如' ',' '
# \d{3,8} 表示3-8个数字  例如 12345678
# 综合上面正则表达式可以匹配任意个空格隔开的带区号的电话号码
# 如果要匹配'010-123456'这样的号码呢？由于'-'是特殊的字符，在正则表达式中要用'\'去转义,所以上面的正则应该是'\d{3}\-\d{3,8}'

# 进阶  如果要做更精准的匹配，可以用[]表示范围
# [0-9a-zA-Z\_] 可以匹配一个数字，字母,或者下划线
# [0-9a-zA-Z\_]+ 可以匹配至少由一个数字,字母,或者下划线组成的字符串,比如'a100'，'0_Z'，'Py3000'等等
# [a-zA-Z\_][0-9a-zA-Z\_]* 可以匹配由字母或下划线开头，后接任意个由一个数字、字母或者下划线组成的字符串，也就是Python合法的变量
# [a-zA-Z\_][0-9a-zA-Z\_]{0, 19}  更加精准的限制了整个的字符串的长度是1-20个字符 (前面1个字符+后面最多19个字符)
# A|B 可以匹配A或B (P|p)ython可以匹配Python或者python
# ^表示行的开头,^\d 表示必须以数字开头
# $表示行的结束,\d$ 表示必须以数字结尾

# re模块
# 由于Python的字符串本身也用\转义，所以要特别注意
# s = 'ABC\\-001'  # python的字符串   对应的正则表达式字符串不变 'ABC|-001'
# 我们强烈建议使用Python的r前缀，就不用考虑转义的问题
import re
print(re.match(r'\d{3}\-\d{3,8}$','010-12345'))   # <_sre.SRE_Match object; span=(0, 9), match='010-12345'>
print(re.match(r'^\d{3}\-\d{3,8}$','010 12345'))  # None 他这个是匹配的是带-的电话，例如010-789345

# match()方法判断是否匹配，如果匹配成功，返回一个Match对象，否则返回None。常见的判断方法就是：
test = '用户输入的字符串'
if re.match(r'\w+',test):
    print('ok')
else:
    print('failed')

# 切分字符串
# 用正则表达式切分字符串比用固定的字符更灵活，请看正常的切分代码
print('a b   c'.split(' '))
# 无法识别连续的空格，用正则表达式试试：
print(re.split(r'\s+','a, b   c'))
# 无论多少空格都可以正常分割,加入,试试
# 如果用户输入了一组标签，下次记得用正则表达式来把不规范的输入转化成正确的数组
print(re.split(r'[\s\,]+','a,b c   d'))
print(re.split(r'[\s\,\;]+','a,b;;c  f;,   d'))

# 分组
# 除了简单地判断是否匹配之外，正则表达式还有提取子串的强大功能。
m = re.match(r'^(\d{3})\-(\d{3,8})$', '010-123456')
print(m)
print(m.group())
print(m.group(1))
print(m.group(2))

t = '19:05:30'
m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
print(m.group())

# 贪婪匹配
# 由于\d+采用贪婪匹配，直接把后面的0全部匹配了，结果0*只能匹配空字符串了。
print(re.match(r'^(\d+)(0*)$','1023000').group())
# 必须让\d+采用非贪婪匹配（也就是尽可能少匹配），才能把后面的0匹配出来，加个?就可以让\d+采用非贪婪匹配
print(re.match(r'^(\d+?)(0*)\w+$','102300xx').group())


L = ['小明', 'xiaohong', '12', 'adf12', '14']
for i in range(len(L)):
    if re.findall(r'^[^\d]\w+', L[i]):
        print(re.findall(r'^\w+$', L[i])[0])


# 编译
# 当我们在Python中使用正则表达式时，re模块内部会干两件事情：
#
# 编译正则表达式，如果正则表达式的字符串本身不合法，会报错；
#
# 用编译后的正则表达式去匹配字符串。
#
# 如果一个正则表达式要重复使用几千次，出于效率的考虑，我们可以预编译该正则表达式，接下来重复使用时就不需要编译这个步骤了，直接匹配：

# 编译:
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
# 使用：
print(re_telephone.match('010-12345').groups())
print(re_telephone.match('010-8086').groups())
# 编译后生成Regular Expression对象，由于该对象自己包含了正则表达式，所以调用对应的方法时不用给出正则字符串

# 写一个邮箱的验证
# someone@gmail.com
# bill.gates@microsoft.com
print(re.match(r'[a-z\.\-\_]+\@[a-z]+\.[a-z]+\w$','bill.gates@microsoft.com'))