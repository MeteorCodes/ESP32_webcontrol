import network
import time
from machine import Pin

class WIFI:
    def __init__(self):
        self.led = Pin(2, Pin.OUT)
        self.wlan = network.WLAN(network.STA_IF)  # 定义WLAN

    def connect(self):
        self.wlan.active(True)  # True和False控制WIFI的开关
        if not self.wlan.isconnected():
            print('connecting to network...')
            self.wlan.connect('ChinaNet-A90AF8', 'cuxe7443') #需要手动输入wifi名字和密码
            i = 1
            while not self.wlan.isconnected():
                print("正在链接...{}".format(i))
                time.sleep(1)
                i = i + 1
        print('network config:', self.wlan.ifconfig()[0])  # 打印出ESP32当前连接网络的IP地址
        self.led.value(1)
            
    def run(self):
        self.connect()

wifi_connect = WIFI()


