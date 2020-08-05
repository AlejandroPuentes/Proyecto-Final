from abc import ABC, abstractmethod

import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk

class AbstractProducto(ABC):

        @abstractmethod
        def __init__(self):
            pass

class Pantalla0(AbstractProducto):
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

        ##imagen de pantalla
        imagen = Image.open("Sprites/Pantalla/0.png")
        imagen.thumbnail((465,365))
        tkimage2 = ImageTk.PhotoImage(imagen)
        fondo2 = Label(ventana,image=tkimage2, width = 445, height = 365 ).place(x=150,y=125)

        ventana.mainloop()

class Pantalla1(AbstractProducto):
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

        ##imagen de pantalla
        imagen = Image.open("Sprites/Pantalla/1.png")
        imagen.thumbnail((465,365))
        tkimage2 = ImageTk.PhotoImage(imagen)
        fondo2 = Label(ventana,image=tkimage2, width = 445, height = 365 ).place(x=150,y=125)

        ventana.mainloop()

class PantallaAgrario(AbstractProducto):
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

        ##imagen de pantalla
        imagen = Image.open("Sprites/Pantalla/Agrario.png")
        imagen.thumbnail((465,365))
        tkimage2 = ImageTk.PhotoImage(imagen)
        fondo2 = Label(ventana,image=tkimage2, width = 445, height = 365 ).place(x=150,y=125)

        ventana.mainloop()

class PantallaBancolombia(AbstractProducto):
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

        ##imagen de pantalla
        imagen = Image.open("Sprites/Pantalla/Bancolombia.png")
        imagen.thumbnail((465,365))
        tkimage2 = ImageTk.PhotoImage(imagen)
        fondo2 = Label(ventana,image=tkimage2, width = 445, height = 365 ).place(x=150,y=125)

        ventana.mainloop()
        
class PantallaDavivienda(AbstractProducto):
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

        ##imagen de pantalla
        imagen = Image.open("Sprites/Pantalla/Davivienda.png")
        imagen.thumbnail((465,365))
        tkimage2 = ImageTk.PhotoImage(imagen)
        fondo2 = Label(ventana,image=tkimage2, width = 445, height = 365 ).place(x=150,y=125)

        ventana.mainloop()