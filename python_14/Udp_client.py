# UDP连接客户端
# TCP是建立的可靠连接,双方通信都是以流的方式发送数据,例如我们的文件传输
# UDP建立的是不可靠连接,他也可以时断时续,可以不是一直连续的,例如我们的微信电话和视频
# 使用UDP协议时，不需要建立连接，只需要知道对方的IP地址和端口号，就可以直接发数据包。但是，能不能到达就不知道了,UDP的传输速度要比TCP快

import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
for data in [b'Michael',b'Tracy',b'Sarah',b'Yangwenbin',b'Wangrui']:
    # 发送数据
    s.sendto(data,('127.0.0.1',9999))
    # 从服务器接收数据
    print(s.recv(1024).decode('utf-8'))

s.close()

# UDP的使用与TCP类似，但是不需要建立连接。此外，服务器绑定UDP端口和TCP端口互不冲突，也就是说，UDP的9999端口与TCP的9999端口可以各自绑定