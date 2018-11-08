from collections import Iterable
from collections import Iterator

# python 迭代器
# 如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）
# 在Python中，迭代是通过for ... in来完成的
d = {'a': 1, 'b': 2, 'c': 3}
# 获取key
for key in d:
    print(key)
# 获取value
for value in d.values():
    print(value)
# 获取key,value的值
for k, v in d.items():
    print(k, v)
# 由于字符串也是可迭代对象，因此，也可以作用于for循环：
for ch in 'ABCD':
    print(ch)

# 如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断
print(isinstance('abc', Iterable))
print(isinstance([1, 2, 3], Iterable))
print(isinstance(123, Iterable))  # False 整数不可迭代

# 最后一个小问题，如果要对list实现类似Java那样的下标循环怎么办？Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身
M = ['A', 'B', 'C', 'D']
for i, value in enumerate(M):
    print(i, value)
    print(M[i])

for x, y in [(1, 2), (2, 4), (3, 9)]:
    print(x, y)

# 请使用迭代查找一个list中最小和最大值，并返回一个tuple：
L = [1, 3, 5, 0, 99, 344, 20]


def findMinAndMax(L):
    if L == None or len(L) == 0:
        return -1
    max = 0
    min = 0
    for x in L:
        if x <= min:
            min = x
        if x > max:
            max = x
    print('最小值是:',min, ',最大值是:', max)
    return 'succcess'


print(findMinAndMax(L))

# 一类是集合数据类型，如list、tuple、dict、set、str等  一类是generator，包括生成器和带yield的generator function
# 直接作用于for循环的对象统称为可迭代对象：Iterable。
# 可以使用isinstance()判断一个对象是否是Iterable对象
print(isinstance([],Iterable))
print(isinstance({},Iterable))
print(isinstance('abc', Iterable))
print(isinstance((x for x in range(10)), Iterable))
print(isinstance(100, Iterable))
print(x for x in range(10))  # 这是一个generator 生成器
print([x for x in range(10)])  # 这是一个list

# 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。
# 可以使用isinstance()判断一个对象是否是Iterator对象：
# 可以使用isinstance()判断一个对象是否是Iterator对象
print(isinstance((x for x in range(10)),Iterator))  # True
print(isinstance([],Iterator))  # False
print(isinstance({},Iterator))  # False
print(isinstance('abc',Iterator))  # False

# 生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator
# 把list、dict、str等Iterable变成Iterator可以使用iter()函数
print(isinstance(iter([]),Iterator))
print(isinstance(iter('abc'),Iterator))

# 你可能会问，为什么list、dict、str等数据类型不是Iterator？
# 这是因为Python的Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，直到没有数据时抛出StopIteration错误。可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，只能不断通过next()函数实现按需计算下一个数据，所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。
# Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。

