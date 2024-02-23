import socket


HOST = socket.gethostbyname(socket.gethostname())
PORT = 9090
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((HOST,PORT))

server.listen(1)

connected = True

while connected:
    conn,addr = server.accept()

    message = conn.recv(1024).decode('utf-8')
   
    

