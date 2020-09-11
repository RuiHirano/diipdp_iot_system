import bluepy
import sys

class MyDelegate(bluepy.btle.DefaultDelegate):
    def __init__(self, params):
        bluepy.btle.DefaultDelegate.__init__(self)
        # ... initialise here

    def handleNotification(self, cHandle, data):
        # ... perhaps check cHandle
        # ... process 'data'
        print("data: ", data)
        pass


# Initialisation  -------
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: {} <addr>".format(sys.argv[0]))
        sys.exit(1)
    p = bluepy.btle.Peripheral( sys.argv[1] )
    p.setDelegate( MyDelegate(params) )

    # Setup to turn notifications on, e.g.
    #   svc = p.getServiceByUUID( service_uuid )
    #   ch = svc.getCharacteristics( char_uuid )[0]
    #   ch.write( setup_data )

    # Main loop --------

    while True:
        if p.waitForNotifications(1.0):
            # handleNotification() was called
            continue

        print("Waiting...")
        # Perhaps do something else here
