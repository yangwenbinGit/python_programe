# 记录错误
# 如果不捕获错误，自然可以让Python解释器来打印出错误堆栈，但程序也被结束了。既然我们能捕获错误，就可以把错误堆栈打印出来，然后分析错误原因，同时，让程序继续执行下去。
# Python内置的logging模块可以非常容易地记录错误信息
import logging

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e :
        logging.exception(e)

main()
print('END')
print('Yes Execute END!!!')

# 同样是出错，但程序打印完错误信息后会继续执行，并正常退出：
# END
# Traceback (most recent call last):
#   File "D:/developeCode/pythonCode/python_09/err_logging.py", line 14, in main
#     bar('0')
#   File "D:/developeCode/pythonCode/python_09/err_logging.py", line 10, in bar
#     return foo(s) * 2
#   File "D:/developeCode/pythonCode/python_09/err_logging.py", line 7, in foo
#     return 10 / int(s)
# ZeroDivisionError: division by zero
# END
# Yes Execute END!!!  这里就是说如果使用了logging的话，可以在出现错误后，后面的信息还会继续执行打印，直到程序执行完成




