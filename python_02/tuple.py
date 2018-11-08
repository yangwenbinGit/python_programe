# 另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改
classmates = ('Michael', 'Bob', 'Tracy')
print(classmates)

# 现在，classmates这个tuple不能变了，它也没有append()，insert()这样的方法。其他获取元素的方法和list是一样的，你可以正常地使用classmates[0]，classmates[-1]，但不能赋值成另外的元素
print(classmates[0])
print(classmates[-1])

# 不可变的tuple有什么意义？因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple。
# tuple的陷阱：当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来 因为初始化就无法改变
t = (1,2)
print(t)

# 如果要定义一个空的tuple，可以写成()
t =()
print(t)
print(len(t))

# 要定义一个只有1个元素的tuple
# 如果只有1个元素的tuple 在定义的时候必须加一个逗号, 因为这是和表示数学公式的小括号分开，消除歧义
t=(1,)
print(t)
print(len(t))

# 来看一个“可变的”tuple：
t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)

# 为什么说tuple是不可变的 现在又变成可变的了，仔细看我们就可以知道tuple本身有3个元素，但是请看索引是2的元素，他是[A,B],其实
# 它是一个list集合，list集合的特性是可以赋值和改变的，还有append和insert方法。
# list和tuple是Python内置的有序集合，一个可变，一个不可变。根据需要来选择使用它们



