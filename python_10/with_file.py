# 文件读写
# 读文件 要以读文件的模式打开一个文件对象，使用Python内置的open()函数，传入文件名和标示符
# 标示符'r'表示读，这样，我们就成功地打开了一个文件，需要注意的是r是表示只读的方式打开
# 'r'也可以省略,如果不写的话默认的是就是只读方式
# 如果文件不存在就会抛出IOError的错误

f = open('test.txt', 'r')
# 调用read方法就可以把文本中的内容全部读入到内存,用一个字符串str表示
print(f.read())
# 最后是使用完毕以后要调用close()方法关闭文件。不然会很占用系统资源
f.close()

# 由于读写文件的时候如果读取的文件不存在的时候会抛出异常的情况
# 所以我们用try..except..finally的方式
print('=' * 100)
try:
    f = open('test.txt')
    print(f.read())
except:
    raise ValueError('your file is not exist!')
finally:
    f.close()

# 每次像上面那样的写有点太繁琐，Python引入了with语句来自动帮我们调用close()方法
print('=' * 100)
with open('test.txt', 'r') as f:
    print(f.read())

# 调用read()会一次性读取文件的全部内容，如果文件有10G，内存就爆了，所以，要保险起见，可以反复调用read(size)方法，每次最多读取size个字节的内容。另外，调用readline()可以每次读取一行内容，调用readlines()一次读取所有内容并按行返回list。因此，要根据需要决定怎么调用
# 如果文件很小，read()一次性读取最方便；如果不能确定文件大小，反复调用read(size)比较保险；如果是配置文件，调用readlines()最方便
print('=' * 100)
with open('test.txt', 'r') as f:
    while True:
        text = f.readline()

        if not text:
            break  # text为空的时候就退出

        print(text.strip())  # 去掉末尾的\n

# 读取二进制文件 例如读取图片和视频文件，用'rb'模式打开文件即可
print('=' * 100)
f = open('LYF.jpg', 'rb')
print(f.read())
f.close()

# 要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数 读取GBK编码的文件
print('=' * 100)
f = open('test.txt', encoding='gbk')
print(f.read())
f.close()

# open()函数还接收一个errors参数，表示如果遇到编码错误后如何处理。最简单的方式是直接忽略
f = open('test.txt', encoding='gbk', errors='ignore')
f.close()

# 写文件
# 写文件的时候如果出现了乱码的时候 就加上encoding ='UTF-8'
f = open('write.txt','w',encoding='UTF-8')
f.write('2018-10-30号伟大的金庸先生去世,享年94岁')
f.close()

# 另外一种写法
with open('write.txt','w',encoding='UTF-8') as f:
    f.write('Hello,World')

# 上面的问题我们就会发现，每次写入进去都是覆盖了之前的内容，如果想要追加该怎么做
with open('write.txt','a',encoding='UTF-8') as f:
    f.write('\n My name is Yangwenbin!!')