import sys
import bluepy

HANDLE_DEVNAME = 0x0009
HANDLE_SERIAL = 0x000c
SERVICE_DATA = 0x0010

def main():
    peri = bluepy.btle.Peripheral()
    peri.connect(devadr, bluepy.btle.ADDR_TYPE_PUBLIC)
    devname = peri.readCharacteristic(HANDLE_DEVNAME)
    print( "Device Name: %s" % devname.decode("utf-8") )
    serialnum = peri.readCharacteristic(HANDLE_SERIAL)
    print( "Serial Number: %s" % serialnum )
    sdata = peri.readCharacteristic(SERVICE_DATA)
    print( "Service Data: %s" % sdata )
    peri.disconnect()

if __name__ == "__main__":
    if len(sys.argv) == 1:
      print('Usage: getvalue.py BLE_DEVICE_ADDRESS')
      sys.exit()
    devadr = sys.argv[1]

    main()