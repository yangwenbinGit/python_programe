# python中的条件判断
# 比如，输入用户年龄，根据年龄打印不同的内容，在Python程序中，用if语句实现
# "your age is:",age 这里在连接的时候用的, 如果要是这样写"your age is:"+age 这是会报错的,因为类型不一样
age = 20;
if age > 18:
    print("your age is:", age)
    print("adult")
# 也可以给if添加一个else语句，意思是，如果if判断是False，不要执行if的内容，去把else执行了
age = 10
if age > 18:
    print("your age is", age)
    print("adult")
else:
    print('your age is ', age)
    print("teenager")
# 可以用elif做更细致的判断
age = 2
if age >= 18:
    print("your age is", age)
    print("adult")
elif age >= 12:
    print("your age is", age)
    print("teenager")
else:
    print("your age is", age)
    print("kids")

# elif是else if的缩写，完全可以有多个elif，所以if语句的完整形式就是
score = 95
if 90 <= score <= 100:
    print("your score is", score)
    print("Prefect")
elif score >= 80:
    print("your score is", score)
    print("Great")
elif score >= 70:
    print("your score is", score)
    print("Good")
else:
    print("your score is", score)
    print("ordinary")

# 只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False。
# x = 200
# x ='yangwenbin'
x =['y','w','b']
if x:
    print(True)
# 很多同学会用input()读取用户的输入，这样可以自己输入，程序运行得更有意思
# TypeError: '<' not supported between instances of 'str' and 'int' 我们发现报错了，说是str不能和int进行比较
# 原因是input()函数返回的类型是str,但是2000是一个int类型，这样比较的话会报错，必须先把str转换成整数,Python提供了int()函数来完成这件事情
str = input('请输入出生年份birth: ')
birth =int(str)
if birth < 2000:
    print('00前')
else:
    print('00后')
    



