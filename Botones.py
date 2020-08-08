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
  





























''' #botones
        self.img = Image.open("Sprites/Button/1.png")
        self.img = self.img.resize((100, 65), Image.ANTIALIAS) # Redimension (Alto, Ancho)
        self.img = ImageTk.PhotoImage(self.img)
        self.btn1 = Button(self.ventana,image=self.img,text="Hola").place(x=20,y=415)
        self.btn2 = Button(self.ventana,image=self.img,text="Hola").place(x=623,y=415)
        self.btn3 = Button(self.ventana,image=self.img,text="Hola").place(x=20,y=330)
        self.btn4 = Button(self.ventana,image=self.img,text="Hola").place(x=623,y=330)
        self.btn5 = Button(self.ventana,image=self.img,text="Hola").place(x=20,y=250)
        self.btn4 = Button(self.ventana,image=self.img,text="Hola").place(x=623,y=250) 
        

        tkimage2 = ImageTk.PhotoImage(imagen2)
        fondo2 = Label(ventana,image=tkimage2, width = 445, height = 365 ).place(x=150,y=125)
        '''
    
     