from bluetooth import *
devices = discover_devices()
for device in devices:
    print([_ for _ in find_service(address=device) if 'RFCOMM' in _['protocol'] ])
# now manually select the desired device or hardcode its name/mac whatever in the script
bt_addr = "58:85:A2:78:FC:44"
port = [_ for _ in find_service(address=bt_addr) if 'RFCOMM' in _['protocol']][0]['port']
s = BluetoothSocket(RFCOMM)
s.connect((bt_addr, port))