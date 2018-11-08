# 函数的参数
# 位置参数,我们先写一个计算x^2的函数：
def power(x):
    return x * x

print(power(5))
print(power(15))

# 现在，如果我们要计算x3怎么办？可以再定义一个power3函数，但是如果要计算x4、x5……怎么办？我们不可能定义无限多个函数
# 你也许想到了，可以把power(x)修改为power(x, n)，用来计算xn，说干就干
def power_n(x,n):
    s =1
    while n>0:
        s *= x
        n =n-1
    return s

print(power_n(5,3))
print(power_n(8,10))

# 我们写个一年级小学生注册的函数，需要传入name和gender两个参数
def enroll(name,gender):
    print('name:',name)
    print('gender:',gender)
# 这样，调用enroll()函数只需要传入两个参数：
print(enroll('yangwenbin','F'))
print('---------------------------------------------------------------')
# 如果要继续传入年龄、城市等信息怎么办？这样会使得调用函数的复杂度大大增加。
# 我们可以把年龄和城市设为默认参数
def enroll_update(name,gender,age=12,city='beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)
# 这样，大多数学生注册时不需要提供年龄和城市，只提供必须的两个参数
print(enroll_update('yangwenbin','F'))

# 只有与默认参数不符的学生才需要提供额外的信息
print('---------------------------------------------------------------')
print(enroll_update('Bob','M',7))
print('---------------------------------------------------------------')
print(enroll_update('Adam','F',city='ShangHai'))

# 定义默认参数要牢记一点：默认参数必须指向不变对象
# Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了
def add_end(L=[]):
    L.append('END')
    return L
print(add_end(['x','y','z']))
print(add_end())
print(add_end())
print(add_end())   # ['END', 'END', 'END']

# 要修改上面的例子，我们可以用None这个不变对象来实现：
# 现在，无论调用多少次，都不会有问题   ['END']
def add_end_update(L=None):
    if L is None:
        L=[]
    L.append('END')
    return L
print(add_end_update())
print(add_end_update())
print(add_end_update())





