#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: zhouey
@file: argparse_test.py
@time: 2020/10/14 17:20
"""
import argparse


def main():
    support_pro_list = ['SSH', 'RDP', 'TELNET', 'VNC', 'SFTP']
    parser = argparse.ArgumentParser()
    parser.add_argument('-P', metavar='<protocol name>', help='协议类型 SSH/VNC/TELNET/SFTP/RDP', type=str, )
    parser.add_argument('-e', metavar='<tcptun port>', help='启动tcptun隧道', type=str, )
    parser.add_argument('--host', metavar='<usm_ip>', help='堡垒机地址: --host 10.0.20.1', type=str, )

    parser.add_argument('--num', metavar='<number>', help='线程发起数，不指定默认为1', type=str, )
    parser.add_argument('--con', metavar='<number>', help='并发数，不指定默认为 1', type=str, )

    parser.add_argument('--cmd', metavar='<cmd_list>', help='ssh telnet 命令字符串 "ls -l,top" ', type=str, )
    parser.add_argument('--config', metavar='<config_file>', help='通过配置文件执行', type=str, )

    parser.add_argument('--a_ip', metavar='<account ip>', help='资产 ip', type=str, )
    parser.add_argument('--a_name', metavar='<account name>', help='资产名', type=str, )
    parser.add_argument('--a_pwd', metavar='<account passwd>', help='资产密码', type=str, )
    parser.add_argument('--a_port', metavar='<account port>', help='资产协议端口', type=str, )
    parser.add_argument('--access_token', metavar='<access token>', help='运维api键访问键token', type=str, )

    parser.add_argument('--file', metavar='<sftp upload file>', help='SFTP 协议上传文件', type=str, )

    parser.add_argument('--ops_user', metavar='', help='运维账号用于登录堡垒机的用户名 <rdp需要>', type=str, )
    parser.add_argument('--cs_port', metavar='', help='cs 运维端口<rdp需要>', type=str, )

    args = parser.parse_args()
    print(args.P)

    if not args.P:
        print('请指定协议类型...')
        exit(-1)

    if args.P.upper() not in support_pro_list:
        print('该脚本不支持 <{}> 协议'.format(args.P))
        exit(-1)

    pro_name =args.P.upper()
    print(pro_name)

    if args.num:
        thread_num = args.num
    else:
        thread_num = 1

    if args.con:
        con = args.con
    else:
        con = 1

    if not args.host:
        print('请指定usm ip ....')
        exit(-1)
    else:
        usm_ip =args.host

    print(usm_ip)

    print(thread_num,con)

    if args.cmd:
        cmd_list = args.cmd.split(',')
    else:
        cmd_list = ['top']

    # print(cmd_list)


if __name__ == '__main__':
    main()
