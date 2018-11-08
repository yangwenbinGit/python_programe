# 生成器
# 如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator
# 要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator
L =[x*x for x in range(11)]
print(L)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
g =(x*x for x in range(11))
print(g)  # <generator object <genexpr> at 0x000000000296FF68>

# 创建L和g的区别仅在于最外层的[]和()，L是一个list，而g是一个generator。
# 如果要一个一个打印出来，可以通过next()函数获得generator的下一个返回值：
print(next(g))
print(next(g))
print(next(g))

# 我们讲过，generator保存的是算法，每次调用next(g)，就计算出g的下一个元素的值，直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误。
# 当然，上面这种不断调用next(g)实在是太变态了，正确的方法是使用for循环，因为generator也是可迭代对象
# 所以，我们创建了一个generator后，基本上永远不会调用next()，而是通过for循环来迭代它，并且不需要关心StopIteration的错误
for n in g:
    print(n)

# 斐波拉契数列用列表生成式写不出来，但是，用函数把它打印出来却很容易 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
L =[]
def fib(max):
    n,a,b =0,0,1
    while n<max:
        L.append(b)
        a,b =b,a+b
        n= n+1
    return L

print(fib(20))

# 注意，赋值语句：
# a,b =b,a+b
# t = (b, a + b) # t是一个tuple
# a = t[0]
# b = t[1]

# 上面的函数和generator仅一步之遥。要把fib函数变成generator，只需要把print(b)改为yield b就可以了
# 这就是定义generator的另一种方法。如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
def fib_gen(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

print(fib_gen(10))  #<generator object fib_gen at 0x000000000295FFC0>

M =fib_gen(10)
for m in M:
    print(m)

# 但是用for循环调用generator时，发现拿不到generator的return语句的返回值。如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中
while True:
    try:
        x =next(M)
        print('m:',x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break


