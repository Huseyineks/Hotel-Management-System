import socket
from database import * 
import threading
from tkinter import *
from tkinter import ttk
from pathlib import Path
HOST = socket.gethostbyname(socket.gethostname())
PORT = 9090
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((HOST,PORT))

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\hüseyin\Desktop\Hotel Management System\build\assets\frame0")
def relative_to_assets(path: str) -> Path:
    
    return ASSETS_PATH / Path(path)


class Server:
    def __init__(self,window):
        self.window = window
        
        self.window.geometry("803x483")
        self.window.configure(bg = "#898282")
        canvas = Canvas(
        self.window,
        bg = "#898282",
        height = 483,
        width = 803,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
        )
        mycursor.execute("SELECT * FROM People")
        canvas.place(x = 0, y = 0)
        image_image_1 = PhotoImage(
        file=relative_to_assets("image_1v.png"))
        image_1 = canvas.create_image(
        401.0,
        135.0,
        image=image_image_1
        )

        image_image_2 = PhotoImage(
        file=relative_to_assets("image_2v.png"))
        image_2 = canvas.create_image(
        120.0,
        86.0,
        image=image_image_2
        )

        canvas.create_text(
        41.0,
        28.0,
        anchor="nw",
        text="Total Member",
        fill="#000000",
        font=("Inter", 12 * -1)
        )

        image_image_3 = PhotoImage(
        file=relative_to_assets("image_3v.png"))
        image_3 = canvas.create_image(
        145.0,
        35.0,
        image=image_image_3
        )

        image_image_4 = PhotoImage(
        file=relative_to_assets("image_4v.png"))
        image_4 = canvas.create_image(
        395.0,
        86.0,
        image=image_image_4
        )

        canvas.create_text(
        320.0,
        28.0,
        anchor="nw",
        text="Total Price",
        fill="#000000",
        font=("Inter", 12 * -1)
        )

        canvas.create_text(
        316.0,
        62.0,
        anchor="nw",
        text="$200",
        fill="#000000",
        font=("Inter Bold", 40 * -1)
        )

        image_image_5 = PhotoImage(
        file=relative_to_assets("image_5v.png"))
        image_5 = canvas.create_image(
        679.0,
        86.0,
        image=image_image_5
        )

        canvas.create_text(
        600.0,
        28.0,
        anchor="nw",
        text="Total Room\n",
        fill="#000000",
        font=("Inter", 12 * -1)
        )

        canvas.create_text(
        598.0,
        62.0,
        anchor="nw",
        text="73",
        fill="#000000",
        font=("Inter Bold", 40 * -1)
        )

        image_image_6 = PhotoImage(
        file=relative_to_assets("image_6v.png"))
        image_6 = canvas.create_image(
        401.0,
        377.0,
        image=image_image_6
        )

        image_image_7 = PhotoImage(
        file=relative_to_assets("image_7v.png"))
        image_7 = canvas.create_image(
        401.0,
        32.0,
        image=image_image_7
        )

        image_image_8 = PhotoImage(
        file=relative_to_assets("image_8v.png"))
        image_8 = canvas.create_image(
        685.0,
        32.0,
        image=image_image_8
        )

        canvas.create_text(
        39.0,
        62.0,
        anchor="nw",
        text="73",
        fill="#000000",
        font=("Inter Bold", 40 * -1)
        )
        table = ttk.Treeview(window,show="headings")
        table['columns'] = ("person_id","Name","Surname","Email")
        
        
        table.column("person_id",anchor=W,width=200)
        table.column("Name",anchor=W,width=200)
        table.column("Surname",anchor=W,width=200)
        table.column("Email",anchor=W,width=200)
        
        
        table.heading("person_id",text="person_id",anchor=W)
        table.heading("Name",text="Name",anchor=W)
        table.heading("Surname",text="Surname",anchor=W)
        table.heading("Email",text="Email",anchor=W)
        table.configure(height=10)
        table.place(x = 0.0,y =271.0)
        for i,data in enumerate(mycursor):
            table.insert(parent='',index='end',iid=i,values=(data[0],data[1],data[2],data[3]))
        self.window.resizable(False, False)
        self.window.mainloop()
        self.start()
            
        
        

              
        

        




    def totalRow(self,table):
        count = 0
        
        

        for i in table:
            count += 1

        return count     


    def receive(self,conn,addr):
        
        while True:
            
                
             
            message = conn.recv(1024).decode('utf-8')
            
            
            DATABASE(message)
            
            


    def start(self):
        server.listen(5)
        while True:
           conn,addr = server.accept()
           package = threading.Thread(target=self.receive,args=(conn,addr))
           package.start()            

    
        


root = Tk()
z = Server(root)



   
    

