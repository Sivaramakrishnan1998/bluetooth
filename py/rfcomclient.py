from bluetooth import *
server_address = "78:44:05:57:A8:A4"
port = 1
sock=BluetoothSocket( RFCOMM )
sock.connect((server_address, port))
sock.send("hello!!")
sock.close()