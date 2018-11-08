# python的继承和多态
# 在OOP程序设计中，当我们定义一个class的时候，可以从某个现有的class继承，新的class称为子类（Subclass），而被继承的class称为基类、父类或超类（Base class、Super class）
class Animal(object):
    def run(self):
        print('Animal is running...')

    def eat(self):
        print('Animal is eating...')
# 当我们需要在编写一个狗或猫的类的时候 可以直接从Animal类中继承:
# 对于Dog来说，Animal就是它的父类，对于Animal来说，Dog就是它的子类。Cat和Dog类似
class Dog(Animal):
    def shout(self):
        print('Dog is shouting...')

    def run(self):
        print('Dog is running...')

class Cat(Animal):
    def shout(self):
        print('Cat is shouting...')

    def run(self):
        print('Cat is running...')

class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')
# 当继承了父类之后子类可以调用父类的方法
dog =Dog()
dog.run()
dog.eat()

cat =Cat()
cat.run()
cat.eat()

# 子类也可以有一些自己的特有方法
print('=========================================================================')
dog.shout()
cat.shout()

# 我们想如果在父类中有了这个run方法，子类继承了父类，在子类中也写了一个run方法
# 这样的话子类就会覆盖父类的方法，调用的时候就会走子类的run的方法，这样就获得了继承的另外一个好处：多态
print('=========================================================================')
dog.run()
cat.run()

a = list() # a是list类型
b = Animal() # b是Animal类型
c = Dog() # c是Dog类型

# 判断一个变量是否是某个类型可以用isinstance()判断
# 看来a、b、c确实对应着list、Animal、Dog这3种类型  看来c不仅仅是Dog,c还是Animal类型！
print('=========================================================================')
print(isinstance(a,list))
print(isinstance(b,Animal))
print(isinstance(c,Dog))
print(isinstance(c,Animal))

print('=========================================================================')
b =Animal()
print(isinstance(b,Dog))  # 这里就是打印出False 狗属于动物这是正确的，但是让父类属于子类这是错误的。就好像动物不属于狗一样

# 要理解多态的好处，我们还需要再编写一个函数，这个函数接受一个Animal类型的变量
def run_twice(animal):
    animal.run()
    animal.run()
# 我们分别传入Animal Dog Cat进行测试 看分别打印出来的是什么
print('=========================================================================')
run_twice(Animal())
run_twice(Dog())
run_twice(Cat())
run_twice(Tortoise())

# 多态的好处就是，当我们需要传入Dog、Cat、Tortoise……时，我们只需要接收Animal类型就可以了，因为Dog、Cat、Tortoise……都是Animal类型，然后，按照Animal类型进行操作即可。由于Animal类型有run()方法，因此，传入的任意类型，只要是Animal类或者子类，就会自动调用实际类型的run()方法，这就是多态的意思
#       ┌───────────────┐
#                 │    object     │
#                 └───────────────┘
#                         │
#            ┌────────────┴────────────┐
#            │                         │
#            ▼                         ▼
#     ┌─────────────┐           ┌─────────────┐
#     │   Animal    │           │    Plant    │
#     └─────────────┘           └─────────────┘
#            │                         │
#      ┌─────┴──────┐            ┌─────┴──────┐
#      │            │            │            │
#      ▼            ▼            ▼            ▼
# ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐
# │   Dog   │  │   Cat   │  │  Tree   │  │ Flower  │
# └─────────┘  └─────────┘  └─────────┘  └─────────┘

# 静态语言 vs 动态语言
# 对于静态语言（例如Java）来说，如果需要传入Animal类型，则传入的对象必须是Animal类型或者它的子类，否则，将无法调用run()方法。
# 对于Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了
# 如果在test类中没有run方法，那么的话运行的时候就要报错，因为找不到run方法  AttributeError: type object 'test' has no attribute 'run'
class Timer(object):
    def run(self):
        print('start...')

class test(object):
    def run(self):
        print('test run...')

run_twice(Timer())
run_twice(test())

# 对于python这种动态语言 他并不需要严格的继承体系  一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子