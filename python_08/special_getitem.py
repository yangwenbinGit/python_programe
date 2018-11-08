# __getitem__
# Fib实例虽然能作用于for循环，看起来和list有点像，但是，把它当成list来使用还是不行，比如，取第5个元素：
class Fib(object):
    def __getitem__(self, n):
        if isinstance(n, int):  # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):  # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

# 如果这样取的话  TypeError: 'Fib' object does not support indexing
# print(Fib()[5])

# 要表现得像list那样按照下标取出元素，需要实现__getitem__()方法：
f = Fib()
print(f[0])
print(f[1])
print(f[2])
print(f[3])
print(f[3])
print(f[10])
print(f[100])

# 如果要取出100范围之内的 区间在[5:20)之内的所有的值  变成list的方式打印
a = list(range(100))[5:20]
print(a)

# 传入切片类型 L[0:10] 取一个范围这就是切片 L=list(range(100))
print(f[0:5])
print(f[:10])  # [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
