#!/usr/bin/env python3
# -*- coding :utf-8 -*-

'a test module'

_author_ = 'WenBin Yang'

# 导入模块
import sys

# sys模块有一个argv变量，用list存储了命令行的所有参数。argv至少有一个元素，因为第一个参数永远是该.py文件的名称
# 运行python3 hello.py获得的sys.argv就是['hello.py']；
# 运行python3 hello.py Michael获得的sys.argv就是['hello.py', 'Michael']
def test():
    args =sys.argv
    if len(args) ==1:
        print('Hello World!')
    elif len(args) ==2 :
        print('Hello,%s' %args[1])
    else:
        print('Too many arguments!')

 # 当我们在命令行运行hello模块文件时，Python解释器把一个特殊变量__name__置为__main__，而如果在其他地方导入该hello模块时，if判断将失败，因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码
if __name__ =='__main__':
    test()

# D:\developeCode\pythonCode\python_06>python hello.py
# Hello World!
#
# D:\developeCode\pythonCode\python_06>python hello.py Michael
# Hello,Michael
#
# D:\developeCode\pythonCode\python_06>python hello.py Michael Yang
# Too many arguments!

# 如果启动Python交互环境，再导入hello模块,导入时，没有打印Hello, word!，因为没有执行test()函数。调用hello.test()时，才能打印出Hello, word!：
# D:\developeCode\pythonCode\python_06>python
# Python 3.6.6 (v3.6.6:4cf1f54eb7, Jun 27 2018, 03:37:03) [MSC v.1900 64 bit (AMD6
# 4)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> import hello
# >>> hello.test()
# Hello World!
# >>>

# 正常的函数和变量名是公开的（public），可以被直接引用，比如：abc，x123，PI等；
#
# 类似__xxx__这样的变量是特殊变量，可以被直接引用，但是有特殊用途，比如上面的__author__，__name__就是特殊变量，hello模块定义的文档注释也可以用特殊变量__doc__访问，我们自己的变量一般不要用这种变量名；
#
# 类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用，比如_abc，__abc等
def _private_1(name):
    return 'Hello, %s' % name

def _private_2(name):
    return 'Hi, %s' % name

def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)

# 我们在模块里公开greeting()函数，而把内部逻辑用private函数隐藏起来了，这样，调用greeting()函数不用关心内部的private函数细节，这也是一种非常有用的代码封装和抽象的方法，即：
#
# 外部不需要引用的函数全部定义成private，只有外部需要引用的函数才定义为public。