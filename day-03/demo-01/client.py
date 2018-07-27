# -*- coding: utf-8 -*-
__author__ = 'QB'

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.connect(('127.0.0.1', 10002))

# 接收成功连接消息:
print('小服务器说===========', s.recv(1024).decode('utf-8'))
# for data in [b'Michael', b'Tracy', b'Sarah']:
#     # 发送数据:
#     s.send(data)
#     print('Server Say===========', s.recv(1024).decode('utf-8'))
# s.send(b'exit')
# s.close()

while True:
    # 输入消息
    sendData = input("发送的消息：")
    # 发送数据:
    s.send(sendData.encode('utf-8'))
    print('小服务器说===========', s.recv(1024).decode('utf-8'))
    if sendData == 'exit':
        s.send(b'exit')
        s.close()
print('exit!')
