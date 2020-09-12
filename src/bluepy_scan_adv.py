from datetime import datetime
from bluepy.btle import Scanner, DefaultDelegate

def convert16to10(x="0000", dicimal=2):
    minus = False
    binx = format(int(x, 16), '016b')  # 二進数表示 16桁に0埋め: '016' 二進数： 'b'
    if binx[0] == "1":
        # 補数変換
        binx = convert2Complement(binx)
        minus = True

    leftbin = binx[:dicimal*4]   # 整数部分
    rightbin = binx[dicimal*4:]  # 小数点部分

    # 10進数へ変換(整数部分)
    left10 = int(leftbin, 0)
    # 10進数へ変換(少数部分)
    right10 = 0
    for index, k in enumerate(rightbin):
        right10 += int(k)*2**(-index-1)
    
    if minus: # 補数だった場合、負にする
        return -(left10 + right10)
    else: 
        return left10 + right10

def convert2Complement(binx):
    # 2の補数変換
    return format((-int(binx[0]) << len(binx) | int(binx, 2))*-1, '016b')
    

class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

    def handleDiscovery(self, dev, isNewDev, isNewData):
        if dev.addr == "ac:23:3f:26:35:20":
            print(datetime.now().time(), str(dev.rawData).replace('\\x', ''), dev.addr)
            data = str(dev.rawData).replace('\\x', '')
            print(data[29:33], data[33:37], data[37:41])
            accx = convert16to10(data[29:33])
            accy = convert16to10(data[33:37])
            accz = convert16to10(data[37:41])
            print('accx {}, accy {}, accz {}'.format(accx, accy, accz))
        scanner.clear()
        scanner.start()


scanner = Scanner().withDelegate(ScanDelegate())
scanner.start()

while True:
    scanner.process()
