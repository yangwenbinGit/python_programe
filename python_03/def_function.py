import math
# 定义函数
# 在Python中，定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，然后，在缩进块中编写函数体，函数的返回值用return语句返回
# 我们自定义一个求绝对值的函数
# 函数体内部的语句在执行时，一旦执行到return时，函数就执行完毕，并将结果返回。因此，函数内部通过条件判断和循环可以实现非常复杂的逻辑
# 如果没有return语句,函数执行完成后也会返回结果，只是结果为none,return None可以简写为return
def my_abs(x):
    if x > 0:
        return x
    else:
        return -x


# 调用函数
print(my_abs(99))
print(my_abs(-88))


# 如果想定义一个什么事也不做的空函数，可以用pass语句：
# pass语句什么都不做，那有什么用？实际上pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来
def nop():
    pass


# pass还可以运在其他语句里 缺少了pass，代码运行就会有语法错误
age = 20
if age >= 18:
    pass


# 对于上面的函数我们先没有对输入参数个数和输入参数类型合法做校验
# 对参数类型做检查，只允许整数和浮点数类型的参数。数据类型检查可以用内置函数isinstance()实现
def my_abs_update(*x):
    i =0
    if len(x) != 0:
        for p in x:
            i = i + 1
    if i > 1:
        raise TypeError('输入的参数个数不合法')
    if not isinstance(x, (int, float)):
        raise TypeError('输入的参数类型不合法')
    if x >= 0:
        return x
    else:
        return -x

# 输入的参数个数不合法例子
# print(my_abs_update(23,40))
# 输入的类型不匹配
# print(my_abs_update('haha'))

# import math语句表示导入math包，并允许后续代码引用math包里的sin、cos等函数
def move(x, y, step, angle):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

# 函数调用 多返回值,分别是x,y
x,y =move(100,100,60,math.pi /6)
print(x,y)    # 151.96152422706632 70.0

# 但其实这只是一种假象，Python函数返回的仍然是单一值
# 返回值是一个tuple ，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值，所以，Python的函数返回多值其实就是返回一个tuple(元组)
r =move(100,100,60,math.pi /6)
print(r)      # (151.96152422706632, 70.0)

# 定义函数时，需要确定函数名和参数个数
# 如果有必要，可以先对参数的数据类型做检查
# 函数体内部可以用return随时返回函数结果
# 函数执行完毕也没有return语句时，自动return None
# 函数可以同时返回多个值，但其实就是一个tuple