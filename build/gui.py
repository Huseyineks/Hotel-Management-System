
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import *
import socket

HOST = socket.gethostbyname(socket.gethostname())
PORT = 9090

data_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
data_server.connect((HOST,PORT))

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\hüseyin\Desktop\Hotel Management System\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    
    return ASSETS_PATH / Path(path)

class App:
    def __init__(self):
        self.window = Tk()

        self.window.geometry("630x379")
        self.window.configure(bg = "#FFFFFF")
        self.frame = Frame(self.window,height=379,width=630)
        self.frame.pack_propagate(False)
        self.frame.configure(bg="#FFFFFF")
        self.frame.pack()
        
        canvas = Canvas(
        self.frame,
        bg = "#FFFFFF",
        height = 379,
        width = 630,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
        )

        canvas.place(x = 0, y = 0)
        image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
        image_1 = canvas.create_image(
        157.0,
        196.0,
        image=image_image_1
        )

        canvas.create_rectangle(
        0.0,
        0.0,
        626.0,
        14.0,
        fill="#520759",
        outline="")

        canvas.create_text(
        377.0,
        47.0,
        anchor="nw",
        text="WELCOME",
        fill="#88176F",
        font=("Inter SemiBold", 36 * -1)
        )

        canvas.create_text(
        379.0,
        119.0,
        anchor="nw",
        text="Name",
        fill="#000000",
        font=("Inter SemiBold", 12 * -1)
        )

        canvas.create_text(
        379.0,
        248.0,
        anchor="nw",
        text="E-mail",
        fill="#000000",
        font=("Inter SemiBold", 12 * -1)
        )

        canvas.create_text(
        375.0,
        186.0,
        anchor="nw",
        text="Surname\n",
        fill="#000000",
        font=("Inter SemiBold", 12 * -1)
        )

        entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
        entry_bg_1 = canvas.create_image(
        471.0,
        159.5,
        image=entry_image_1
        )
        self.entry_1 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
        )
        self.entry_1.place(
        x=389.0,
        y=145.0,
        width=164.0,
        height=27.0
        )

        entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
        entry_bg_2 = canvas.create_image(
        472.0,
        224.5,
        image=entry_image_2
        )
        self.entry_2 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
        )
        self.entry_2.place(
        x=389.0,
        y=210.0,
        width=166.0,
        height=27.0
        )

        entry_image_3 = PhotoImage(
        file=relative_to_assets("entry_3.png"))
        entry_bg_3 = canvas.create_image(
        471.0,
        288.5,
        image=entry_image_3
        )
        self.entry_3 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
        )
        self.entry_3.place(
        x=389.0,
        y=274.0,
        width=164.0,
        height=27.0
        )

        button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
        self.button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=self.getInfo,
        relief="flat"
        )
        self.button_1.place(
        x=434.0,
        y=310.0,
        width=66.0,
        height=38.0
        )
        self.window.resizable(False, False)
        self.window.mainloop()
    def getInfo(self):
        
        name = self.entry_1.get()
        surname = self.entry_2.get()
        email = self.entry_3.get()

        package = name + ',' + surname + ',' + email
        
        data_server.send(package.encode('utf-8'))
        
        self.cleanFrame()
          
    def cleanFrame(self):
        self.button_1.place_forget()
        self.entry_1.place_forget()
        self.entry_2.place_forget()
        self.entry_3.place_forget()
        self.frame.pack_forget()
        Page(self.window)

class Page:
    def __init__(self,master):
        self.window = master
        self.window.geometry("630x481")
        self.window.configure(bg = "#FFFFFF")
        self.frame = Frame(self.window,height=481,width=630)
        self.frame.pack_propagate(False)
        self.frame.configure(bg="#FFFFFF")
        self.frame.pack()
        canvas = Canvas(
            self.frame,
            bg = "#FFFFFF",
            height = 481,
            width = 630,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
            )

        canvas.place(x = 0, y = 0)
        button_image_1 = PhotoImage(
        file=relative_to_assets("button_1g.png"))
        button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=self.getInfo,
        relief="flat"
        )
        button_1.place(
        x=282.0,
        y=409.0,
        width=66.0,
        height=38.0
        )

        entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1g.png"))
        entry_bg_1 = canvas.create_image(
        141.5,
        313.0,
        image=entry_image_1
        )
        self.entry_1 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
        )
        self.entry_1.place(
        x=41.0,
        y=294.0,
        width=201.0,
        height=36.0
        )

        entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2g.png"))
        entry_bg_2 = canvas.create_image(
        493.5,
        313.0,
        image=entry_image_2
        )
        self.entry_2 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
        )
        self.entry_2.place(
        x=393.0,
        y=294.0,
        width=201.0,
        height=36.0
        )

        canvas.create_text(
        389.0,
        279.0,
        anchor="nw",
        text="Adult",
        fill="#000000",
        font=("Inter", 12 * -1)
        )

        entry_image_3 = PhotoImage(
        file=relative_to_assets("entry_3g.png"))
        entry_bg_3 = canvas.create_image(
        166.5,
        378.0,
        image=entry_image_3
        )
        self.entry_3 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
        )
        self.entry_3.place(
        x=66.0,
        y=359.0,
        width=201.0,
        height=36.0
        )

        entry_image_4 = PhotoImage(
        file=relative_to_assets("entry_4g.png"))
        entry_bg_4 = canvas.create_image(
        463.5,
        378.0,
        image=entry_image_4
        )
        self.entry_4 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
        )
        self.entry_4.place(
        x=363.0,
        y=359.0,
        width=201.0,
        height=36.0
        )

        image_image_1 = PhotoImage(
        file=relative_to_assets("image_1g.png"))
        image_1 = canvas.create_image(
        315.0,
        130.0,
        image=image_image_1
        )

        image_image_2 = PhotoImage(
        file=relative_to_assets("image_2g.png"))
        image_2 = canvas.create_image(
        13.0,
        312.0,
        image=image_image_2
        )

        canvas.create_text(
        34.0,
        279.0,
        anchor="nw",
        text="Childeren",
        fill="#000000",
        font=("Inter", 12 * -1)
        )

        image_image_3 = PhotoImage(
        file=relative_to_assets("image_3g.png"))
        image_3 = canvas.create_image(
        365.0,
        312.0,
        image=image_image_3
        )

        image_image_4 = PhotoImage(
        file=relative_to_assets("image_4g.png"))
        image_4 = canvas.create_image(
        34.0,
        378.0,
        image=image_image_4
        )

        image_image_5 = PhotoImage(
        file=relative_to_assets("image_5g.png"))
        image_5 = canvas.create_image(
        335.0,
        377.0,
        image=image_image_5
        )

        canvas.create_text(
        61.0,
        344.0,
        anchor="nw",
        text="Room",
        fill="#000000",
        font=("Inter", 12 * -1)
        )

        canvas.create_text(
        362.0,
        344.0,
        anchor="nw",
        text="Date",
        fill="#000000",
        font=("Inter", 12 * -1)
        )

        canvas.create_text(
        216.0,
        279.0,
        anchor="nw",
        text="+$5.00",
        fill="#000000",
        font=("Inter", 12 * -1)
        )

        canvas.create_text(
        558.0,
        279.0,
        anchor="nw",
        text="+$10.00",
        fill="#000000",
        font=("Inter", 12 * -1)
        )

        canvas.create_text(
        236.0,
        345.0,
        anchor="nw",
        text="+$50.00",
        fill="#000000",
        font=("Inter", 12 * -1)
        )
        self.window.resizable(False, False)
        self.window.mainloop()



    def getInfo(self):
        child = self.entry_1.get()
        adult = self.entry_2.get()
        room = self.entry_3.get()
        date = self.entry_4.get()

        package = child + ',' + adult + ',' + room + ',' + date

        data_server.send(package.encode('utf-8'))    

        
        
         






App()
  
        
  
  
  