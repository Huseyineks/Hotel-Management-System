import socket
from database import * 
import threading
HOST = socket.gethostbyname(socket.gethostname())
PORT = 9090
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((HOST,PORT))




class Server:
    def __init__(self):
        
    
        self.connected = True


    def receive(self,conn,addr):
        
        while self.connected:
            
                
             
            message = conn.recv(1024).decode('utf-8')
            
            DATABASE(message)
            
            


    def start(self):
        server.listen(5)
        while True:
           conn,addr = server.accept()
           package = threading.Thread(target=self.receive,args=(conn,addr))
           package.start()            

    
        


z = Server()
z.start()
   
    

