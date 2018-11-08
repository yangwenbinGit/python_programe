# metaclass
# 连接起来就是：先定义metaclass，就可以创建类，最后创建实例。

# metaclass是类的模板，所以必须从`type`类型派生：
class ListMataclass(type):
    def __new__(cls, name,bases,attrs):
        attrs['add'] = lambda self,value : self.append(value)
        return type.__new__(cls,name,bases,attrs)

class MyList(list,metaclass=ListMataclass):
    pass

L = MyList()
L.add(1)
print(L)