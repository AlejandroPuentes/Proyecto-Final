from Builder import *

import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk

class Cajero():
    def __init__(self):
        ##ventana
        self.root = tk.Tk()
        self.root.title("Cajero")
        self.root.geometry("749x721")
        self.root.resizable(width=0, height=0)

        ##fondo // ifo = Imagen Fondo Original
        self.ifo = Image.open("Sprites/Cajero/DiseñoSprites.png")
        self.ifo.thumbnail((749,721))
        self.ifo = ImageTk.PhotoImage(self.ifo)
        self.imgprincipal = Label(self.root, image=self.ifo, width = 1000, height = 980)
        self.imgprincipal.pack()

        #Botones
        self.imgbtn = Image.open("Sprites/Button/1.png")
        self.imgbtn = self.imgbtn.resize((100, 65), Image.ANTIALIAS) # Redimension (Alto, Ancho)
        self.imgbtn = ImageTk.PhotoImage(self.imgbtn)

        ##imagen de pantalla // ii = imagen interfaces
        self.fondo = Label(self.root,image=self.setScreen(0), width = 445, height = 365 )
        self.fondo.place(x=150,y=125)
        self.text1 = Label(self.root, text = "Iniciar Sesión" )
        self.text1.place(x=423, y = 455)
        self.text2 = Label(self.root, text = "Registrarse" )
        self.text2.place(x=423, y = 360)
        self.btn1 = Button(self.root,image=self.imgbtn, command = self.update)
        self.btn1.place(x=623,y=415)
        self.btn2 = Button(self.root,image=self.imgbtn)
        self.btn2.place(x=623,y=330)

        self.root.mainloop()
    
    def setScreen(self, posicion):
        self.options = [Image.open(self.getCarrusel(0)),Image.open(self.getCarrusel(1)), Image.open(self.getCarrusel(2)), Image.open(self.getCarrusel(3)), Image.open(self.getCarrusel(4))]
        self.ii2 = self.options[posicion]
        self.ii2.thumbnail((465,365))
        self.ii2 = ImageTk.PhotoImage(self.ii2)
        return self.ii2 

    def update(self):
        self.fondo.place(x=9999, y=9999)
        self.nfondo = Label(self.root, image=self.setScreen(1))
        self.nfondo.place(x=150,y=125)

    def getCarrusel(self, posicion):
        self.app = BuilderManager()
        self.opciones = [BuilderPantalla0(), BuilderPantalla1(), BuilderAgrario(), BuilderBancolombia(), BuilderDavivienda()]
        self.app.setBuilder(self.opciones[posicion])
        return self.app.buildCajero()

cajero = Cajero()

