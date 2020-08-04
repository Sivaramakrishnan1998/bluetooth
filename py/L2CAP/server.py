from bluetooth import *
import socket
import time

try:
    port = 0x1001
    #create socket
    server_sock=BluetoothSocket(L2CAP)

    server_sock.bind(("",port))
    server_sock.listen(1)

    #accept the connection
    client_sock,address = server_sock.accept()
    print("Accepted connection from ",address)
    
    #receive data
    data = client_sock.recv(1024)
    print("received ", data)
    time.sleep(10)

    #close the sockets
    client_sock.close()
    server_sock.close()
except:
    print("Exception occurred")