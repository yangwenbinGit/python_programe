from types import MethodType
# 面向对象高级编程   使用__slots__
# 正常情况下,我们定义了一个class,我们给可以给该实例绑定任何的属性和方法 这就是动态语言的灵活性
class Student(object):
    pass
# 尝试给实例绑定一个属性
s =Student()
s.name = 'Michael'
print(s.name)

# 尝试给实例绑定一个方法
def set_age(self,age):
    self.age = age
s.set_age =MethodType(set_age,s)  # 给实例绑定一个方法
s.set_age(30)
print(s.age)

# 但是，给一个实例绑定的方法，对另一个实例是不起作用的
# 在创建一个实例,然后用这个实例去调用给上一个实例绑定的方法 因为没有这个方法所以会报错
s1 = Student()
# s1.set_age(45)  # AttributeError: 'Student' object has no attribute 'set_age'

# 为了给所有的实例都绑定方法，可以给class绑定方法：
def set_score(self,score):
    self.score = score

Student.set_score = set_score

# 给class绑定方法后,所有的实例均可调用：
s.set_score(90)
print(s.score)
s1.set_score(77)
print(s1.score)

# 使用__slots__
# 但是，如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性
# 为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性
class Teacher(object):
    __slots__ = ('name','age')  # 用元组定义允许绑定的属性名称

t = Teacher()
t.name = 'Tai Ge'
t.age = 30
# 绑定一个不允许绑定的属性，就会直接报错,因为绑定了不能绑定的属性  AttributeError: 'Teacher' object has no attribute 'score'
# 由于'score'没有被放到__slots__中，所以不能绑定score属性，试图绑定score将得到AttributeError的错误
# t.score =90


# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
class GraduateTeacher(Teacher):
    pass
g = GraduateTeacher()
g.score = 90
print(g.score)  # 在这里看到__slots__只是在本类中有用，但是一个子类继承了他，对于子类是没有任何的影响的
