# Lock
# 多线程和多进程最大的不同在于,多进程中,对于同一个变量会拷贝一份放在自己的进程中。
# 而多线程中就是所有的线程对于同一个变量都是共享的，每一个线程都可以改变这个变量的值，线程之间数据共享最大的危险是就是多个线程同时修改一个变量，把内容给该乱了。
# 看看多个线程同时操作一个变量怎么把内容给改乱了

import time,threading,multiprocessing

# 假定这个是银行的存款
balabce = 0
lock = threading.Lock()

def change_it(n):
    global balabce
    balabce = balabce + n
    print('当前进程是:%s,当前money：%s,当前n:%s,+' % (threading.current_thread().name, balabce, n))
    time.sleep(1)
    balabce = balabce - n
    print('当前进程是:%s,当前money：%s,当前n:%s,-' % (threading.current_thread().name, balabce, n))

# 这是线程不安全的
# def run_thread(n):
#     for i in range(100):
#         change_it(n)

# 多个线程共同操作一个变量的话 要加锁
def run_thread(n):
    for i in range(100):
        # 要先获取到锁
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()


t1 = threading.Thread(target=run_thread,args=(5,),name='t1')
t2 = threading.Thread(target=run_thread,args=(8,),name='t2')
t1.start()
t2.start()
t1.join()
t2.join()
print(balabce)


# 上面的代码如果不加一个time.sleep(1) 是看不到效果的
# 究其原因,因为修改balancex需要多条语句,而执行这多条语句的时候，由于线程之间会涉及到抢占CPU的情况,从而导致多个线程在抢占执行的时候把同一个对象内容改乱了

# 如果我们要确保balance计算正确，就要给change_it()上一把锁，当某个线程开始执行change_it()时，我们说，该线程因为获得了锁，因此其他线程不能同时执行change_it()，只能等待，直到锁被释放后，获得该锁以后才能改。由于锁只有一个，无论多少线程，同一时刻最多只有一个线程持有该锁，所以，不会造成修改的冲突。创建一个锁就是通过threading.Lock()来实现

# 当多个线程同时执行lock.acquire()时,只有一个线程能成功的获取锁,然后继续执行代码,其他线程就继续等待直到获得锁为止。
# 获取到锁的线程,在使用完成后一定要释放锁，否则那些苦苦等待的线程将永远的等待下去，成为死线程，所以用try...finally来确保锁一定会被释放
# 锁的好处就是确保了某段关键代码只能由一个线程从头到尾完整地执行，坏处当然也很多，首先是阻止了多线程并发执行，包含锁的某段代码实际上只能以单线程模式执行，效率就大大地下降了。其次，由于可以存在多个锁，不同的线程持有不同的锁，并试图获取对方持有的锁时，可能会造成死锁，导致多个线程全部挂起，既不能执行，也无法结束，只能靠操作系统强制终止。

# 下面是一段死循环的代码
# 启动与CPU核心数量相同的N个线程，在4核CPU上可以监控到CPU占用率仅有102%，也就是仅使用了一核。
def loop():
    x = 0
    while True:
        x = x^1


for i in range(multiprocessing.cpu_count()):
    t = threading.Thread(target=loop,name='t'+str(i))
    t.start()

# 但是用C、C++或Java来改写相同的死循环，直接可以把全部核心跑满，4核就跑到400%，8核就跑到800%，为什么Python不行呢？
# 因为Python的线程虽然是真正的线程，但解释器执行代码时，有一个GIL锁：Global Interpreter Lock，任何Python线程执行前，必须先获得GIL锁，然后，每执行100条字节码，解释器就自动释放GIL锁，让别的线程有机会执行。这个GIL全局锁实际上把所有线程的执行代码都给上了锁，所以，多线程在Python中只能交替执行，即使100个线程跑在100核CPU上，也只能用到1个核。
# GIL是Python解释器设计的历史遗留问题，通常我们用的解释器是官方实现的CPython，要真正利用多核，除非重写一个不带GIL的解释器。
# 所以，在Python中，可以使用多线程，但不要指望能有效利用多核。如果一定要通过多线程利用多核，那只能通过C扩展来实现，不过这样就失去了Python简单易用的特点。
# 不过，也不用过于担心，Python虽然不能利用多线程实现多核任务，但可以通过多进程实现多核任务。多个Python进程有各自独立的GIL锁，互不影响。