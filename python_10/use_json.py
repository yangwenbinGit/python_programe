# JSON
# 我们先看看如何把一个python对象转换为json

import json
# d = {'name':'yangwenbin','age':20,'score':98}
d = dict(name='yangwenbin',age = 28,score =99)
print(json.dumps(d))  # {"name": "yangwenbin", "age": 28, "score": 99}

# dumps()方法返回一个str，内容就是标准的JSON。类似的，dump()方法可以直接把JSON写入一个file-like Object
# 要把JSON反序列化为Python对象，用loads()或者对应的load()方法，前者把JSON的字符串反序列化，后者从file-like Object中读取字符串并反序列化

# json反序列化
json_str = json.dumps(d)
print(json.loads(json_str))


# JSON进阶
# 将一个对象转化为json
class Student(object):
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score
s =Student('yangwenbin',28,99)
# print(json.dumps(s))

# 当按照上面的方式直接对s对象实例进行序列化的时候，直接报错，提示Student不能被json序列化
# TypeError: Object of type 'Student' is not JSON serializable
# 前面的代码之所以无法把Student类实例序列化为JSON，是因为默认情况下，dumps()方法不知道如何将Student实例变为一个JSON的{}对象
# 可选参数default就是把任意一个对象变成一个可序列为JSON的对象，我们只需要为Student专门写一个转换函数，再把函数传进去即可
def StudentToJson(std):
    return {
        'name' : std.name,
        'age' : std.age,
        'score' : std.score
    }

# 当我们修改以后 通过下面的方式将这个Student转换为json，其实是现将Student转换为dict，然后再把dict转换为json
# 这样，Student实例首先被StudentToJson()函数转换成dict，然后再被顺利序列化为JSON：
# {"name": "yangwenbin", "age": 28, "score": 99}  这样就成功的转换了
print(json.dumps(s,default=StudentToJson))

# 但是我们想如果每次把一个对象转换为json,还要在写一个转换函数太麻烦了，每次转换都要写
# 我们可以偷个懒,把任意的class的实例变为dict,这样写也可以
# 因为通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量。也有少数例外，比如定义了__slots__的class。
print(json.dumps(s, default=lambda obj: obj.__dict__))

# 对于对象进行反序列化
def dict2student(d):
    return Student(d['name'],d['age'],d['score'])

json_str = json.dumps(s, default=lambda obj: obj.__dict__)
print(json.loads(json_str,object_hook=dict2student))  # 反序列化为一个实例,先通过函数转化为一个对象实例,然后返回回去
# <__main__.Student object at 0x00000000029F9780>  这样就实现了对象的反序列化



# 加了这个ensure_ascii=True以后的话,中文字符就会被编码为16进制
obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=True)
print(s)