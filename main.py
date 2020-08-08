from Builder import *
from Botones import *
import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
from Registrar import registro

class Cajero():
    def __init__(self):
        self.estado = 1
        self.datos = registro()
        ##ventana
        self.root = tk.Tk()
        self.root.title("Cajero")
        self.root.geometry("749x721")
        self.root.resizable(width=0, height=0)
        self.bont1 = Boton1(self.root)

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
        self.btn1 = Button(self.root,image=self.imgbtn, command = self.btnBoton1)
        self.btn1.place(x=623,y=415)
        self.btn2 = Button(self.root,image=self.imgbtn)
        self.btn2.place(x=623,y=330)

        self.root.mainloop()
    
    def setScreen(self, posicion):
        self.ii2 = Image.open(self.getCarrusel(posicion))
        self.ii2.thumbnail((465,365))
        self.ii2 = ImageTk.PhotoImage(self.ii2)
        return self.ii2 

    def update(self):
        ##self.fondo.place(x=9999, y=9999)
        self.nfondo = Label(self.root, image=self.setScreen(0))
        self.nfondo.place(x=150,y=125)

    def btnBoton1(self):
        
        if (self.estado==1):
            self.nfondo = Label(self.root, image=self.setScreen(1))
            self.nfondo.place(x=150,y=125)
            self.bont1.registrar()
            self.estado=2
        elif(self.estado==2):
            self.n2fondo = Label(self.root, image=self.setScreen(2))
            self.n2fondo.place(x=150,y=125)
            self.datos.setUsuario(self.bont1.getNombre())
            print(self.bont1.getNombre())
            self.datos.setDocumento(self.bont1.getCedula())
            print(self.bont1.getCedula())
            self.datos.setBanco(self.bont1.getBanco())
            print(self.bont1.getBanco())
            self.datos.setClave(self.bont1.getClave())
            print(self.bont1.getClave())
            self.r = Text(self.root, width=30,height=10).place(x=250,y=150)
            self.r.insert(INSERT, 'Nombre: ' + str(self.datos.getUsuario) +'\nCedula'+str(self.datos.getDocumento)+'\nBanco: '+str(self.datos.getBanco))
            self.r.config(state=DISABLED)
            self.r.pack()
            self.estado = 3
        elif(self.estado==3):
            self.n2fondo = Label(self.root, image=self.setScreen(0))
            self.n2fondo.place(x=150,y=125)
            

            




    def getCarrusel(self, posicion):
        self.app = BuilderManager()
        self.opciones = [BuilderPantalla0(), BuilderPantalla1(),BuilderPantalla2(), BuilderAgrario(), BuilderBancolombia(), BuilderDavivienda()]
        self.app.setBuilder(self.opciones[posicion])
        return self.app.buildCajero()

    
cajero = Cajero()


