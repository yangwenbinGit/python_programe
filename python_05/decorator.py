# 装饰器
import functools
# 现在，假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）
# 本质上，decorator就是一个返回函数的高阶函数。所以，我们要定义一个能打印日志的decorator，可以定义如下
# 观察上面的log，因为它是一个decorator，所以接受一个函数作为参数，并返回一个函数。我们要借助Python的@语法，把decorator置于函数的定义处
# @functools.wraps(func) 因为返回的那个wrapper()函数名字就是'wrapper'，所以，需要把原始函数的__name__等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错。python中Python内置的functools.wraps就是干这个事的
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


# 由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数。
@log('execute')
def now_time():
    print('2018-10-19')

# 直接调用函数
now_time()
# 将函数赋值给变量 这样的话也会调用函数
f = now_time()
# 还有一种写法
f = now_time
f()

# 但是一定要注意下面的错误写法
# f =now_time()
# f()

# 函数对象有一个__name__属性，可以拿到函数的名字： 先执行了log函数  然后最终返回了wrapper这个函数
# print(now_time.__name__)
# print(f.__name__)

# 把@log放到now()函数的定义处，相当于执行了语句
now =log(now_time)

# 和两层嵌套的decorator相比，3层嵌套的效果是这样的
now =log('execute')(now_time)
print(now.__name__)  # wrapper
print(now_time.__name__)  # wrapper

# 由于怕依赖函数签名的代码执行出错  将now_time的_name_等属性复制到wrapper()函数中，通过@functools.wraps(func)方式，这样最后返回的wrapper还是我们的函数本身的名称 now_time







