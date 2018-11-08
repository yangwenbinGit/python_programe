class Hello(object):
    def hello(self,name='world'):
        self.name = name
        print('Hello,%s!!'%self.name)

h =Hello()
h.hello()
print(type(Hello))  # <class 'type'> Hello是一个class，它的类型就是type
print(type(h))      # <class '__main__.Hello'> 而h是一个实例，它的类型就是class Hello

# type()函数既可以返回一个对象的类型，又可以创建出新的类型，比如，我们可以通过type()函数创建出Hello类，而无需通过class Hello(object)...的定义
def fn(self,name='world'):
    print('Hello,%s!!'%name)
Hello1 =type('Hello1',(object,),dict(hello=fn))  # # 创建Hello class

h1 =Hello1()
h1.hello()
print(Hello1.__name__)  # 打印出类名  Hello1


# 要创建一个class对象，type()函数依次传入3个参数：
#
# class的名称；
# 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
# class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。

