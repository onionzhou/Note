#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: zhouey
@file: tcp_proxy.py
@time: 2020/8/20 11:17
"""
import sys
import socket
import threading


def server_loop(local_host, local_port, remote_host, remote_port, receive_first):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server.bind((local_host, local_port))
    except:
        print("[!!] Failed to listen on {}:{}".format(local_host, local_port))
        sys.exit(0)

    print("[*] listen on {}:{}".format(local_host, local_port))

    server.listen(5)

    while True:
        # 本地连接信息
        client_socket, addr = server.accept()
        print("[===>] Received incoming connection from {}:{}".format(addr[0], addr[1]))

        # 开启一个线程与远程主机通信
        proxy_thread = threading.Thread(target=proxy_handler,
                                        args=(client_socket, remote_host, remote_port, receive_first))

        proxy_thread.start()


def receive_from(con):
    pass


def hexdump(src, length=16):
    result = []
    digits = 4 if isinstance(src, unicode) else 2


def response_handler(data):
    pass


def proxy_handler(client_socket, remote_host, remote_port, receive_first):
    remote_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    remote_socket.connect((remote_host, remote_port))

    # 从远程主机接收数据
    if receive_first:
        remote_buffer = receive_from(remote_socket)
        hexdump(remote_buffer)

        remote_buffer = response_handler(remote_buffer)

        if len(remote_buffer):
            print("[<===] sending {} bytes to localhost.".format(len(remote_buffer)))
            client_socket.send(remote_buffer.encode('utf-8'))
    # 从本地循环读取数据，发送给远程主机和本地主机
    while True:

        local_buffer = receive_from(client_socket)
        if len(local_buffer):
            print('[==>] Received {} bytes  from localhost '.format(len(local_buffer)))
            hexdump(local_buff)
            # 发送给我们的本地请求
            local_buff = request_handler(local_buffer)

            # 向远程主机发送数据
            remote_socket.send(local_buffer)
            print("[==>] sent to remote ")

        #
        remote_buffer = receive_from(remote_socket)

        if len(remote_buffer):
            print('[<==] received {} byte from remote.'.format(len(remote_buffer)))
            hexdump(remote_buffer)

            remote_buff = response_handler(remote_buffer)

            # 将响应发送给本地socket
            client_socket.send(remote_buffer)
            print("[<==] sent to localhost")

        if not len(local_buffer) or not len(remote_buffer):
            client_socket.close()
            remote_socket.close()
            print('[*] no more data ,closing connections')
            break


def main():
    if len(sys.argv[1:]) != 5:
        print("Usage: ./tcp_proxy.py [localhost] [localport] [remotehost] [remoteport] [receive_first]")
        print("example: ./tcp_proxy.py 127.0.0.1 9000 10.0.80.1 9000 True")
        sys.exit(0)

    local_host = sys.argv[1]
    local_port = sys.argv[2]

    remote_host = sys.argv[3]
    remote_port = sys.argv[4]

    receive_first = sys.argv[5]

    if "True" in receive_first:
        receive_first = True
    else:
        receive_first = False

    server_loop(local_host, local_port, remote_host, remote_port, receive_first)


if __name__ == '__main__':
    main()
