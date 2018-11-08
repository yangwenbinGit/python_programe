# BytesIO
# StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO
# BytesIO实现了在内存中读写bytes，我们创建一个BytesIO，然后写入一些bytes：

from io import BytesIO
f = BytesIO()
f.write('中文'.encode('utf-8'))  # 写入的不是str，而是经过UTF-8编码的bytes
print(f.getvalue())

# b'\xe4\xb8\xad\xe6\x96\x87' 进过了UTF-8进行编码后得到的字节存到了内存中

f =BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f.read())

# StringIO和BytesIO是在内存中操作str和bytes的方法，使得和读写文件具有一致的接口