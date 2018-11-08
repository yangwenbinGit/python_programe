# 调用函数 Python内置了很多有用的函数，我们可以直接调用
# 求绝对值的函数,调用abs函数
print(abs(20))
print(abs(-50))
print(abs(13.14))

# 调用函数的时候，如果传入的参数数量不对，会报TypeError的错误 abs() takes exactly one argument (2 given)
# print(abs(1, 2))

# 如果传入的参数数量是对的，但参数类型不能被函数所接受，也会报TypeError的错误 bad operand type for abs(): 'str'  错误的参数类型str
# print(abs('a'))

# 而max函数max()可以接收任意多个参数，并返回最大的那个
print(max(1,2))
print(max(2, 3, 1, -5))

# 类型转换函数 Python内置的常用函数还包括数据类型转换函数，比如int()函数可以把其他数据类型转换为整数
print(int('123'))
print(int(12.34))
print(float('33.788'))
print(str(123))
print(str(100))
print(bool(1))
print(bool(''))

# 可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”：
a =int
print(a(12.88))

# 在def_function这个文件中定义了一个函数，我们现在要调用my_abs()这个函数,我们先要导入这个函数，然后在调用
# 用from def_function import my_abs 来导入my_abs()函数
from def_function import my_abs
print(my_abs(-9))
