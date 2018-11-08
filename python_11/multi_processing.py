# multiprocessing模块提供了一个Process类来代表一个进程对象，下面的例子演示了启动一个子进程并等待其结束：
from multiprocessing import Process
import os

# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    # 创建一个进程的实例 传入一个函数和函数的参数
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    # 启动一个进程
    p.start()
    # 等待子进程结束后 主进程在继续往下运行
    p.join()
    print('Child process end.')

# 创建子进程的时候，只要传入一个执行函数和函数的参数,创建一个process实例
# 用start()方法启动，要比fork简单
# join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步

# Parent process 44944.
# Child process will start.
# Run child process test (41060)...
# Child process end.