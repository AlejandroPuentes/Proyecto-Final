import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk

colorFondo = "#006"
colorLetra = "#fff"
##ventana
ventana = tk.Tk()
ventana.title("Cajero")
ventana.geometry("749x721")
ventana.resizable(width=0, height=0)
ventana.configure(background=colorFondo)


##fondo
image = Image.open("Sprites/Cajero/DiseñoSprites.png")
image.thumbnail((749,721))
tkimage = ImageTk.PhotoImage(image)
bckground = Label(ventana, image=tkimage, width = 1000, height = 980).pack()
##imagen de pantalla
imagen2 = Image.open("Sprites/Pantalla/Davivienda.png")
imagen2.thumbnail((465,365))
tkimage2 = ImageTk.PhotoImage(imagen2)
fondo2 = Label(ventana,image=tkimage2,width =445,height = 365 ).place(x=150,y=125)

#botones
img = Image.open("Sprites/Button/1.png")
img = img.resize((100, 65), Image.ANTIALIAS) # Redimension (Alto, Ancho)
img = ImageTk.PhotoImage(img)
btn1 = Button(ventana,image=img,text="Hola").place(x=20,y=415)
btn2 = Button(ventana,image=img,text="Hola").place(x=623,y=415)
btn3 = Button(ventana,image=img,text="Hola").place(x=20,y=330)
btn4 = Button(ventana,image=img,text="Hola").place(x=623,y=330)
btn5 = Button(ventana,image=img,text="Hola").place(x=20,y=250)
btn4 = Button(ventana,image=img,text="Hola").place(x=623,y=250)


ventana.mainloop()