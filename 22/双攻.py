#!/usr/bin/python3
# -*- coding : utf-8 -*-
# File   : 双攻.py
# Author : cjz
# Date  : 2019-03-01 11:22
import socket

def send(udp_socket):
    dest_ip = input('请输入对方ip')
    dest_port = int(input('请输入对方端口'))
    send_data = input("请输入内容")

    udp_socket.sendto(send_data.encode('utf-8'), dest_ip, dest_port)

def recv(udp_socket):
        data = udp_socket.recvfrom(1024)
        print("%s:%s" % (str(data[1]), data[0].decode('utf-8')))

def main():
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    udp_socket.bind(1024)
    while True:
        send(udp_socket)
        recv(udp_socket)

    udp_socket.close()

if __name__ =='__main__':
    main()