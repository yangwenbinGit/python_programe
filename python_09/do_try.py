# 错误处理

def foo():
    r = some_function(-20)
    if r == -1:
        return (-1)
    return r

def some_function(age):
    if age<0 or age >130:
        return -1
    else:
        return age

def bar():
    r = foo()
    if r == -1:
        print("Error")
    else:
        print(r)

# 调用函数
# 由于这样的函数一旦出错要一级一级的上报,直到某个函数可以处理改错误，这样不是很方便
# 所以高级语言通常都内置了一套 try...except...finally...的错误机制
print(bar())

# 让我们用一个例子来看看try的机制：
# 当我们认为某些代码可能会出错时，就可以用try来运行这段代码，如果执行出错，则后续代码不会继续执行，而是直接跳转至错误处理代码，即except语句块，执行完except后，如果有finally语句块，则执行finally语句块，至此，执行完毕
try:
    print('try...')
    r = 10 / 0
    print('result:',r)
except ZeroDivisionError as e:
    print('except:',e)
finally:
    print('finally...')
print('END')

# 打印结果
# try...
# except: division by zero
# finally...
# END

# 如果将0修改为2 再次执行
print('==================================================================================')
try:
    print('try...')
    r = 10 / 2
    print('result:',r)
except ZeroDivisionError as e:
    print('except:',e)
finally:
    print('finally...')
print('END')

# try...
# result: 5.0
# finally...
# END

# 你还可以猜测，错误应该有很多种类，如果发生了不同类型的错误，应该由不同的except语句块处理。没错，可以有多个except来捕获不同类型的错误
# int()函数可能会抛出ValueError，所以我们用一个except捕获ValueError，用另一个except捕获ZeroDivisionError
# 可以在except语句块后面加一个else，当没有错误发生时，会自动执行else语句
print('==================================================================================')
try:
    print('try...')
    r = 10 /int('a')
    print('result:',r)
except ValueError as e:
    print('ValueError:',e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:',e)
else:
    print('no Error...')
finally:
    print('finally...')
print('END')


# 像这种写法 第二个except永远也捕获不到UnicodeError，因为UnicodeError是ValueError的子类，如果有，也被第一个except给捕获了。
try:
    foo()
except ValueError as e:
    print('ValueError')
except UnicodeError as e:
    print('UnicodeError')


# 使用try...except捕获错误还有一个巨大的好处，就是可以跨越多层调用，比如函数main()调用bar()，bar()调用foo()，结果foo()出错了，这时，只要main()捕获到了，就可以处理
print('==================================================================================')
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s)

def main():
    try:
        bar('0')
    except Exception as e:
        print('Error:', e)
    finally:
        print('finally...')

main()

# 打印结果
# Error: division by zero
# finally...





