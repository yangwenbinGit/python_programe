from functools import reduce


# Python内建了map()和reduce()函数
# 我们先看map。map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
# 比如我们有一个函数f(x)=x2，要把这个函数作用在一个list上
def f(x):
    return x * x


L = [1, 2, 3, 4, 5, 6, 7, 8, 9]
r = map(f, L)
print(list(r))

# map()传入的第一个参数是f，即函数对象本身。由于结果r是一个Iterator，Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list
# 这个就是将f这个函数作用到L 这个列表上，返回Iterator对象  然后在由list()函数计算出整个序列

# 可能会想，不需要map()函数，写一个循环，也可以计算出结果
M = []
for x in L:
    M.append(f(x))
print(M)

# map()作为高阶函数，事实上它把运算规则抽象了 还可以计算任意复杂的函数，比如，把这个list所有数字转为字符串
print(list(map(str, L)))


# reduce
# 比方说对一个序列求和，就可以用reduce实现
def add(x, y):
    return x + y


result = reduce(add, L)
print(result)  # 45
print(sum(L))  # 这样直接求和即可


# 但是如果要把序列[1, 3, 5, 7, 9]变换成整数13579，reduce就可以派上用场
def fn(x, y):
    return x * 10 + y


print(reduce(fn, L))  # 123456789

# 其实这个reduce是这样的，reduce(add,L)以这个为例，我们的L是1-9的数字，我们的函数是add，但是让我们迷惑的是x,y的值是多少？
# 先是1,2 然后得到的结果是3 然后3在作为x,下一个元素3作为y 然后继续往下得出6 6作为x 4作为y 直到计算出结果。
# 对于fn 函数也是一样的，先x,y分别是1和2 得到12 然后下一次x为12 y为3 得出123 依次往下执行

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def char2num(s):
    return DIGITS[s]


def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


print(reduce(fn, map(char2num, '13579')))


# map(f,L) 将函数作用于列表,根据函数返回结果 返回的是Iterator list(Iterator)可以返回的是list reduce(f,L) 将函数作用于列表，这个和map不同的是将上一个计算的结果用于下一个参数
# 然后和list的参数继续进行运算 最终得出结果,他返回的就是一个结果 filter(f,
# L) filter也是有两个参数，第一个是函数，第二个是要作用的list，他会作用于list的每一个元素，根据返回的true或者是false决定元素的去留  如果return n%2==0 这个是成立的，返回true
# 那么就删除这个元素n 他是根据true和false判断的，他返回的结果也是一个Iterator，惰性加载 需要用list进行转换
