from Builder import *

import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk

app = BuilderManager()

opciones = [BuilderPantalla0(), BuilderPantalla1(), BuilderAgrario(), BuilderBancolombia(), BuilderDavivienda()]

app.setBuilder(opciones[0])

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

#Botones
img = Image.open("Sprites/Button/1.png")
img = img.resize((100, 65), Image.ANTIALIAS) # Redimension (Alto, Ancho)
img = ImageTk.PhotoImage(img)

##imagen de pantalla
imagen = Image.open(app.buildCajero())
imagen.thumbnail((465,365))
tkimage2 = ImageTk.PhotoImage(imagen)
fondo2 = Label(ventana,image=tkimage2, width = 445, height = 365 ).place(x=150,y=125)
text1 = Label(ventana, text = "Iniciar Sesión" ).place(x=423, y = 455)
text2 = Label(ventana, text = "Registrarse" ).place(x=423, y = 360)
btn1 = Button(ventana,image=img).place(x=623,y=415)
btn2 = Button(ventana,image=img,).place(x=623,y=330)

ventana.mainloop()