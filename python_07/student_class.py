# 类 class
# 在Python中，定义类是通过class关键字
# class后面紧接着是类名，即Student，类名通常是大写开头的单词，紧接着是(object)，表示该类是从哪个类继承下来的，继承的概念我们后面再讲，通常，如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类
class Student(object):
    pass


# 定义好了Student类，就可以根据Student类创建出Student的实例，创建实例是通过类名+()实现的
# 可以看到，变量bart指向的就是一个Student的实例，后面的0x10a67a590是内存地址，每个object的地址都不一样，而Student本身则是一个类
bart = Student()
print(bart)  # <__main__.Student object at 0x000000000219EEF0>
print(Student)  # <class '__main__.Student'>

# 可以自由地给一个实例变量绑定属性，比如，给实例bart绑定一个name属性：
bart.name ='WenHao Yang'
print(bart.name)

# 由于类可以起到模板的作用，因此，可以在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去。通过定义一个特殊的__init__方法，在创建实例的时候，就把name，score等属性绑上去
# 注意到__init__方法的第一个参数永远是self，表示创建的实例本身，因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身。
# 有了__init__方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数，但self不需要传，Python解释器自己会把实例变量传进去：
#  注意：特殊方法“__init__”前后分别有两个下划线！！！
class Student_init(object):
    def __init__(self,name,score,age):
        self.name =name
        self.score =score
        self.age =age

    def get_grade(self):
        if self.score >=90:
            return 'A'
        elif self.score >= 80:
            return 'B'
        elif self.score >= 70:
            return 'C'
        else:
            return 'D'

    def checkAge(self):
        if self.age < 18:
            self.info = '未满十八岁'
        elif self.age < 40:
            self.info = '拼搏的时代'
        elif self.age < 70:
            self.info = '请注意身体'
        else:
            self.info = '年过七旬'

    # 数据封装
    def print_score(self):
        print('姓名是:'+self.name+','+'成绩是:'+str(self.score)+','+'年龄是:'+str(self.age)+','+'年龄信息:'+self.info)

# 初始化和调用方法
bart_init =Student_init('WenBin Yang',99,23);
bart_init.checkAge()
print(bart_init.get_grade())
bart_init.print_score()
print(bart_init.info)


print('============================================================')
lisa =Student_init('Lisa',98,22)
bob =Student_init('Bob',70,75)
lisa.checkAge()
bob.checkAge()
print(lisa.print_score())
print(bob.print_score())


# 类是创建实例的模板，而实例则是一个一个具体的对象，各个实例拥有的数据都互相独立，互不影响；
#
# 方法就是与实例绑定的函数，和普通函数不同，方法可以直接访问实例的数据；
#
# 通过在实例上调用方法，我们就直接操作了对象内部的数据，但无需知道方法内部的实现细节。
#
# 和静态语言不同，Python允许对实例变量绑定任何数据，也就是说，对于两个实例变量，虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不同：


