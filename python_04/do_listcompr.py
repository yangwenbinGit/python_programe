import os
# 列表生成式
# 列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。
# 要生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]可以用list(range(1, 11))
print(list(range(11)))
print(list(range(1,11)))

# 但如果要生成[1x1, 2x2, 3x3, ..., 10x10]怎么做？方法一是循环
L =[]
for x in list(range(1,11)):
    L.append((str(x)+ 'x' +str(x)).strip().strip("'"))
print(L)

# 但是循环太繁琐，而列表生成式则可以用一行语句代替循环生成上面的list
# 写列表生成式时，把要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来
print([str(x)+ 'x' +str(x) for x in range(1, 11)])

# for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方
# 列表生成式 执行顺序是 for x in range(1,11) 然后执行if判断 满足的话才输出结果  [4, 16, 36, 64, 100]
print([x*x for x in range(1,11) if x%2 ==0])

# 还可以使用两层循环，可以生成全排列
# ['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']
print([m+n for m in 'ABC' for n in 'XYZ'])

# 获取到当前目录下的所有文件和目录名
print([d for d in os.listdir('.')])

# for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value
d = {'x': 'A', 'y': 'B', 'z': 'C' }
for x,y in d.items():
    print(x+'='+y)
# 上面的也可以用简单的列表的方式一句话生成
# d.items()是可以将字典中的所有项，以列表方式返回
print(d.items())  # dict_items([('x', 'A'), ('y', 'B'), ('z', 'C')])
print([x+'='+y for x,y in d.items()])

# 最后把一个list中所有的字符串变成小写
L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])

# 使用内建的isinstance函数可以判断一个变量是不是字符串
# 如果包含数字的话在按照上面的方式写的话直接报错了 我们要判断是否是字符串 是的话在调用s.lower()
L = ['Hello', 'World', 18, 'IBM', 'Apple']
print([s.lower() for s in L if isinstance(s,str)])