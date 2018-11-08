# TCP服务端的开发
import  socket
import threading
import time

# 创建一个基础IPV4的TCP协议的socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 监听端口,这个里面的参数是一个元组,里面有两个参数
s.bind(('127.0.0.1',9999))
# 调用listen()方法开始监听端口,传入的参数指定等待连接的最大数量
s.listen(5)
print('Waiting for connection...')


# 每一个连接必须创建新的线程来处理,单线程的话无法处理多个客户端的请求连接
def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    # 这个关闭是当前线程创建的socket关闭了,但是主程序还是在运行的
    sock.close()
    print('Connection from %s:%s closed.' % addr)

# 服务器程序通过一个永久的循环接收来自客户端的连接，accept()会等待并返回一个客户端连接
# 服务端是不会关闭的,他会一直开着，除非我们自己关闭
while True:
    # 接受一个新连接:
    sock, addr = s.accept()
    # 创建新的线程来处理TCP连接：
    t =threading.Thread(target=tcplink,args=(sock,addr))
    t.start()


