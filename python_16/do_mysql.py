# python连接mysql数据库
# 我们演示通过python连接到mysql数据库 并且操作数据库

# 导入mysql驱动
import mysql.connector

# 在连接数据库的时候设置用户名 密码和要连接的数据库
conn = mysql.connector.connect(user='root',password='password',database='test')
cursor = conn.cursor()

# 创建user表
cursor.execute('create table user(id varchar(20) primary key,name varchar(20))')

# 插入一行记录 注意mysql的占位符是%s
cursor.execute('insert into user (id,name) VALUES (%s,%s)',['1','Michael'])
cursor.execute('insert into user (id,name) VALUES (%s,%s)',['2','Bob'])
cursor.execute('insert into user (id,name) VALUES (%s,%s)',['3','March'])
cursor.rowcount

# 提交事务
conn.commit()
cursor.close()

# 进行查询
cursor = conn.cursor()
cursor.execute('select * from user where id = %s',['2'])
values = cursor.fetchall()
print(values)  # [('1', 'Michael')]

# 关闭Cursor和Connection:
cursor.close()
conn.close()

# 执行INSERT操作等后要调用commit()提交事务;
# MySQL的SQL的占位符是%s。