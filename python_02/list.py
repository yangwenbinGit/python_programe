# 使用list和tuple
# Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素。

# 列出班里所有同学的名字，就可以用一个list表示
classmates =['Michael','Bob','Tracy']
print(classmates)

# 用len()函数可以获得list元素的个数
print(len(classmates))

# 用索引来访问list中每一个位置的元素，记得索引是从0开始的
print(classmates[0])
print(classmates[1])
print(classmates[2])

# 当索引超出了范围时，Python会报一个IndexError错误，所以，要确保索引不要越界，记得最后一个元素的索引是len(classmates) - 1
# IndexError: list index out of range
# print(classmates[3])

# 如果要取最后一个元素，还可以用-1做索引,直接获取最后一个元素
print(classmates[-1])

# 以此类推，可以获取倒数第2个、倒数第3个：
print(classmates[-2])
print(classmates[-3])

# list是一个可变的有序表，所以，可以往list中追加元素到末尾
classmates.append('Adam')
print(classmates)

# 也可以把元素插入到指定的位置，比如索引号为1的位置：
classmates.insert(1,'jack')
print(classmates)

# 要删除list末尾的元素，用pop()方法
print(classmates.pop())
print(classmates)

# 要删除指定位置的元素，用pop(i)方法，其中i是索引位置
print(classmates.pop(1))
print(classmates)

# 要把某个元素替换成别的元素，可以直接赋值给对应的索引位置
classmates[1] ='Jack'
print(classmates)

# 对于python list中可以放不同类型的元素，但是java是不允许的
# TypeError: insert() takes exactly 2 arguments (1 given) 如果需要2个参数但是，如果只传入一个就是报错
classmates.insert(1,'Ywb')
classmates.append(123)
classmates.append(89.88)
classmates.append(True)
print(classmates)

# list元素也可以是另一个list
s = ['python', 'java', ['asp', 'php'], 'scheme']
print(len(s))

# 要注意s只有4个元素，其中s[2]又是一个list，如果拆开写就更容易理解了
p =['asp','php']
s= ['python', 'java', p, 'scheme']
print(s)
print(s[2][0])
print(s[2][1])
print(s[2])

# 如果一个list中一个元素也没有，就是一个空的list，它的长度为0：
L =[]
print(len(L))

