# 为了编写单元测试，我们需要引入Python自带的unittest模块，编写mydict_test.py如下
import unittest

# 这个的意思就是从mydict.py这个文件中导入我们编写的Dict这个类,虽然报错但是不用管
from mydict import Dict

# 编写单元测试时，我们需要编写一个测试类，从unittest.TestCase继承。
class TestDict(unittest.TestCase):

    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)  # 断言函数返回的结果与1相等
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))
        print('test1.....')

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')
        print('test2.....')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')
        print('test3.....')


    # 通过d['empty']访问不存在的key时，断言会抛出KeyError
    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']
        print('test4.....')


    # 通过d.empty访问不存在的key时，我们期待抛出AttributeError
    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty
        print('test5.....')

    # 加上这个后就在每一个测试用例执行之前和之后都会执行一次
    def setUp(self):
        print('setUp....')

    def tearDown(self):
        print('tearDown...')


# 以test开头的方法就是测试方法，不以test开头的方法不被认为是测试方法，测试的时候不会被执行
# 对每一类测试都需要编写一个test_xxx()方法。由于unittest.TestCase提供了很多内置的条件判断，我们只需要调用这些方法就可以断言输出是否是我们所期望的。最常用的断言就是assertEqual()：
# self.assertEqual(abs(-1), 1) # 断言函数返回的结果与1相等
# 另一种重要的断言就是期待抛出指定类型的Error，比如通过d['empty']访问不存在的key时，断言会抛出KeyError

# 运行单元测试
# 一旦编写好单元测试，我们就可以运行单元测试。最简单的运行方式是在mydict_test.py的最后加上两行代码：
#
# if __name__ == '__main__':
#     unittest.main()
# 这样就可以把mydict_test.py当做正常的python脚本运行：
#
# $ python mydict_test.py
# 另一种方法是在命令行通过参数-m unittest直接运行单元测试：
#
# $ python -m unittest mydict_test
# .....
# ----------------------------------------------------------------------
# Ran 5 tests in 0.000s
#
# OK

# 我使用的是第一种
if __name__ == '__main__':
    unittest.main()

# 测试结果 代表通过
# .....
# ----------------------------------------------------------------------
# Ran 5 tests in 0.001s
# OK

# setUp与tearDown

# 可以在单元测试中编写两个特殊的setUp()和tearDown()方法。这两个方法会分别在每调用一个测试方法的前后分别被执行。
# setUp()和tearDown()方法有什么用呢？设想你的测试需要启动一个数据库，这时，就可以在setUp()方法中连接数据库，在tearDown()方法中关闭数据库，这样，不必在每个测试方法中重复相同的代码：
# 执行结果如下：
# .....
# ----------------------------------------------------------------------
# Ran 5 tests in 0.000s
#
# OK
# setUp....
# test3.....
# tearDown...
# setUp....
# test5.....
# tearDown...
# setUp....
# test1.....
# tearDown...
# setUp....
# test2.....
# tearDown...
# setUp....
# test4.....
# tearDown...