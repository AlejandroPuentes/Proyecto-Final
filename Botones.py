import tkinter as tk
from tkinter import ttk
<<<<<<< HEAD
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
=======
class Boton1():
    def __init__(self,root):
        self.ventana =root
        self.nombreUsu = None
        self.cedula = None
        self.banco = None
        self.clave = None
    
    
    def registrar (self):
        lblUsuario =tk.Label(self.ventana,text= "Nombre").place(x=200, y=140)
        self.nombreUsu = tk.StringVar()
        txtUsuario = ttk.Entry(self.ventana,textvariable=self.nombreUsu).place(x=250, y=150)
        lblCedula =tk.Label(self.ventana,text="Cedula").place(x=200, y=180)
        self.cedula = tk.StringVar()
        txtcedula = ttk.Entry(self.ventana,textvariable=self.cedula).place(x=250, y=190)
        lblBanco =tk.Label(self.ventana,text= "Banco").place(x=200, y=220)
        txtbanco = ttk.Entry(self.ventana,textvariable=self.banco).place(x=250, y=230)
        lblClave =tk.Label(self.ventana,text= "Clave").place(x=200, y=260)
        self.clave = tk.StringVar()
        txtclave = ttk.Entry(self.ventana,textvariable=self.clave).place(x=250, y=270)
    
    def getNombre (self):
        return self.nombreUsu.get()
    
    def getCedula (self):
        return self.cedula.get()
    
    def getBanco (self):
        return self.banco.get()

    def getClave (self):
        return self.clave.get()
  




























>>>>>>> ee82c41177e4f63ca92cfc8a0077d5340c1c3a96


     