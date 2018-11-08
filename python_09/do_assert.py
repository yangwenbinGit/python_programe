# 调试bug
# 第一种方法简单直接粗暴有效，就是用print()把可能有问题的变量打印出来看看
def foo(s):
    n = int(s)
    print('>>> n = %d' % n)
    return 10 / n

def main():
    foo('0')

# main()

#断言
# 凡是用print()来辅助查看的地方，都可以用断言（assert）来替代：
def foo(s):
    n = int(s)
    assert n != 0,'n is zero!'
    return 10 /n

def main():
    foo('0')

# assert的意思是，表达式n != 0应该是True，否则，根据程序运行的逻辑，后面的代码肯定会出错。
# 如果断言失败，assert语句本身就会抛出AssertionError
# AssertionError: n is zero!
# assert n != 0,'n is zero!' 这句话的理解是如果n!=0的时候,就继续往下执行，如果等于了0 就抛出异常assert语句本身就会抛出AssertionError
main()



