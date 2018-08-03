# -*- coding: utf-8 -*-
__author__ = 'QB'

import socket
import time
import threading


def tcplink(count, sock, addr):
    print('接受第', count, '个连接请求：%s:%s...' % (addr))
    sock.send('连接成功!'.encode('utf-8'))
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('连接关闭：%s:%s' % addr)


# 创建一个socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 监听端口
s.bind(('127.0.0.1', 10002))

# 开始监听端口，设置最大连接数量
s.listen(5)
print('等待连接...')

# 客户端连接个数
count = 0
# 循环接收客户端的连接请求
while True:
    count += 1
    # 接收一个新连接
    sock, addr = s.accept()
    # 创建新线程来处理
    t = threading.Thread(target=tcplink, args=(count, sock, addr))
    t.start()
