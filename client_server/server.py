# -*- coding: utf-8 -*-
__author__ = 'QB'

import socket
import time
import threading


def tcplink(sock, addr):
    sock.send(b'Connecting...')
    print('Accept new connection from %s:%s...' % (addr))
    time.sleep(1)
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        # 如果客户端发送了bye字符串，就直接关闭连接
        if not data or data.decode('utf-8') == 'bye':
            break
        sock.send(('server> Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)


# 创建一个socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 监听端口
s.bind(('127.0.0.1', 10002))

# 开始监听端口，设置最大连接数量
s.listen(5)
print('Waiting for connection...')

# 客户端连接个数
count = 0
# 循环接收客户端的连接请求
while True:
    # 接收一个新连接
    sock, addr = s.accept()
    # 创建新线程来处理
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()
