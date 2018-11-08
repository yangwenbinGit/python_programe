#  python支持的数据类型有 int  float  double  boolean string 对数据类型的练习
# int 类型  <class 'int'>
print(100)
print(type(100))
print(type(-10))
print(type(0))
print(type(0xff00))
print(type(0xa5b4c3d2))
print('-----------------------------------------------------\n')

# <class 'float'>
print(1.02)
print(type(1.02))
print(type(-9.01))
print(type(1.2e-5))
print(type(12.3e8))
print('-----------------------------------------------------\n')

# True or False
print(True)
print('a'>'b')
print(False)
print(3>5)
print(3>2)
print(True and True)
print(True and False)
print(False and False)
print(3>2 and 1>3)
print(True or True)
print(True or False)
print(False or False)
print(not True)
print(not False)
print(not 1>2)

a =30;
if a>=18:
    print("adult")
else:
    print("teenager")

print('-----------------------------------------------------\n')

# <class 'str'>
print('abc')
print('xyz')
print(type('abc'))
print('I\'m "OK"!')
print('I\'m Ok')
print('I\'m learning python \nauthor yangwenbin')
print('\\\n\\') # 在python中\\ 双斜杠会被转义成单斜杠\
print('D:\\developeCode\\pythonCode')
print('\\\t\\') # \t 表示的是tab占位符
print(r'\\\t\\') # Python还允许用r'' 表示''内部的字符串默认不转义  输出为 \\\t\\
print('''line1
line2
line3''')   # 如果字符串内部有很多换行，用\n写在一行里不好阅读，为了简化，Python允许用''' '''的格式表示多行内容
print('''hello,\n
world ''')
print('-----------------------------------------------------\n')

# 变量的定义 在python中对于变量的定义和java中还是有区别的
# 变量在程序中就是用一个变量名表示了，变量名必须是大小写英文、数字和_的组合，且不能用数字开头 在python中不用写类型
a =10
t_007 ='T007'
b =1.23
Answer = True
print(a)
print(t_007)
print(b)
print(Answer)

a +=10;
print(a)
# 在Python中，有两种除法，一种除法是/ 他们相除的结果哪怕是整数相除可以除尽 结果还是浮点数，  还有一种除法是//，称为地板除，两个整数的除法仍然是整数
print(10/3)
print(9/3)
print(9//3)
print('-----------------------------------------------------\n')


# 练习
n = 123    # 123
f = 456.789   # 456.789
s1 = 'Hello, world'   # Hello, world
s2 = 'Hello, \'Adam\''   # Hello,'Adam'   \' 这种是转义  输出的时候也会输出' 来
s3 = r'Hello, "Bart"'   # r'' 这种写法就是他里面的原样输出  Hello, "Bart"
s4 = r'''Hello,   
Lisa!'''
# Hello,
# Lisa!
print(n)
print(f)
print(s1)
print(s2)
print(s3)
print(s4)


