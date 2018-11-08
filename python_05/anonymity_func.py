# 匿名函数
print(list(map(lambda x:x*x,[1,2,3,4,5,6,7,8,9])))
# 通过对比可以看出，匿名函数lambda x: x * x实际上就是
# lambda x: x * x 这个和下面的f(x)是一样的效果
def f(x):
    return x*x

# 关键字lambda表示匿名函数，冒号前面的x表示函数参数
# 匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。
# 用匿名函数有个好处，因为函数没有名字，不必担心函数名冲突。此外，匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数
f =lambda x:x*x
print(f)  # <function <lambda> at 0x00000000021A4730>
print(f(10)) # f() 这样的话就是函数了,10就是把值赋值给x,然后得出结果为100

# 同样，也可以把匿名函数作为返回值返回，比如：
def build(x,y):
    return lambda x,y:x*y

m =build(3,5)
print(m(4,5))
print(m(5,8))