import socket

targethost = '0.0.0.0'
targerport = 5555
soc = socket.socket()

#connecting to target
soc.connect((targethost, targerport))

#sending data
soc.send(b"GET / HTTP/1.1\r\nHOst: google.com\r\n\r\n")
response = soc.recv(4096)
print(response)