from bluetooth import *
target_name = "sirakr"
target_address = None
nearby_devices = discover_devices()
for address in nearby_devices:
    print (address)

if target_address is not None:
    print ("found target bluetooth device with address ", target_address)
else:
    print ("could not find target bluetooth device nearby")

