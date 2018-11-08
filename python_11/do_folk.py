# 多进程
import os
# 下面的代码在Windows上无法运行
# 有了fork调用，一个进程在接到新任务时就可以复制出一个子进程来处理新任务，常见的Apache服务器就是由父进程监听端口，每当有新的http请求时，就fork出子进程来处理新的http请求。
# 但是fork()调用一次，返回两次 第一次是fork出来的是父进程,第二次才是返回的子进程 子进程永远返回0,而父进程返回子进程的ID。
print('Process (%s) start...' %os.getpgid())
# only works on Unix/linux/Mac
pid = os.fork()
if pid ==0:
    print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
else:
    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))

# Process (876) start...
# I (876) just created a child process (877).
# I am child process (877) and my parent is 876.

