# python中的循环编写
# 要计算1+2+3，我们可以直接写表达式：
print(1 + 2 + 3)
# 如果要算1+...+10000这样写就不行了。
# Python的循环有两种，一种是for...in循环，依次把list或tuple中的每个元素迭代出来
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

# 如果我们要计算1到10的累加和
number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum = 0;
for num in number:
    sum += num
print('sum的累加和是:', sum)

# 如果要计算1-100的整数之和，从1写到100有点困难，幸好Python提供一个range()函数，可以生成一个整数序列，再通过list()函数可以转换为list。比如range(5)生成的序列是从0开始小于5的整数
print(list(range(5)))

# 生成0-100的序列然后计算总和
numbers = list(range(101))
sum = 0
for num in numbers:
    sum += num;
print('sum的累加和是:', sum)

# 第二种循环是while循环，只要条件满足，就不断循环，条件不满足时退出循环。比如我们要计算100以内所有奇数之和，可以用while循环实现
sum = 0;
n = len(numbers) - 1
while (n > 0):
    sum += numbers[n]
    n -= 1;
print('while方式的累加和是:', sum)

# break和continue的测试
# break语句可以在循环过程中直接退出循环，而continue语句可以提前结束本轮循环，并直接开始下一轮循环。这两个语句通常都必须配合if语句使用。
n = 1
sum = 0
while (n <= 100):
    sum += n;
    n += 2;
    if (sum >= 2000):
        break
    else:
        continue
print('break的测试结果得出的sum的值是:', sum)

# 请利用循环依次对list中的每个名字打印出Hello, xxx!
L = ['Bart', 'Lisa', 'Adam']
str ='Hello,'
for name in L:
    str += name +","
print(str.strip().strip(','))  # 删除字符串两边的,和空字符  Hello,Bart,Lisa,Adam


