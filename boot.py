# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()
from wifi import wifi_connect
from demo import app_instance


if __name__ == '__main__':
    wifi_connect.run()
    app_instance.run()
