# 把一个表的内容用Python的数据结构表示出来的话，可以用一个list表示多行，list的每一个元素是tuple，表示一行记录，比如，包含id和name的user表
# [
#     ('1', 'Michael'),
#     ('2', 'Bob'),
#     ('3', 'Adam')
# ]

# 但是我们发现用元组的话不太容易看出表的结构,如果把一个tuple用class实例表示 就可以很容易的看出表结构
# class User(object):
#     def __init__(self,id,name):
#         self.id = id
#         self.name = name
#
# [
#     User('1', 'Michael'),
#     User('2', 'Bob'),
#     User('3', 'Adam')
# ]

# 这就是传说中的ORM技术：Object-Relational Mapping，把关系数据库的表结构映射到对象上。是不是很简单？
# 在Python中，最有名的ORM框架是SQLAlchemy。我们来看看SQLAlchemy的用法。

# 第一步，导入SQLAlchemy，并初始化DBSession：
from sqlalchemy import Column, String, create_engine, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()

# 定义User对象:
# 以上代码完成SQLAlchemy的初始化和具体每个表的class定义。如果有多个表，就继续定义其他class

class User(Base):
    # 表的名字:
    __tablename__ = 'user'

    # 表的结构:
    id = Column(String(20), primary_key=True)
    name = Column(String(20))

# 初始化数据库连接:
# '数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
engine = create_engine('mysql+mysqlconnector://root:password@localhost:3306/test')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

# 由于有了ORM，我们向数据库表中添加一行记录，可以视为添加一个User对象
# 创建session对象
# session = DBSession()
# # 创建新的user对象
# new_user = User(id ='5',name='YANG WenBin')
# # 添加到session:
# session.add(new_user)
# # 提交即可保存到数据库中
# session.commit()
# # 关闭session
# session.close()

# 可见，关键是获取session，然后把对象添加到session，最后提交并关闭。DBSession对象可视为当前数据库连接。
# 如何从数据库表中查询数据呢？有了ORM，查询出来的可以不再是tuple，而是User对象。SQLAlchemy提供的查询接口如下
session = DBSession()
#
# 创建query查询,filter是where条件,最后调用one()返回唯一行,如果调用all()则返回所有行：
User = session.query(User).filter(User.id == 5).one()
# 查询到一条对象的时候,我们打印对象的id和name属性
print('type:',type(User))
print('id:',User.id)
print('name:',User.name)
# 最后要关闭session
session.close()

# 从结果来看我们使用了ORM的模式,将查询到的数据自动封装到User类中
# type: <class '__main__.User'>
# id: 5
# name: YANG WenBin

