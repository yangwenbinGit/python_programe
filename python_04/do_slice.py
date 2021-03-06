# 切片
# 取一个list或tuple的部分元素是非常常见的操作。比如，一个list如下：
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
# 取前3个元素，应该怎么做？笨办法就是:
print(L[0],L[1],L[2])

# 也可以用循环的方式 方式一
i=0
for x in L:
    if(i<3):
        print(L[i])
    i=i+1

# 方式二 range(5)生成的序列是从0开始小于5的整数 list(range(5)) 会将生成的数转换为list
r=[]
n=3
for i in list(range(n)):
    r.append(L[i])
print(r)
print(list(range(n)))

# 对这种经常取指定索引范围的操作，用循环十分繁琐，因此，Python提供了切片（Slice）操作符，能大大简化这种操作。
# 对应上面的问题，取前3个元素，用一行代码就可以完成切片：
# L[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3。即索引0，1，2，正好是3个元素
print(L[0:3])

# 如果第一个索引是0，还可以省略
print(L[:3])

# 也可以从索引1开始，取出2个元素出来
print(L[1:3])

# Python支持L[-1]取倒数第一个元素，那么它同样支持倒数切片
# 记住倒数第一个元素的索引是-1
print(L[-1:])   # ['Jack']
print(L[-2:])   # ['Bob', 'Jack']
print(L[-2:-1]) # ['Bob']

# 我们先创建一个0-99的数列
M =list(range(100))
print(M)

# 取出前10个数
print(M[0:10])  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# 取出后10个
print(M[-10:])
# 前11-20中的所有数：
print(M[11:21])
# 前10个数，每两个取一个：
print(M[0:10:2])
# 所有数，每5个取一个：
print(M[::5])
# 甚至什么都不写，只写[:]就可以原样复制一个list
print(M[:])

# tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple
N =(0,1,2,3,4,5)
print(N[:3])  # (0,1,2)

# 字符串'xxx'也可以看成是一种list，每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串
S ='ABCDEFG'
print(S[0:3])  # ABC
print(S[::2])  # ACEG

# 在很多编程语言中，针对字符串提供了很多各种截取函数（例如，substring），其实目的就是对字符串切片。Python没有针对字符串的截取函数，只需要切片一个操作就可以完成，非常简单
