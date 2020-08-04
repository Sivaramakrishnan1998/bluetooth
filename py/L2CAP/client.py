from bluetooth import *
import socket
import time

def return_server_addr(server:str)->str:
    available_devices = discover_devices()
    for address in available_devices:
        if (server == lookup_name(address)):
            return address


try:

    #create socket
    sock = BluetoothSocket(L2CAP)

    #get server address from available devices
    server_address = return_server_addr("device_name") # param -> device name

    if server_address is not None:
        port = 0x1001
        #socket connection
        sock.connect((server_address, port))
        #send message
        sock.send("hello from client")
        time.sleep(10)

    else:
        print("Could not able to discover server")

    #close socket
    sock.close()

except:
    print("Exception Occurred")

