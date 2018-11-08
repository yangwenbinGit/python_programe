# ThreadLocal
# 我们在编写多线程程序的时候，往往会遇到两种类型的变量。
# 一种是全局变量，多个线程共享。为了避免改乱为，我们在前面已经提到说要加锁。
# 一种是局部变量。仅供一个线程使用，线程间相互不影响。

# 下面我们举一个局部变量的例子，使用多线程处理
import threading


# def task():
#     count = 0
#     for i in range(10000):
#         count += 1
#         print(count)
#
#
# if __name__ == '__main__':
#     t1 = threading.Thread(target=task,name='t1')
#     t2 = threading.Thread(target=task,name='t2')
#     t1.start()
#     t2.start()


# 有没有一种方法，能让我们在线程中定义一个变量后，那么这个线程中的函数就都能调用
# Python为我们做到了，那就是ThreadLocal.
# ThreadLocal的用法只需要三步
#     定义一个对象  threading.local
#
#     在线程内给该对象绑定参数。所有绑定的参数都是线程隔离的。
#
#     在线程内调用

# 请看下面的一段代码
# print(100*'==')
# local = threading.local() # 创建一个全局的对象
#
#
# def task():
#     local.count = 0  # 初始化一个线程内变量，该变量线程间互不影响。
#     for i in range(1000):
#         count_plus()
#
#
# def count_plus():
#     local.count += 1
#     print(threading.current_thread().name, local.count)
#
#
# if __name__ == '__main__':
#     t1 = threading.Thread(target=task,name='t1')
#     t1.start()
#     t2 = threading.Thread(target=task,name='t2')
#     t2.start()


# 创建全局ThreadLocal对象:
local_school = threading.local()

def process_student():
    # 获取当前线程关联的student:
    std = local_school.student
    for i in range(100):
        print('Hello, %s (in %s) %s' % (std, threading.current_thread().name,i))

def process_thread(name):
    # 绑定ThreadLocal的student:
    local_school.student = name
    process_student()


t1 = threading.Thread(target= process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target= process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()

# 从执行结果看到,线程A和线程B都分别执行了100次，他们相互交替执行，各自在各自的线程内互不影响
# 全局变量local_school就是一个ThreadLocal对象,每一个Thread对它都可以读写student属性，但是彼此互不影响
# 你可以把local_school看成全局变量，但每个属性如local_school.student都是线程的局部变量，可以任意读写而互不干扰，也不用管理锁的问题，ThreadLocal内部会处理。
# 可以理解为全局变量local_school是一个dict，不但可以用local_school.student，还可以绑定其他变量，如local_school.teacher等等

# 一个ThreadLocal变量虽然是全局变量，但每个线程都只能读写自己线程的独立副本，互不干扰。ThreadLocal解决了参数在一个线程中各个函数之间互相传递的问题
