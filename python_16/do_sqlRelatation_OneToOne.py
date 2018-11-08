from sqlalchemy import Column, String, create_engine, ForeignKey, Integer, MetaData, Table, or_, and_
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()


# 初始化数据库连接:
# '数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
engine = create_engine('mysql+mysqlconnector://root:password@localhost:3306/test')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)
session = DBSession()

# python增删改查一整套
# 测试一对一的关系
class User(Base):
    __tablename__ = 'user'
    id = Column(String(20),primary_key=True)
    name =Column(String(20))

    # 一对一的情况，这里要设置下, uselist设置成false, 关闭列表让一对多，变成一对一的关系
    userInformation = relationship('UserInformation',uselist=False)


class UserInformation(Base):
    __tablename__ = 'user_information'  # 表名
    id = Column(String(20), primary_key=True)
    id_number = Column(String(20),nullable=True)
    age = Column(Integer)
    sex = Column(String(1))
    user_id = Column(String(20))

    user_id = Column(String(20), ForeignKey('user.id'))
    # 这里是通过用户信息可以直接找到用户
    User = relationship("User", backref="UserInformation")

# 初始化数据库
def init_de():
    Base.metadata.create_all(engine)

# 删除所有的数据库表
def drop_db():
    Base.metadata.drop_all(engine)

# 创建表
# init_de()

# 往user_information中添加记录
# user_information = UserInformation(id ='1',id_number ='140181199205031413',age =22,sex ='1',user_id ='1')
# session.add(user_information)
# user_information = UserInformation(id ='2',id_number ='140181199205031413',age =24,sex ='1',user_id ='2')
# session.add(user_information)
# user_information = UserInformation(id ='3',id_number ='140181199205031413',age =28,sex ='0',user_id ='3')
# session.add(user_information)
# session.commit()

# 更新一条记录
# query = session.query(UserInformation)
# UserInformation = query.get('1')
# UserInformation.id_number = '140181199205038888'
# session.commit()
# print(UserInformation)

# 删除记录
# session.query(User).filter(User.id == 2).delete()
# session.commit()
# session.close()

# 增加一个
# user = User(id ='2',name ='Bob')
# session.add(user)
# session.commit()


# 按条件查询
user = session.query(User).filter_by(name="Yang wenbin").first()
print(user)

# 查询所有
user = session.query(User).filter_by().all()
print(user)

# 过滤表的条件
# 这样的会打印出sql语句
my_userInfromation = session.query(UserInformation).filter(UserInformation.id_number.like("%140%"))
print(my_userInfromation)
# equals
print(session.query(UserInformation).filter(UserInformation.id == '1'))
# not equals
print(session.query(UserInformation).filter(UserInformation.age != 22))
# in 打印sql语句
print(session.query(UserInformation).filter(UserInformation.id.in_(['1', '2'])))
# in 打印数据
print(session.query(UserInformation).filter(UserInformation.id.in_(['1', '2'])).all())
# not in
print(session.query(UserInformation).filter(~UserInformation.id.in_(['1', '2'])))
# AND:
print(session.query(UserInformation).filter(and_(UserInformation.id=='1',UserInformation.age == 22)))
print(session.query(UserInformation).filter(UserInformation.id=='1').filter( UserInformation.age == 22))
# OR
print(session.query(UserInformation).filter(or_(UserInformation.id=='1',UserInformation.age == 22)))
# 按条件查询列表
user = session.query(User).filter(User.name=="Yang wenbin")
print(user)

# 如果我们要查询数据呢,而不是打印sql
# <__main__.UserInformation object at 0x000000000398BF98>
print(session.query(UserInformation).filter(UserInformation.id == '1').one())


UserInformation = session.query(UserInformation).first()
print(UserInformation)
# 从用户信息中获取用户
print(UserInformation.User)
print(UserInformation.User.name)
# 从用户中获取用户信息 至此一对一完成
User = session.query(User).first()
print(User.userInformation)
print(User.userInformation.age)

# 关闭session
session.close()



