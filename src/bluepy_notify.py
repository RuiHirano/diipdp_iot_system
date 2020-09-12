import bluepy
import binascii
import sys

HANDLE_ACC = 0x001d
HANDLE_ACC2 = 0x0023
HANDLE_ACC3 = 0x0025
HANDLE_ACC4 = 0x0027
HANDLE_ACC5 = 0x0029
HANDLE_ACC6 = 0x002b


exflag = False

class MyDelegate(bluepy.btle.DefaultDelegate):
    def __init__(self, params):
        bluepy.btle.DefaultDelegate.__init__(self)

    def handleNotification(self, cHandle, data):
        global exflag
        print("handle name: ", cHandle, data)
        #if cHandle == HANDLE_ACC:
        #    pass

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
    print("connected")
    charas = peri.getCharacteristics()
    for chara in charas:
        print("======================================================")
        print(" UUID : %s" % chara.uuid )
        print(" Handle %04x: %s" % (chara.getHandle(), chara.propertiesToString()))

    # ボタン notify を要求
    peri.writeCharacteristic(HANDLE_ACC, b'\x01\x00', True)
    peri.writeCharacteristic(HANDLE_ACC2, b'\x01\x00', True)
    peri.writeCharacteristic(HANDLE_ACC3, b'\x01\x00', True)
    peri.writeCharacteristic(HANDLE_ACC4, b'\x01\x00', True)
    peri.writeCharacteristic(HANDLE_ACC5, b'\x01\x00', True)
    peri.writeCharacteristic(HANDLE_ACC6, b'\x01\x00', True)
    #peri.writeCharacteristic(NOTIFY, "\x01\x00", True) # 通知有効化
    #peri.writeCharacteristic(0x002a, b"\x50\x00", True) # 80ms ごとに通知 #デフォルトは 20ms
    #peri.writeCharacteristic(0x0028, b"\x01\x00", True) # 通知有効化

    print( "Notification を待機。A or B ボタン長押しでプログラム終了")
    while exflag == False:
        if peri.waitForNotifications(1.0):
            print("wait")
            continue
    #peri.disconnect()

if __name__ == "__main__":
    main()