# 偏函数
print(int('12345'))

# 但int()函数还提供额外的base参数，默认值为10。如果传入base参数，就可以做N进制的转换
print(int('12345',base=8))  # 将12345先由str 转换为int类型 然后在转换为8进制
print(int('12345',base=16))

# 假设要转换大量的二进制字符串，每次都传入int(x, base=2)非常麻烦，于是，我们想到，可以定义一个int2()的函数，默认把base=2传进去
def int2(str,base=2):
    return int(str,base)

print(int2('1000000'))
print(int2('1010101'))
print(int2('10001100',base=10))

# functools.partial就是帮助我们创建一个偏函数的，不需要我们自己定义int2()，可以直接使用下面的代码创建一个新的函数int2：
import functools
int3 =functools.partial(int,base=2)
print(int3('10000000'))
print(int3('10101010'))

# *args是非关键字参数，用于元组，**kw是关键字参数，用于字典

# 最后，创建偏函数时，实际上可以接收函数对象、*args和**kw这3个参数，当传入：

int2 = functools.partial(int, base=2)
# 实际上固定了int()函数的关键字参数base，也就是：

int2('10010')
# 相当于(base=2 这样表示的可以用dict表示{'base':2},当他传入的时候因为是关键字参数会被放在kw中)：

kw = { 'base': 2 }
int('10010', **kw)
# 当传入：

max2 = functools.partial(max, 10)
# 实际上会把10作为*args的一部分自动加到左边，也就是：

max2(5, 6, 7)
# 相当于：

args = (10, 5, 6, 7)
max(*args)  # *args非关键字参数 可变参数
# 结果为10。