from bluetooth import *
import socket
import time
port = 0x1001
server_sock=BluetoothSocket(L2CAP)
server_sock.bind(("",port))
server_sock.listen(1)
client_sock,address = server_sock.accept()
print("Accepted connection from ",address)
data = client_sock.recv(1024)
print("received [%s]" % data)
time.sleep(10)
client_sock.close()
server_sock.close()