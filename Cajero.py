from Builder import *
from Botones import *

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

        btn = Boton1(self.root)
        self.manejoInterfaz(0)
        self.root.mainloop()

    def manejoInterfaz(self, x):
        ##imagen de pantalla // ii = imagen interfaces
        self.fondo = Label(self.root,image=self.setScreen(x), width = 445, height = 365 )
        self.fondo.place(x=150,y=125)
        
    
    def setScreen(self, posicion):
        self.ii2 = Image.open(self.getCarrusel(posicion))
        self.ii2.thumbnail((466,366))
        self.ii2 = ImageTk.PhotoImage(self.ii2)
        return self.ii2 

    def update(self, label, x):
        label.place(x=9999, y=9999)
        self.nfondo = Label(self.root, image=self.setScreen(x))
        self.nfondo.place(x=151,y=126)

    def getCarrusel(self, posicion):
        self.app = BuilderManager()
        self.opciones = [BuilderPantalla0(), BuilderPantalla1(), BuilderPantalla2(), BuilderAgrario(), BuilderBancolombia(), BuilderDavivienda()]
        self.app.setBuilder(self.opciones[posicion])
        return self.app.buildCajero()
    

