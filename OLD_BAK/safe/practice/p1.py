#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: zhouey
@file: p1.py
@time: 2020/8/20 10:12
"""
import socket
import threading


def tcp_client_test():
    host = '127.0.0.1'
    port = 9999
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client.connect((host, port))

    # client.send("get / HTTP/1.1\r\n Host:baidu.com\r\n\r\n".encode('utf-8'))
    client.send("www.qq.com".encode('utf-8'))

    res = client.recv(4096)

    print(res)


def udp_client_test():
    host = '127.0.0.1'
    port = 80
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.sendto('aaabbbccc'.encode('utf-8'), (host, port))
    data, addr = client.recvfrom(4096)

    print(data)


def handle_client(client_socket):
    request = client_socket.recv(1024)
    print("[*] recevied {}".format(request))
    client_socket.send("ACK!".encode('utf-8'))
    client_socket.close()


def tcp_server_test():
    bind_ip = '0.0.0.0'
    bind_port = 9999
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((bind_ip, bind_port))
    server.listen(5)
    print("[*] listening on {}:{}".format(bind_ip, bind_port))

    while True:
        client, addr = server.accept()
        print("[*] accepted connection from {}:{}".format(addr[0], addr[1]))
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()


if __name__ == '__main__':
    tcp_client_test()
    # udp_client_test()
    # tcp_server_test()
    import os