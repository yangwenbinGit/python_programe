# 多重继承
# 继承是面向对象编程的一个重要的方式，因为通过继承，子类就可以扩展父类的功能
class Animal(object):
    pass

# 哺乳类
class Mammal(Animal):
    pass

# 鸟类
class Bird(Animal):
    pass

# 各种动物
# 狗
class Dog(Mammal):
    pass
# 蝙蝠
class Bat(Mammal):
    pass
# 鹦鹉
class Parrot(Bird):
    pass
# 鸵鸟
class Ostrich(Bird):
    pass

# 现在，我们要给动物再加上Runnable和Flyable的功能，只需要先定义好Runnable和Flyable的类
class RunableMixIn(object):
    def run(self):
        print('Running...')

class FlyableMixIn(object):
    def fly(self):
        print('Flying...')
# 食肉
class CarnivorousMixIn(object):
    def carnivorous(self):
        print('Carnivorous...')
# 食草
class HerbivoresMixIn(object):
    def herbivores(self):
        print('Herbivores...')

# MixIn
# 通过多重继承，一个子类就可以同时获得多个父类的所有功能
# 对于需要Runnable功能的动物，就多继承一个Runnable，例如Dog
class Dog(Mammal,RunableMixIn,CarnivorousMixIn):
    pass
# 对于需要Flyable功能的动物，就多继承一个Flyable，例如Bat
class Parrot(Bird,FlyableMixIn,HerbivoresMixIn):
    pass





