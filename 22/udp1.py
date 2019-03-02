#!/usr/bin/python3
# -*- coding : utf-8 -*-
# File   : udp1.py
# Author : cjz
# Date  : 2019-03-01 10:28
import socket
def main():
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    local_addr = ('ip',8080)
    #s.bind(local_addr)  绑定端口号

    recv_data = s.recvfrom(1024)
    #print("%s:%s" % (str(send_addr),recv_data.decode(utf-8))
    #从键盘获取
    while True:
        send_data = input('请输入')
        if send_data =="exit":
            break
        #s .sendto(send_data.encode('utf-8'),("ip",port))
    s.close()

if __name__ =="__main__":
    main()


#1.创建套接字  s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#2.绑定端口 s.bind("192.168.9.9",8080):::自己电脑的ip和port
#3.接受输入数据 recv_data = s.recvfrom(1024)
#4.输出打印接收到的数据print()
#5.关闭套接字s.close()

#创建套接字，发送，关闭