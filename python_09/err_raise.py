# 抛出错误
# 如果要抛出错误，首先根据需要，可以定义一个错误的class，选择好继承关系，然后，用raise语句抛出一个错误的实例
class FooError(ValueError):
    pass


def foo(s):
    n = int(s)
    if n == 0:
        raise FooError('invalid value: %s' % s)
    return 20 / n

# 执行，可以跟踪到我们自己定义的错误
# __main__.FooError: invalid value: 0
# foo('0')


# 我们来看另一种错误处理的方式
def foo(s):
    n = int(s)
    if n==0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n

def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise

# ValueError: invalid value: 0
# 上面的结果我们可以得出  当执行foo('0')的时候然后执行上面的内容，执行了 raise ValueError('invalid value: %s' % s)这样就处理了错误,后面的Exception就不会执行了。
bar()
