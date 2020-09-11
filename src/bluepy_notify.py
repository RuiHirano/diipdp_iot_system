import bluepy
import binascii
import sys

HANDLE_ACC = 0x001d

exflag = False

class MyDelegate(bluepy.btle.DefaultDelegate):
    def __init__(self, params):
        bluepy.btle.DefaultDelegate.__init__(self)

    def handleNotification(self, cHandle, data):
        global exflag
        print("handle name: ", cHandle, data)
        if cHandle == HANDLE_ACC:
            pass

        c_data = binascii.b2a_hex(data)
        print( "%s: %s" % (b, c_data) )

def main():
    if len(sys.argv) == 1:
      print('Usage: notify.py BLE_DEVICE_ADDRESS')
      sys.exit()

    devadr = sys.argv[1]
    peri = bluepy.btle.Peripheral()
    peri.connect(devadr, bluepy.btle.ADDR_TYPE_PUBLIC)
    peri.withDelegate(MyDelegate(bluepy.btle.DefaultDelegate))
    

    # ボタン notify を要求
    peri.writeCharacteristic(HANDLE_ACC, b'\x01\x00', True)
    peri.writeCharacteristic(0x0028, "\x01\x00", True) # 通知有効化
    #peri.writeCharacteristic(0x002a, b"\x50\x00", True) # 80ms ごとに通知 #デフォルトは 20ms
    #peri.writeCharacteristic(0x0028, b"\x01\x00", True) # 通知有効化

    print( "Notification を待機。A or B ボタン長押しでプログラム終了")
    while exflag == False:
        if peri.waitForNotifications(1.0):
            continue
    peri.disconnect()

if __name__ == "__main__":
    main()