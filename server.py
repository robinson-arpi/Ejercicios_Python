from socket import*
s = socket(AF_INET, SOCK_STREAM)

HOST = '10.21.165.12'
PORT =  8000
s.bind((HOST, PORT))
s.listen(1)
(conn, addr) = s.accept()
while True:
    data = conn.recv(1024)
    if not data:
        break
    conn.send(data + b"*")
    print(str(data))
conn.close()    
