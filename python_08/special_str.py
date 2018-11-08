# 看到类似__slots__这种形如__xxx__的变量或者函数名就要注意，这些在Python中是有特殊用途的
# __str__
class Student(object):
    def __init__(self,name):
        self.name = name

print(Student('Michael'))

# 打印出来一堆 <__main__.Student object at 0x00000000021EEEF0> 不好看
# 怎么才能打印得好看呢?只需要定义好__str__()方法，返回一个好看的字符串就可以了
# 这是因为直接显示变量调用的不是__str__()，而是__repr__()，两者的区别是__str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的。<__main__.Student object at 0x109afb310>
class Student1(object):
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return 'Student object (name:%s)'%self.name
    __repr__ = __str__
print(Student1('Michael'))  # Student object (name:Michael)
s =Student1('Michael')
print(s)
