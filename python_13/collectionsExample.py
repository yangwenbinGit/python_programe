# collections是Python内建的一个集合模块

from collections import namedtuple,deque,defaultdict
from collections import OrderedDict
from collections import ChainMap
import os,argparse
from  collections import Counter

Point = namedtuple('Point',['x','y'])
p = Point(1,2)
print(p.x)
print(p.y)

print(isinstance(p,Point))
print(isinstance(p,tuple))

# 如果要用坐标和半径表示一个圆，也可以用namedtuple定义
Cricle = namedtuple('Cricle',['x','y','z'])
c = Cricle(3,4,5)
print(c.x)
print(c.y)
print(c.z)

# deque
# 使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为list是线性存储，数据量大的时候，插入和删除效率很低
# deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈
q = deque(['a','b','c'])
q.append('x') # 在末尾进行插入元素
q.appendleft('y')  # 在首位进行元素的插入
print(q)
q.popleft()  # 删除最左边(头部)的一个元素
print(q)
q.pop()
print(q)   # 从尾部删除一个元素

# defaultdict
# 使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict
# 在defaultdict中的参数是如果dict中的key不存在，如果要获取的时候默认打印的内容
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print(dd['key1'])  # key1存在 正常的打印abc
print(dd['key2'])  # 如果key2不存在的话，就会打印出N/A,而不是和之前一样报错

# OrderedDict
# 使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。如果要保持Key的顺序，可以用OrderedDict
d = {'Michael':88,'Bob':95,'Tracy':85}
print(d['Michael'])

# 还有一种定义的方法是这样的
d = dict([('Michael',88),('Bob',95),('March',100)])
print(d['Bob'])

# 如果要保持Key的顺序，可以用OrderedDict： 放进去的和取出来的是一样的
# OrderedDict的Key会按照插入的顺序排列，不是Key本身排序
od = OrderedDict([('a',1),('b',2),('c',3)])
print(od)

# OrderedDict可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key：
class LastUpdatedOrderedDict(OrderedDict):

    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:', last)
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)

# ChainMap
# 应用程序往往都需要传入参数  我们可以用ChainMap实现参数的优先级查找，即先查命令行参数，如果没有传入，再查环境变量，如果没有，就使用默认参数
# 构造缺省参数：
defaults = {
    'color' : 'red',
    'user' : 'guest'
}

# 构造命令行参数:
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')
namespace = parser.parse_args()
command_line_args = { k: v for k, v in vars(namespace).items() if v }

# 组合成ChainMap:
combined = ChainMap(command_line_args, os.environ, defaults)

# 打印参数:
print('color=%s' % combined['color'])
print('user=%s' % combined['user'])

# Counter
# Counter是一个简单的计数器，例如，统计字符出现的个数：
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] +1
print(c)

# Counter({'r': 2, 'g': 2, 'm': 2, 'p': 1, 'o': 1, 'a': 1, 'i': 1, 'n': 1})










