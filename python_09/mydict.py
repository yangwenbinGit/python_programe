# # 单元测试
# 比如对函数abs()，我们可以编写出以下几个测试用例：
# 输入正数，比如1、1.2、0.99，期待返回值与输入相同；
# 输入负数，比如-1、-1.2、-0.99，期待返回值与输入相反；
# 输入0，期待返回0；
# 输入非数值类型，比如None、[]、{}，期待抛出TypeError

# 函数abs 输入正数进行测试
# print(abs(1))
# print(abs(1.2))
# print(abs(0.99))

# 函数abs 输入负数进行测试
# print(abs(-1))
# print(abs(-1.2))
# print(abs(-0.99))

# 函数abs 输入0进行测试
# print(abs(0))

# 函数非数值类型进行测试 如我们预期的一样 下面的这几种都报错了 None [] {}
# print(abs(None))
# print(abs([]))
# print(abs({}))

# 给字典进行赋值的方法是self[key] = value,取值的方法是self[key]
class Dict(dict):
    # 当函数的参数不确定时，可以使用*args 和**kwargs，*args 没有key值，**kwargs有key值。
    def __init__(self, **kw):
        super().__init__(self,**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

# 报错解决办法：
# TypeError: descriptor '__init__' of 'super' object needs an argument
# 它的意思是说父类dict的__init__方法，需要一个参数
# 然后我看了下他的底层， def __init__(self, seq=None, **kwargs) 于是修改成了 super.__init__(self,**kw)


# 然后出现了下面的错误：
# TypeError: descriptor '__init__' requires a 'super' object but received a 'Dict'
# 它的意思就是 super.__init__(self,**kwargs); 这一行代码出现问题，错误信息是描述符‘__init__’需要一个‘super’对象 但是接收到的是一个Dict
# 解决办法：super().__init__(self,**kw) 这样才可以