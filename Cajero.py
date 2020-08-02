import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk

from FactoriaInterfaz import *
from Builder import *

app = BuilderManager()
app.setBuilder(BuilderPantalla0())
app.buildCajero()
app0 = app.getCajero()

class Cajero():

    def __init__(self):

        ##ventana
        ventana = tk.Tk()
        ventana.title("Cajero")
        ventana.geometry("749x721")
        ventana.resizable(width=0, height=0)

        ##fondo
        image = Image.open("Sprites/Cajero/DiseñoSprites.png")
        image.thumbnail((749,721))
        tkimage = ImageTk.PhotoImage(image)
        bckground = Label(ventana, image=tkimage, width = 1000, height = 980).pack()
    
        self.fondoPantalla = None

    def setFondoPantalla(self, fondoPantalla):
        self.fondoPantalla = fondoPantalla
    
    def getFondoPantalla(self):
        return self.fondoPantalla

    def operacion(self):

        pantallas = [FabricaScreenPrincipal(), FabricaScreens(), FabricaAgrario(), FabricaBancolombia(), FabricaDavivienda()]

        pantalla = pantallas[0]

        pantalla.crearPantalla(ventana)

        ventana.mainloop()
        
