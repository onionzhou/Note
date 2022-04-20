#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: zhouey
@file: sensor1.py
@time: 2022/4/20 10:30
# 温湿度传感器使用
"""
import RPi.GPIO as GPIO

import time

CHANNEL = 4  # 传感器输出口接BCM模式 GPIO4


def mode_init():
    GPIO.setmode(GPIO.BCM)
    time.sleep(1)
    # / *MCU向DCT发射启动信号 * /
    GPIO.setup(CHANNEL, GPIO.OUT)
    GPIO.output(CHANNEL, GPIO.LOW)  # 数据总线空闲状态为高电平，通信开始时，将电平拉低
    time.sleep(0.02)  # 此过程至少需要18ms才能确保DHT检测到MCU信号
    GPIO.output(CHANNEL, GPIO.HIGH)  # 上拉电压20us~40us回应DHT
    GPIO.setup(CHANNEL, GPIO.IN)

    # / *DHT响应MCU* /
    while GPIO.input(CHANNEL) == GPIO.LOW:  # DHT检测到启动信号，发出持续80us的低电平响应信号
        continue
    while GPIO.input(CHANNEL) == GPIO.HIGH:  # DHT程序准备向数据总线拉高保持80us，以便DHT准备发送数据
        continue


def get_data():
    j = 0
    data = []
    # / *DHT传送数据 * /
    while j < 40:  # 单线串行发送数据，共40位数据
        k = 0
        while GPIO.input(CHANNEL) == GPIO.LOW:  # 每个数据位都以50us低电平开始，后续高电平信号长度决定0或1
            continue
        while GPIO.input(CHANNEL) == GPIO.HIGH:  # 判断高电平信号长度
            k += 1
            if k > 200:  # 始终高电平，代表DHT未正确响应
                print('!!!!!!!!!!!k={} j ={}'.format(k, j))
                break
        if k < 8:
            data.append(0)  # 高电平信号持续为26~28us，写0
        else:
            data.append(1)  # 高电平持续信号为70us左右，写1

        j += 1  # 读取一位数据成功

    # print("sensor is working.")
    # print(data)
    return data


def data_process(data):
    
    humidity_bit = data[0:8]  # 湿度位
    humidity_point_bit = data[8:16]  # 湿度检测位
    temperature_bit = data[16:24]  # 温度位
    temperature_point_bit = data[24:32]  # 温度检测位
    check_bit = data[32:40]  # 检测位

    humidity = 0
    humidity_point = 0
    temperature = 0
    temperature_point = 0
    check = 0

    # / *数据换算及检测数据是否正确 * / 二进制转10进制
    for i in range(8):
        humidity += humidity_bit[i] * 2 ** (7 - i)  # 换算湿度
        humidity_point += humidity_point_bit[i] * 2 ** (7 - i)
        temperature += temperature_bit[i] * 2 ** (7 - i)  # 换算温度
        temperature_point += temperature_point_bit[i] * 2 ** (7 - i)
        check += check_bit[i] * 2 ** (7 - i)

    tmp = humidity + humidity_point + temperature + temperature_point

    if check == tmp:  # 代表检测成功，输出温度和湿度
        print("temperature :", temperature, "*C, humidity :", humidity, "%")
    else:
        print("wrong")  # 检测失败，输出错误数据
        print("check :", check, ", tmp :", tmp)

    GPIO.cleanup()


def main():
    while True:
        mode_init()
        data = get_data()
        data_process(data)


if __name__ == '__main__':
    main()
