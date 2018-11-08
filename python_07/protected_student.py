# 访问限制
# 在Class内部，可以有属性和方法，而外部代码可以通过直接调用实例变量的方法来操作数据，这样，就隐藏了内部的复杂逻辑

class Student(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score

    def print_score(self):
        print('姓名:'+self.name,'成绩:'+str(self.score))


bart = Student('Bart Simpson', 59)
bart.print_score()
# 修改参数
bart.score =99
bart.name ='WenBin Yang'
bart.print_score()

# 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问，所以，我们把Student类改一改：
# 将类中的属性修改为私有，就是在属性前面加两个下划线__即可
class Student_private(object):
    def __init__(self,name,score):
        self.__name = name
        self.__score = score

    def set_name(self,name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_score(self,score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

    def get_score(self):
        return self.__score

    def print_score(self):
        print('姓名:'+self.__name,'成绩:'+str(self.__score))

bart = Student_private('Bart Simpson', 59)
bart.print_score()
# 如果我们直接从外部访问私有的变量__name或__score 会报错AttributeError: 'Student' object has no attribute '__name'
# bart.__name

# 下面的部分  虽然我们修改了成绩和名字  但是在打印的时候没有报错  依然是之前的 姓名:Bart Simpson 成绩:59
bart.__score =99
bart.__name ='WenBin Yang Protrct'
bart.print_score()

# 但是如果外部代码要获取name和score怎么办？可以给Student类增加get_name和get_score这样的方法：

# 最后注意下面的这种错误写法：
#
# >>> bart = Student('Bart Simpson', 59)
# >>> bart.get_name()
# 'Bart Simpson'
# >>> bart.__name = 'New Name' # 设置__name变量！
# >>> bart.__name
# 'New Name'
# 表面上看，外部代码“成功”地设置了__name变量，但实际上这个__name变量和class内部的__name变量不是一个变量！内部的__name变量已经被Python解释器自动改成了_Student__name，而外部代码给bart新增了一个__name变量。不信试试：
#
# >>> bart.get_name() # get_name()内部返回self.__name
# 'Bart Simpson'