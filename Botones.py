import tkinter as tk
from tkinter import ttk
class Boton1():
     
    def __init__(self,root):
        self.ventana =root
        self.nombreUsu = None
        self.cedula = None
        self.banco = None
        self.clave = None
    
    
    def registrar (self):
        self.lblUsuario =tk.Label(self.ventana,text= "Nombre").place(x=200, y=150)
        self.nombreUsu = tk.StringVar()
        self.txtUsuario = ttk.Entry(self.ventana,textvariable=self.nombreUsu).place(x=250, y=150)
        self.lblCedula =tk.Label(self.ventana,text="Cedula").place(x=200, y=190)
        self.cedula = tk.StringVar()
        self.txtcedula = ttk.Entry(self.ventana,textvariable=self.cedula).place(x=250, y=190)
        self.lblBanco =tk.Label(self.ventana,text= "Banco").place(x=200, y=230)
        self.banco = tk.StringVar()
        self.txtbanco = ttk.Entry(self.ventana,textvariable=self.banco).place(x=250, y=230)
        self.lblClave =tk.Label(self.ventana,text= "Clave").place(x=200, y=270)
        self.clave = tk.StringVar()
        self.txtclave = ttk.Entry(self.ventana,textvariable=self.clave).place(x=250, y=270)
    

    
    def getNombre(self):
        return self.nombreUsu.get()
    
    def getCedula(self):
        return self.cedula.get()
    
    def getBanco(self):
        return self.banco.get()

    def getClave (self):
        return self.clave.get()
  






























     