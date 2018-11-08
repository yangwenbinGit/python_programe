# 使用枚举类
# 当我们需要定义常量时，一个办法是用大写变量通过整数来定义，例如月份
# 好处是简单，缺点是类型是int，并且仍然是变量
JAN = 1
FEB = 2
MAR = 3
NOV = 11
DEC = 12

# Python提供了Enum类来实现这个功能,就是枚举类
from enum import Enum,unique

# 这样我们就获得了Month类型的枚举类，可以直接使用Month.Jan来引用一个常量，或者枚举它的所有成员：
Month = Enum('Month',('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name,member in Month.__members__.items():
    print(name,'==>',member,'==>',member.value)
# value属性则是自动赋给成员的int常量，默认从1开始计数。 member.value 就是这个值 自动赋值
# Jan ==> Month.Jan ==> 1
# Feb ==> Month.Feb ==> 2
# Mar ==> Month.Mar ==> 3
# Apr ==> Month.Apr ==> 4
# May ==> Month.May ==> 5
# Jun ==> Month.Jun ==> 6
# Jul ==> Month.Jul ==> 7
# Aug ==> Month.Aug ==> 8
# Sep ==> Month.Sep ==> 9
# Oct ==> Month.Oct ==> 10
# Nov ==> Month.Nov ==> 11
# Dec ==> Month.Dec ==> 12

# 如果需要更精确地控制枚举类型，可以从Enum派生出自定义类
# @unique装饰器可以帮助我们检查保证没有重复值
@unique
class Weekday(Enum):
    Sun = 0   #将Sun的value的值设置为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

day1 = Weekday.Sun
print(day1)
print(Weekday.Thu)
print(Weekday['Sat'])
print(Weekday.Mon.value)
print(day1 == Weekday.Sun)
print(day1 == Weekday.Wed)
print(Weekday(1))  # Weekday.Mon
print(Weekday(3).value)
# 如果不存在的话就会报错
# print(Weekday(7))  #ValueError: 7 is not a valid Weekday

# name得到的就是里面的具体的Sun Fri   member得到的就是类名.name  value就是member.value的值
for name,member in Weekday.__members__.items():
    print(name,'==>',member,'==>',member.value)

# Sun ==> Weekday.Sun ==> 0
# Mon ==> Weekday.Mon ==> 1
# Tue ==> Weekday.Tue ==> 2
# Wed ==> Weekday.Wed ==> 3
# Thu ==> Weekday.Thu ==> 4
# Fri ==> Weekday.Fri ==> 5
# Sat ==> Weekday.Sat ==> 6

# 可见，既可以用成员名称引用枚举常量，又可以直接根据value的值获得枚举常量。

# 把Student的gender属性改造为枚举类型，可以避免使用字符串：
class Gender(Enum):
    Male =0
    Female = 1

for name,member in Gender.__members__.items():
    print(name,'==>',member,'==>',member.value)

# Male ==> Gender.Male ==> 0
# Female ==> Gender.Female ==> 1
