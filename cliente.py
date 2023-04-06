from socket import *

HOST = '10.21.165.12'
PORT = 8000

s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PORT))
s.send("Hello world".encode('utf-8'))
data = s.recv(1024)
print(data.decode('utf-8'))
s.close()
