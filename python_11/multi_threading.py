# 多线程
# 在多线程中提供了两个模块_thread和threading,_thread是低级模块，threading是高级模块
# 平时在使用的话我们要使用的是threading这个高级模块

# 启动一个线程就是把一个函数传入并创建Thread实例,并调用start()开始执行
import time,threading

# 新线程执行的代码：
def loop():
    print('thread %s is runnning...'% threading.current_thread().name)
    n =0
    while n<5:
        n = n+1
        print('thread %s>>> %s'%(threading.current_thread().name,n))
        time.sleep(1)
    print('thread %s is running...'%threading.current_thread().name)


print('thread %s is runnning...' % threading.current_thread().name)
t = threading.Thread(target=loop,name='LoopThread')
t.start()
t.join()   # 等他先执行完成  主线程在执行
print('thread %s is end...'%threading.current_thread().name)

# thread MainThread is runnning...
# thread LoopThread is runnning...
# thread LoopThread>>> 1
# thread LoopThread>>> 2
# thread LoopThread>>> 3
# thread LoopThread>>> 4
# thread LoopThread>>> 5
# thread LoopThread is running...
# thread MainThread is end...

# 任何的进程默认会启动一个线程,我们把该线程称为主线程,主线程又可以启动新的线程
# Python的threading模块有个current_thread()函数，它永远返回当前线程的实例。主线程实例的名字叫MainThread，子线程的名字在创建时指定，我们用LoopThread命名子线程。名字仅仅在打印时用来显示，完全没有其他意义，如果不起名字Python就自动给线程命名为Thread-1，Thread-2……


# 在写一个多线程的例子，比如说一个人在唱歌的时候也在跳舞
def single():
    print('唱歌开始....')
    for x in range(5):
        print('---正在唱--菊花台---single',x)
        time.sleep(1)


def dance():
    print('跳舞开始....')
    for x in range(5):
        print('---正在跳舞---dance',x)
        time.sleep(1)


def main():
    # 这样写的话肯定是按照顺序执行 先执行完唱歌后执行跳舞
    # single()
    # dance()

    # 我们想要一边唱歌一边跳舞的效果
    t1 = threading.Thread(target=single)
    t2 = threading.Thread(target=dance)
    t1.start()
    t2.start()


if __name__ == '__main__':
    main()


