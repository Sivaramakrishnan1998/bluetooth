
from bluetooth import *
server_address = "58:85:A2:78:FC:44"
port = 1
sock=BluetoothSocket( RFCOMM )
sock.connect((server_address, port))
sock.send("hello!!")
sock.close()
