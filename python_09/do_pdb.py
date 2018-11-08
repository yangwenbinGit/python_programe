# 第4种方式是启动Python的调试器pdb，让程序以单步方式运行，可以随时查看运行状态。我们先准备好程序
import pdb
s ='0'
n =int(s)
pdb.set_trace()  # 运行到这里会自动暂停 这就好比是一个断点的东西
print(10 / n)

# 运行代码，程序会自动在pdb.set_trace()暂停并进入pdb调试环境，可以用命令p查看变量，或者用命令c继续运行
# 效果如下所示：
# D:\developeCode\pythonCode\venv\Scripts\python.exe D:/developeCode/pythonCode/python_09/do_pdb.py
# > d:\developecode\pythoncode\python_09\do_pdb.py(6)<module>()
# -> print(10 / n)
# (Pdb) p n   查看n的值
# 0
# (Pdb) c      c是继续往下执行
# Traceback (most recent call last):
#   File "D:/developeCode/pythonCode/python_09/do_pdb.py", line 6, in <module>
#     print(10 / n)
# ZeroDivisionError: division by zero

# 这个的效率也是很低,还不如pychame自带的debug调试器