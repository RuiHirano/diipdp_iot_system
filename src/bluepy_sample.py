import bluepy

scanner = bluepy.btle.Scanner(0)
devices = scanner.scan(3)      # 3秒間スキャンする

for device in devices:
  print('======================================================')
  print('iface : %s' % device.iface)
  print('connectable : %s' % device.connectable)
  print('address : %s' % device.addr)
  print('addrType: %s' % device.addrType)
  print('RSSI    : %s' % device.rssi)
  print('Adv data:')
  for (adtype, desc, value) in device.getScanData():
    print(' (%3s) %s : %s ' % (adtype, desc, value.encode().decode('utf-8')))
    if desc == "16b Service Data":
        print("get 16b Service Data")
        data_length = int((value[0:1]), 16)
        print("data_length: ", data_length)
        flag_data_type = int((value[1:2]), 16)
        print("flag_data_type: ", flag_data_type)
        flag_data = int((value[2:3]), 16)
        print("flag_data: ", flag_data)
        data_length2 = int((value[3:4]), 16)
        print("data_length2: ", data_length2)
