import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk

class Boton1():
    def __init__(self, x):

        self.x = x

        #Botones
        self.imgbtn = Image.open("Sprites/Button/1.png")
        self.imgbtn = self.imgbtn.resize((100, 65), Image.ANTIALIAS) # Redimension (Alto, Ancho)
        self.imgbtn = ImageTk.PhotoImage(self.imgbtn)

        self.btn1 = Button(self.x,image=self.imgbtn, command = lambda: self.update(self.fondo, 1))
        self.btn1.place(x=623,y=415)
        self.btn2 = Button(self.x,image=self.imgbtn, command = lambda: self.update(self.fondo, 0))
        self.btn2.place(x=623,y=330)


     