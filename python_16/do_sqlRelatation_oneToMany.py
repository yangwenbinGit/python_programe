from sqlalchemy import Column, String, create_engine, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()


# 初始化数据库连接:
# '数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
engine = create_engine('mysql+mysqlconnector://root:password@localhost:3306/test')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

# 一对多的关系
# 由于关系数据库的多个表还可以用外键实现一对多、多对多等关联，相应地，ORM框架也可以提供两个对象之间的一对多、多对多等功能。
# 例如，如果一个User拥有多个Book，就可以定义一对多关系如下
class User(Base):

    __tablename__ = 'user'

    id = Column(String(20),primary_key=True)
    name =Column(String(20))

    # 对应人和书的关系  一对多 一个人对应多本书
    # 在用户表类中通过 relationship() 方法来引用书表的类集合
    books = relationship('Book')


class Book(Base):

    __tablename__ = 'book'

    id = Column(String(20),primary_key=True)
    name = Column(String(20))

    # 多的一方的book表中设置了一个外键字段user_id,这个字段保存了属于哪个用户,通过这个外键指向user对象
    # 千万要记住 ForeignKey(数据库名.字段名) book表的外键对应的是用户表的id主键,要一定注意大小写
    user_id = Column(String(20),ForeignKey('user.id'))
    User = relationship("User", backref="Book")


# 一对多测试
session = DBSession()

Book = session.query(Book).first()
print('书作者的编号是:',Book.user_id)

User = session.query(User).filter(User.id == Book.user_id).one()
# print('id:',User.id)
# print('name:',User.name)
# 获取用户所写的书
print(User.books)
for book in User.books:
    print('book id is :',book.id,'  ,book name is:',book.name,'  ,book user_id is:',book.user_id)

print('author name is:',User.name,' ,author id is :',User.id)

# 获取到书对应的用户(这样就可以双向匹配了)
print(Book.User.name)
print(Book.User.id)

# 关闭session
session.close()



