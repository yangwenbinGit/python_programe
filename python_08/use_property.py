# 使用@property
# 在绑定属性时，如果我们直接把属性暴露出去，虽然写起来很简单，但是，没办法检查参数，导致可以把成绩随便改
class Student(object):
    pass

s =Student()
s.score = 9999
print(s.score)

# 将分数设置成9999这显然是不对的，为了限制score的范围,可以通过一个set_score()方法来设置成绩
# 再通过一个get_score()来获取成绩，这样在set_score就可以检查参数
class Student1(object):
    def set_score(self,score):
        if not isinstance(score,int):
            raise ValueError('score must be an integer!')
        if score<0 or score>100:
            raise ValueError('score must be 0~100')
        self.score =score

    def get_score(self):
        return self.score
# 现在，对任意的Student实例进行操作，就不能随心所欲地设置score了：
s1 = Student1()
s1.set_score(60)
print(s1.get_score())  # 没有问题

# s1.set_score(9999)
# print(s1.get_score())  # 错误提示 ValueError: score must be 0~100

# 但是，上面的调用方法又略显复杂，没有直接用属性这么直接简单
# 还记得装饰器（decorator）可以给函数动态加上功能吗？对于类的方法，装饰器一样起作用。Python内置的@property装饰器就是负责把一个方法变成属性调用的
class Student2(object):
    # 加上property就可以把getter方法变成属性
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

s2 = Student2()
s2.score = 60  # OK，实际转化为s2.set_score(60)
print(s2.score)  # OK，实际转化为s2.get_score()
# s2.score = 9999
# print(s2.score)  # ValueError: score must between 0 ~ 100!

# 上面的birth是可读写属性，而age就是一个只读属性，因为age可以根据birth和当前时间计算出来。
class Student3(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return str(2015) +'-'+ self._birth

s3 = Student3()
s3.birth = '10-15'  # 这里一定要注意是= 他变成了属性
print(s3.age)


# 请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution

class Screen(object):
    @property
    def wigth(self):
        return self._wigth

    @wigth.setter
    def wigth(self,value):
        self._wigth =value

    @property
    def heigth(self):
        return self._heigth

    @heigth.setter
    def heigth(self, value):
        self._heigth = value

    @property
    def area(self):
        return self._wigth * self._heigth

sc = Screen()
sc.wigth =20  # 请记得加了property就是属性了 不是方法
sc.heigth =30
print(sc.area)