# 基于TCP/IP协议的编程
import socket

# 编写客户端   创建一个socket
# 创建socket的时候,AF_INET指的是IPV4协议，如果要使用更先进的IPV6，就指定AF_INET6
# SOCK_STREAM指定使用面向流的TCP协议,这样一个socket对象就创建成功
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 建立连接,客户端要主动发起TCP连接，必须知道服务器的IP地址和端口号
# 注意参数是一个tuple(元组)，包含地址和端口号。
s.connect(('www.sina.com.cn', 80))

# 建立TCP连接后，我们就可以向新浪服务器发送请求，要求返回首页的内容
# 发送的文本格式必须符合HTTP标准,如果格式没有问题,就接收新浪服务器的返回数据了
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')


# 发送完成后就可以接收新浪服务器返回的数据了
# 接收数据时，调用recv(max)方法，一次最多接收指定的字节数，因此，在一个while循环中反复接收，直到recv()返回空数据，表示接收完毕，退出循环
buffer = []
while True:
    # 每次最多接收1K字节
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)

# 关闭连接
s.close()

# 接收到的数据包括HTTP头和网页本身，我们只需要把HTTP头和网页分离一下，把HTTP头打印出来，网页内容保存到文件
# \r\n 表示的是换行和回车这样进行分割,分割成2部分
header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
# 把接收的数据写入文件:
with open('sina.html', 'wb') as f:
    f.write(html)


print(100 * '===')
# 连接建立后，服务器首先发一条欢迎消息，然后等待客户端数据，并加上Hello再发送给客户端。如果客户端发送了exit字符串，就直接关闭连接。
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.connect(('127.0.0.1', 9999))
# 接收欢迎消息:
print(s.recv(1024).decode('utf-8'))
for data in [b'Michael', b'Tracy', b'Sarah']:
    # 发送数据:
    s.send(data)
    print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()