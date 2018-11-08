# 递归函数
# 在函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，这个函数就是递归函数
# 计算n的阶乘,可以理解成(n-1)!*n
# 比如5！可以理解成5!=5*4！ 4!=4*3!  3!=3*2! 2!=2*1!  ==>5!=5*4*3*2*1=120
def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)

# 调用阶乘
print(fact(1))
print(fact(5))
print(fact(100))

# 如果我们计算fact(5)，可以根据函数定义看到计算过程如下：
# ===> fact(5)
# ===> 5 * fact(4)
# ===> 5 * (4 * fact(3))
# ===> 5 * (4 * (3 * fact(2)))
# ===> 5 * (4 * (3 * (2 * fact(1))))
# ===> 5 * (4 * (3 * (2 * 1)))
# ===> 5 * (4 * (3 * 2))
# ===> 5 * (4 * 6)
# ===> 5 * 24
# ===> 120

# 由于上面的方式递归的层数增加就会出现栈溢出的情况，栈溢出解决的办法就是通过尾递归优化，尾递归可以看做事一种特殊的循环
# 上面的fact(n)函数由于return n * fact(n - 1)引入了乘法表达式，所以就不是尾递归了。要改成尾递归方式，需要多一点代码，主要是要把每一步的乘积传入到递归函数中
def fact_w(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

print(fact_w(1))
print(fact_w(5))
print(fact_w(100))
# print(fact_w(1000)) # RecursionError: maximum recursion depth exceeded in comparison

# 可以看到，return fact_iter(num - 1, num * product)仅返回递归函数本身，num - 1和num * product在函数调用前就会被计算，不影响函数调用
# fact(5)对应的fact_iter(5, 1)的调用如下：
# ===> fact_iter(5, 1)
# ===> fact_iter(4, 5)
# ===> fact_iter(3, 20)
# ===> fact_iter(2, 60)
# ===> fact_iter(1, 120)
# ===> 120

# 尾递归调用时，如果做了优化，栈不会增长，因此，无论多少次调用也不会导致栈溢出。
# 遗憾的是，大多数编程语言没有针对尾递归做优化，Python解释器也没有做优化，所以，即使把上面的fact(n)函数改成尾递归方式，也会导致栈溢出

# 利用递归函数移动汉诺塔:
def move(n, a, b, c):
    if n == 1:
        print('move', a, '-->', c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)

move(3, 'A', 'B', 'C')