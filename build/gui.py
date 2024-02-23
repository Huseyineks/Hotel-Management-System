
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import *


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
        
        
        
        self.cleanFrame()
          
    def cleanFrame(self):
        self.button_1.place_forget()
        self.entry_1.place_forget()
        self.entry_2.place_forget()
        self.entry_3.place_forget()
        self.frame.pack_forget()

class Page:
    def __init__(self,master):
        frame1 = Frame(master,height=379,width=630)
        frame1.pack_propagate(False)
        frame1.configure(bg="#FFFFFF")
        frame1.pack()
        label = Label(frame1,text="asdadsdd")
        label.pack()
        label1 = Label(frame1,text="asdadsdasdasdsadasdd")
        label1.pack()

        
        
         






App()
  
        
  
  
  