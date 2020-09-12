from datetime import datetime
from bluepy.btle import Scanner, DefaultDelegate

class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

    def handleDiscovery(self, dev, isNewDev, isNewData):
        if dev.addr == "ac:23:3f:26:35:20":
            print(datetime.now().time(), dev.rawData.replace('\x', ''), dev.addr)
        scanner.clear()
        scanner.start()


scanner = Scanner().withDelegate(ScanDelegate())
scanner.start()

while True:
    scanner.process()
