import sys
import bluepy

HANDLE_DEVNAME = 0x0009
HANDLE_SERIAL = 0x0010   # Manufacture
SERVICE_DATA = 0x0012   # Model
SERVICE_DATA1 = 0x0014  # Mac Address
SERVICE_DATA2 = 0x0016  # HardwareVersion
SERVICE_DATA3 = 0x0018  # FirmwareVersion
SERVICE_DATA4 = 0x001a # Software Version
SERVICE_DATA5 = 0x001d # ??? b'F\xd9c\x0e\xad\x14u@\xcaM\xbd/\x10\xeb\x066', 2: b'\xb2l\xf70D\xbd\xc3(}\x98\x19\xca\x11\xfa1\xba'
SERVICE_DATA6 = 0x0021 
SERVICE_DATA7 = 0x0023
SERVICE_DATA8 = 0x0025
SERVICE_DATA9 = 0x0027
SERVICE_DATA10 = 0x0029
SERVICE_DATA11 = 0x002b

def main():
    peri = bluepy.btle.Peripheral()
    peri.connect(devadr, bluepy.btle.ADDR_TYPE_PUBLIC)
    devname = peri.readCharacteristic(HANDLE_DEVNAME)
    print( "Device Name: %s" % devname )
    serialnum = peri.readCharacteristic(HANDLE_SERIAL)
    print( "Serial Number: %s" % serialnum )
    sdata = peri.readCharacteristic(SERVICE_DATA)
    print( "Service Data: %s" % sdata )
    sdata = peri.readCharacteristic(SERVICE_DATA1)
    print( "Service Data1: %s" % sdata )
    sdata = peri.readCharacteristic(SERVICE_DATA2)
    print( "Service Data2: %s" % sdata )
    sdata = peri.readCharacteristic(SERVICE_DATA3)
    print( "Service Data3: %s" % sdata )
    sdata = peri.readCharacteristic(SERVICE_DATA4)
    print( "Service Data4: %s" % sdata )
    #sdata = peri.readCharacteristic(SERVICE_DATA5)
    #print( "Service Data5: %s" % sdata )
    sdata = peri.readCharacteristic(SERVICE_DATA6)
    print( "Service Data6: %s" % sdata )
    sdata = peri.readCharacteristic(SERVICE_DATA7)
    print( "Service Data7: %s" % sdata )
    sdata = peri.readCharacteristic(SERVICE_DATA8)
    print( "Service Data8: %s" % sdata )
    sdata = peri.readCharacteristic(SERVICE_DATA9)
    print( "Service Data9: %s" % sdata )
    sdata = peri.readCharacteristic(SERVICE_DATA10)
    print( "Service Data10: %s" % sdata )
    sdata = peri.readCharacteristic(SERVICE_DATA11)
    print( "Service Data11: %s" % sdata )
    peri.disconnect()

if __name__ == "__main__":
    if len(sys.argv) == 1:
      print('Usage: getvalue.py BLE_DEVICE_ADDRESS')
      sys.exit()
    devadr = sys.argv[1]

    main()