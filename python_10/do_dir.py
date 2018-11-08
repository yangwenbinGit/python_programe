# 操作文件
# 进行小文件的读写
# 01.都打开文件,读取文件是以读,写的话要加w
read = open('test.txt','r',encoding='UTF-8')
write = open('copy_test.txt','w')
# 02.开始读取 然后写入
text = read.read()
write.write(text)
# 03.关闭读取和写入
read.close()
write.close()


# 进行大文件的读写操作 逐行读取并且写入
read = open('test.txt','r',encoding='UTF-8')
write = open('big_copy_test.txt','w',encoding='UTF-8')

while True:
    text =read.readline()

    if text == '':
        break

    write.write(text)

read.close()
write.close()

import os
# 获取操作系统的类型  如果是nt就是windows系统 如果是posix就是Linux Unix Mac os
print(os.name)

# 要获取详细的系统信息，可以调用uname()函数
# 注意uname()函数在Windows上不提供支持,调用的话会报错,也就是说，os模块的某些函数是跟操作系统相关的。
# print(os.uname())

# 环境变量
# 在操作系统中定义的环境变量，全部保存在os.environ这个变量中，可以直接查看
print(os.environ)

# 要获取某个环境变量的值，可以调用os.environ.get('key')：
print(os.environ.get('path'))

# 操作文件和目录
# 查看当前目录的绝对路径: D:\developeCode\pythonCode\python_10
print(os.path.abspath('.'))
# 将两个路径合并成一个，首先把新目录的完整路径表示出来: D:\developeCode\pythonCode\python_10\testdir
print(os.path.join('D:\developeCode\pythonCode\python_10','testdir'))
# 然后创建一个目录:
os.mkdir('D:\developeCode\pythonCode\python_10\\testdir')
# 删除一个目录
os.rmdir('D:\developeCode\pythonCode\python_10\\testdir')
# 拆分路径 ('/Users/michael/testdir', 'file.txt')
print(os.path.split('/Users/michael/testdir/file.txt'))
# os.path.splitext()可以直接让你得到文件扩展名  ('/path/to/file', '.txt')
print(os.path.splitext('/path/to/file.txt'))

# 对文件进行重命名
os.rename('big_copy_test.txt','rename_copy_test.txt')
# 删除文件
os.remove('rename_copy_test.txt')

# 我们要列出当前目录下的所有目录/文件
print( [x for x in os.listdir('.') if os.path.isdir(x)])
print( [x for x in os.listdir('.') if os.path.isfile(x)])

# 要列出所有的.py文件
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])
