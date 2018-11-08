# datetime
# datatime是Python处理日期和时间的标准库

# 获取当前日期和时间
# ImportError: cannot import name 'datetime' 当我导入from datetime import datetime的时候发现报错了,原因是我的类起了一个名字
# 也叫datetime,这样在执行的时候先找的我本地的类执行的，没有找到直接报错了
from datetime import datetime,timedelta,timezone

now = datetime.now()   # 返回的是当前的日期,类型是datetime
print(now)
print(type(now))

# 获取指定日期和时间
dt = datetime(2018,11,5,9,40)
print(dt)   # 2018-11-05 09:40:00

# datetime转换为timestamp
# 把一个datetime类型转换为timestamp只需要简单调用timestamp()方法：
# Python的timestamp是一个浮点数。如果有小数位，小数位表示毫秒数
print(dt.timestamp())  # 1541382000.0

# timestamp转换为datetime
print(datetime.fromtimestamp(dt.timestamp()))
# timestamp也可以直接被转换到UTC标准时区的时间，整整会和当前的时间相差8个小时
print(datetime.utcfromtimestamp(dt.timestamp()))

# 将str转换为datetime 转换方法是通过datetime.strptime()实现，需要一个日期和时间的格式化字符串
cday = datetime.strptime('2015-11-06 09:57:29', '%Y-%m-%d %H:%M:%S')
print(cday)

# 将datetime转换为str
# %a 表示的是星期 %b表示的是月份  %d表示的是日   %H表示的是小时  %M表示的是分钟
now_time = datetime.now()
print(now_time.strftime('%a,%b %d %H:%M'))

# datetime加减 可以计算出当前时间往后或者往前多久时间
print(now + timedelta(hours=10))
print(now - timedelta(days=1))
print(now + timedelta(days=2,hours=12))

# 本地时间转换为UTC时间 就是北京时间
# 创建时区UTC+8:00
tz_utc_8 = timezone(timedelta(hours=8))
now = datetime.now()
print(now)
dt = now.replace(tzinfo=tz_utc_8) # 强制设置为UTC+8:00
print(dt)

# 时区转换
# 我们可以先通过utcnow()拿到当前的UTC时间，再转换为任意时区的时间：

# 拿到UTC时间，并强制设置时区为UTC+0:00:
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)
# astimezone()将转换时区为北京时间:
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)
# astimezone()将转换时区为东京时间:
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt)
# astimezone()将bj_dt转换时区为东京时间:
tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=2)))
print(tokyo_dt2)