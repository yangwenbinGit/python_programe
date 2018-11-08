# 可变参数 就是函数中传入的参数的个数是可变的，可以是1个 2个还可以是0个
# 我们以数学题为例子，给定一组数字a，b，c……，请计算a2 + b2 + c2 + ……。
# 要定义出这个函数，我们必须确定输入的参数。由于参数个数不确定，我们首先想到可以把a，b，c……作为一个list或tuple传进来
def calc(numbers):
    sum =0
    for x in numbers:
        sum += x*x
    return sum

# 调用的时候我们组装出一个list或者tuple
print(calc([1,2,3,4,6,8]))
print(calc((1,2,3,4,6,8)))

# 如果利用可变参数，调用函数的方式可以简化成这样
# 定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。在函数内部，参数numbers接收到的是一个tuple，因此，函数代码完全不变。但是，调用该函数时，可以传入任意个参数，包括0个参数
def calc_update(*numbers):
    sum =0
    for x in numbers:
        sum += x*x
    return sum

print(calc_update(1,2,3))
print(calc_update())

# 如果已经有一个list或者tuple，要调用一个可变参数怎么办？可以这样做
num =[1,2,4,8,10]
print(calc_update(num[0],num[1],num[2]))

# 上面的写法太繁琐了，如果要很多的元素我这样写显然是不行的
# Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去
print(calc_update(*num))

# ==============================================================================================
# 关键字参数 关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
# 函数person除了必选参数name和age外，还接受关键字参数kw。在调用该函数时，可以只传入必选参数
print(person('yangwenbin',26))

# 也可以传入任意个数的关键字参数：
print(person('yangwenbin',26,city='beijing'))  # name: yangwenbin age: 26 other: {'city': 'beijing'}
print(person('yangwenbin',26,gender='M',work='IT',address='朝阳门')) # name: yangwenbin age: 26 other: {'gender': 'M', 'work': 'IT', 'address': '朝阳门'}

# 和可变参数类似，也可以先组装出一个dict，然后，把该dict转换为关键字参数传进去,dict就是java的map
extra = {'city': 'Beijing', 'job': 'Engineer'}
print(person('yangwenbin',26,city=extra['city'],job=extra['job']))

# **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra
print(person('jack',24,**extra))  # name: jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}

# ==============================================================================================
# 命名关键字参数
# 仍以person()函数为例，我们希望检查是否有city和job参数
def person_isExist(name,age,**kw):
    if 'city' in kw:
        print('exist city')
    if 'job' in kw:
        print('exist job')
    print(name,age,kw)
print(person_isExist('jack',40,job='engiee',city='beijing',work='IT'))

# 命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数
def person_kw(name, age, *, city, job):
    print(name, age, city, job)
print(person_kw('Jack', 24, city='Beijing', job='Engineer'))  # Jack 24 Beijing Engineer

# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
def person_exist_kw(name, age, *args, city, job):
    print(name, age, args, city, job)
# 命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错：
# print(person_exist_kw('Jack', 24, 'Beijing','Engineer')) #错误写法
print(person_exist_kw('Jack', 24, city='Beijing', job='Engineer'))

# ==============================================================================================
#  参数组合
# 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数
# 参数组合可以一起使用，但是顺序必须是必选参数，默认参数，可变参数，关键字参数，命名关键字参数
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

# 命名关键字参数需要一个特殊分隔符* *后面的参数被视为命名关键字参数
# 命名关键字在赋值的时候要带上对应的key,比如d=99,extra =None
def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

print(f1(1,2))
print(f1(1,2,c=3))
print(f1(1, 2, 3, 'a', 'b','c'))
print(f1(1, 2, 3, 'a', 'b', x=99)) # **kw 必须是key=value的形式  关键字参数
print(f2(1, 2, d=99, ext=None))  # a = 1 b = 2 c = 0 d = 99 kw = {'ext': None}