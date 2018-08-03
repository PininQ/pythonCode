# -*- coding: utf-8 -*-
__author__ = 'QB'

import socket
import time

# step 1：创建socket套接字（AF_INET指定使用IPv4协议，SOCK_STREAM指定使用面向流的TCP协议）
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# step 2：与服务端建立连接
s.connect(('127.0.0.1', 10002))

# 服务端返回连接成功消息，recv(1024)限制接收的数据大小为 1KB
print('server> ', s.recv(1024).decode('utf-8'))
time.sleep(1)
while True:
    # step 3：发送消息
    send_data = input("client> ")
    # 如果客户端输入了bye，退出循环，关闭与服务端的连接
    if send_data != 'bye':
        # 如果没有输入,重新循环接收输入
        if len(send_data) == 0: continue
        # 向服务端发送数据
        s.send(send_data.encode('utf-8'))
        # step 4: 接收消息
        print(s.recv(1024).decode('utf-8'))
    else:
        # step 5: 关闭连接
        s.close()
        break
