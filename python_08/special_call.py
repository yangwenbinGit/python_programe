# __call__
# 一个对象实例可以有自己的属性和方法，当我们调用实例方法时，我们用instance.method()来调用。能不能直接在实例本身上调用呢？在Python中，答案是肯定的。
# 任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用。请看示例：
class Student(object):
    def __init__(self,name):
        self.name = name

    def __call__(self, *args, **kwargs):
        print('My name is %s.' %self.name)

# 调用方式如下：
s =Student('Michael')
print(s())   # s表示的是类的实例，如果直接打印s 就会打印出一串字符串(类的名称和内存地址)  如果s() 表示的是一个实例，打印实例的话，由于__call__这个方法 就是在调用实例的时候直接走他里面的方法

# __call__()还可以定义参数。对实例进行直接调用就好比对一个函数进行调用一样，所以你完全可以把对象看成函数，把函数看成对象，因为这两者之间本来就没啥根本的区别
# 如果你把对象看成函数，那么函数本身其实也可以在运行期动态创建出来，因为类的实例都是运行期创建出来的，这么一来，我们就模糊了对象和函数的界限
# 那么，怎么判断一个变量是对象还是函数呢？其实，更多的时候，我们需要判断一个对象是否能被调用，能被调用的对象就是一个Callable对象，比如函数和我们上面定义的带有__call__()的类实例

# 通过callable()函数，我们就可以判断一个对象是否是“可调用”对象。
print(callable(Student('Yang')))  # True
print(callable(max))  # True
print(callable([1,2,3]))  # False
print(callable(None))  # False
print(callable('str')) # False