from lightblue import *
s = socket()
s.bind(("", 0))
s.listen(1)
advertise("my service", s, RFCOMM)
conn, addr = s.accept
data = conn.recv(1024)
conn.close()
s.close()