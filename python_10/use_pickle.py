# 序列化
# 在程序运行的过程中所有的变量都是在内存中
# pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件。或者用另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object
import pickle
d = dict(name ='bob',age =20,score =98)
print(pickle.dumps(d))

# 将对象序列化后，然后将序列化的结果保存到dump.txt中
# 看看写入的dump.txt文件，一堆乱七八糟的内容，这些都是Python保存的对象内部信息
f = open('dump.txt','wb')
pickle.dump(d,f)
f.close()

# 我们要把对象从磁盘读入到内存中,可以先把内容读入到一个bytes
# 然后用pickle.loads()方法反序列化出对象
f = open('dump.txt','rb')
d = pickle.load(f)  # 从文本中读取到内容，然后进行反序列化
f.close()
print(d)  # {'name': 'bob', 'age': 20, 'score': 98}


# 这里有一条要注意一下如果是往文件中写入二进制的字节码的时候,需要使用wb,如果是普通的字符的写入的时候就是w
# 如果要从文件中读取二进制的内容的时候，记得要使用rb,如果是简单的字符的话,就用r,如果读取二进制的文件的时候使用r就会报错
