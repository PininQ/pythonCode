# -*- coding: utf-8 -*-
__author__ = 'QB'
'''
一对一的生产者消费者 Demo
'''

# 消费者
def consumer():
    r = ""
    print("开始消费...")
    while True:
        n = yield r
        if not n:
            return
        print("【消费者】消费了{}".format(n))
        r = "OK"


# 生产者
def produce(csm):
    print("开始生产...")
    csm.send(None)
    n = 0
    while n < 5:
        n += 1
        print("【生产者】生产了{}".format(n))
        r = csm.send(n)
        print("【生产者】消费者返回了{}".format(r))
    csm.close()


if __name__ == '__main__':
    c = consumer()
    produce(c)
