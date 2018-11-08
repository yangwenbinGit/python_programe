# 有了ORM，我们就可以把Web App需要的3个表用Model表示出来
import time,uuid

# noinspection PyUnresolvedReferences
from orm import Model,StringField,BooleanField,FloatField,TextField

def next_id():
    return '%015d%s000' % (int(time.time() * 1000), uuid.uuid4().hex)


class User(Model):
    __table__ = 'Users'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    email = StringField(ddl='varchar(50)')
    passwd = StringField(ddl='varchar(50)')
    admin = BooleanField()
    name = StringField(ddl='varchar(50)')
    image = StringField(ddl='varchar(500)')
    created_at = FloatField(default=time.time)

class Blog(Model):
    __table__ = 'blogs'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    user_id = StringField(ddl='varchar(50)')
    user_name = StringField(ddl='varchar(50)')
    user_image = StringField(ddl='varchar(500)')
    name = StringField(ddl='varchar(50)')
    summary = StringField(ddl='varchar(200)')
    content = TextField()
    created_at = FloatField(default=time.time)

class Comment(Model):
    __table__ = 'comments'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    blog_id = StringField(ddl='varchar(50)')
    user_id = StringField(ddl='varchar(50)')
    user_name = StringField(ddl='varchar(50)')
    user_image = StringField(ddl='varchar(500)')
    content = TextField()
    created_at = FloatField(default=time.time)

# sql脚本文件
# -- schema.sql
#
# drop database if exists awesome;
#
# create database awesome;
#
# use awesome;
#
# grant select, insert, update, delete on awesome.* to 'www-data'@'localhost' identified by 'www-data';
#
# create table users (
#     `id` varchar(50) not null,
#     `email` varchar(50) not null,
#     `passwd` varchar(50) not null,
#     `admin` bool not null,
#     `name` varchar(50) not null,
#     `image` varchar(500) not null,
#     `created_at` real not null,
#     unique key `idx_email` (`email`),
#     key `idx_created_at` (`created_at`),
#     primary key (`id`)
# ) engine=innodb default charset=utf8;
#
# create table blogs (
#     `id` varchar(50) not null,
#     `user_id` varchar(50) not null,
#     `user_name` varchar(50) not null,
#     `user_image` varchar(500) not null,
#     `name` varchar(50) not null,
#     `summary` varchar(200) not null,
#     `content` mediumtext not null,
#     `created_at` real not null,
#     key `idx_created_at` (`created_at`),
#     primary key (`id`)
# ) engine=innodb default charset=utf8;
#
# create table comments (
#     `id` varchar(50) not null,
#     `blog_id` varchar(50) not null,
#     `user_id` varchar(50) not null,
#     `user_name` varchar(50) not null,
#     `user_image` varchar(500) not null,
#     `content` mediumtext not null,
#     `created_at` real not null,
#     key `idx_created_at` (`created_at`),
#     primary key (`id`)
# ) engine=innodb default charset=utf8;

# 编写数据访问代码

