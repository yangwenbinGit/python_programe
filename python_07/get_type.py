import types
# 获取对象信息
# 当我们拿到一个对象的引用时，如何知道这个对象是什么类型、有哪些方法呢
# 首先，我们来判断对象类型，使用type()函数
# 基本类型都可以用type()判断

print(type(123))
print(type('WenBin Yang'))
print(type(None))

# 如果一个变量指向函数或者类，也可以用type()判断：
print(type(abs))
class Animal(object):
    def run(self):
        print('Animal is running...')

    def eat(self):
        print('Animal is eating...')

animal =Animal()
print(type(animal))

# 获取到类型 然后进行比较两个变量的type类型是否相同：
print(type(123) == type(456))  #True
print(type(123) == int)  #True
print(type('abc') == type('123'))  #True
print(type('abc') == str)  #True
print(type('abc') == type(123))  #False

# 判断基本数据类型可以直接写int，str等，但如果要判断一个对象是否是函数怎么办？可以使用types模块中定义的常量
def fn():
    pass
print(type(fn) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x:x) == types.LambdaType)  # lambda x:x 他就是def f(x): return x
print(type((x for x in range(10))) == types.GeneratorType)
print(x for x in range(10))  # <generator object <genexpr> at 0x00000000029CFF68>  这就是生成器类型
g = (x for x in range(10))
for n in g:
    print(n)

# 使用isinstance()
# 能用type()判断的基本类型也可以用isinstance()判断,我们要判断class的类型，可以使用isinstance()函数：
class Animal(object):
    def run(self):
        print('Animal is running...')

    def eat(self):
        print('Animal is eating...')

class Dog(Animal):
    def shout(self):
        print('Dog is shouting...')

    def run(self):
        print('Dog is running...')

class Cat(Animal):
    def shout(self):
        print('Cat is shouting...')

    def run(self):
        print('Cat is running...')

class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')

a = Animal()
d = Dog()
c = Cat()
t = Tortoise()
print(isinstance(d,Animal))
print(isinstance(c,Animal))
print(isinstance(t,Animal))

# 普通的类型也可以用isinstance这个方法进行比较
print('==========================================================')
print(isinstance('a',str))
print(isinstance(123,int))
print(isinstance(b'a',bytes))

# 并且还可以判断一个变量是否是某些类型中的一种，比如下面的代码就可以判断是否是list或者tuple
print(isinstance([1,2,3],(list,tuple)))
print(isinstance((1,2,3),(list,tuple)))
