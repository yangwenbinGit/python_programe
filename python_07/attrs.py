# 获取对象的所有属性和方法 使用dir()
# 如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：
print(dir('ABC'))

# 类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度。在Python中，如果你调用len()函数试图获取一个对象的长度，实际上，在len()函数内部，它自动去调用该对象的__len__()方法，所以，下面的代码是等价的
# 这两种方式其实是一样的，只不过len()是做了封装,底层调用的也是对象.__len__()这样获取长度的
print(len('ABC'))
print('ABC'.__len__())

# 剩下的都是普通属性或方法，比如lower()返回小写的字符串
print('ABC'.lower())

# 仅仅把属性和方法列出来是不够的，配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态
class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x

obj = MyObject()
print(obj.power())

# 测试该对象的属性
print(hasattr(obj,'x'))  # 有属性x吗？
print(obj.x)
print(hasattr(obj,'y'))
setattr(obj,'y',20)
print(hasattr(obj,'y'))
getattr(obj,'y')  # 获取对象的属性y
print(obj.y)  # 获取属性y
print(getattr(obj,'z',404))  # 获取属性z 不存在的话就返回404

# 也可以获得对象的方法：
print(hasattr(obj,'power'))
print(getattr(obj,'power'))
fn =getattr(obj,'power')
print(fn())

