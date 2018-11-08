# noinspection PyUnresolvedReferences
import orm
# noinspection PyUnresolvedReferences
from models import User,Blog,Comment
import asyncio

# 这里要注意如果外面用async修饰的话,里面不能用yield from 否则报错
# 这里的user='root' 这个key是user 必须和create_pool方法中的定义的参数是一样的
# 在保存数据的时候如果没有给默认值得，必须都给数据,否则插入报错
async def test(loop):

    await orm.create_pool(loop,user='root',password='password',db ='python')

    u = User(name='Test',email ='test@example.com',passwd='123456',image='about.blank')

    await u.save()

# 要运行协程，需要使用事件循环,这样才能成功的保存到数据库
if __name__ == '__main__':
        loop = asyncio.get_event_loop()
        loop.run_until_complete(test(loop))
        print('Test finished.')
        loop.close()