# 正常情况下，当我们调用类的方法或属性时，如果不存在，就会报错。比如定义Student类：
class Student(object):
    def __init__(self,name):
        self.name = name

    def __getattr__(self, attr):
        if attr == 'score':
            return 99
        if attr == 'age':
            return lambda :25  # 返回函数也是可以的
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)

s = Student('Michael')
print(s.name)

# 调用name是没有问题的，但是如果要给一个不存在属性score赋值的话就会有问题
# 错误信息会清楚的告诉我们没有score这个属性
# print(s.score)  # AttributeError: 'Student' object has no attribute 'score'

# 要避免运行的错误，就是要加上一个__getattr__()方法，动态返回一个属性
# 当调用不存在的属性时，比如score，Python解释器会试图调用__getattr__(self, 'score')来尝试获得属性，这样，我们就有机会返回score的值
print(s.score)
print(s.age())

# 注意，只有在没有找到属性的情况下，才调用__getattr__，已有的属性，比如name，不会在__getattr__中查找
# 注意在这里如果没有加raise AttributeError的话,如果s.abc属性没有的话返回的是None 但是如果我们要s.abc() 调用函数的话就会报错  TypeError: 'NoneType' object is not callable
# 但是现在如果加了raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr) 这个的话,就可以直接提示 AttributeError: 'Student' object has no attribute 'abc' 就是在没有函数也不会报错
# print(s.abc)
# print(s.abc())

