#!/user/bin/env python3
#-*-  coding: utf-8 -*-
import pywifi
from pywifi import const

def createCard():
    #创建一个无限网卡
    wifi = pywifi.PyWiFi()
    #获取无限网卡
    card = wifi.interfaces()[0]
    #打印无限网卡名字
    print(card.name())
    #打印连接状态
    # print(card.status())
    if card.status() == const.IFACE_DISCONNECTED:
        print("未连接")
    elif card.status() == const.IFACE_CONNECTED:
        print("已连接")
#扫描
def scanWifi():
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]
    #扫描附近wifi
    iface.scan()
    #获取扫描之后的结果--结果是一个列表
    numWifi = iface.scan_results()
    # print(numWifi)
    for data in numWifi:
        #遍历后打印在附近扫描出来wifi的名称用ssid -----中文就会乱码
        print(data.ssid)
if __name__ == '__main__':
    #createCard()
    scanWifi()