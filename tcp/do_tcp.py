# -*- coding: utf-8 -*-
__author__ = 'QB'

import socket
'''
TCP编程
'''
# 创建一个socket（AF_INET指定使用IPv4协议，SOCK_STREAM指定使用面向流的TCP协议）
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 建立连接（建立TCP连接）:
s.connect(('mamicode.com', 80))

# 发送数据（向新浪服务器发送GET请求，请求返回首页的内容，并关闭连接）:
s.send(b'GET / HTTP/1.1\r\nHost: mamicode.com\r\nConnection: close\r\n\r\n')

# 接收数据
buffer = []
# 在while循环中反复接收，直到recv()返回空数据，表示接收完毕，退出循环
while True:
    # 每次最多接收1k字数据
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break

data = b''.join(buffer)

# 关闭连接
s.close()

header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))

# 把接收的数据写入文件
with open('mamicode.html', 'wb') as f:
    f.write(html)