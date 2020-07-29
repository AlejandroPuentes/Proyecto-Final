import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk

colorFondo = "#006"
colorLetra = "#fff"

ventana = tk.Tk()
ventana.title("Cajero")
ventana.geometry("749x721")
ventana.resizable(width=0, height=0)
ventana.configure(background=colorFondo)
#Imagenes
'''imagen = PhotoImage(file="Cajero/DiseñoSprites.png")
fondo = Label(ventana,image=imagen).place(x=0,y=0)
imagen2 = PhotoImage(file="Cajero/Davivienda.png")

fondo2 = Label(ventana,image=imagen2).place(x=200,y=200)'''
image = Image.open("Cajero/DiseñoSprites.png")
image.thumbnail((749,721))
tkimage = ImageTk.PhotoImage(image)
bckground = Label(ventana, image=tkimage, width = 1000, height = 980).pack()
imagen2 = PhotoImage(file="Cajero/BancoAgrario_opt.png")
fondo2 = Label(ventana,image=imagen2).place(x=150,y=125)

#botones
img = Image.open("Cajero/1.png")
img = img.resize((100, 65), Image.ANTIALIAS) # Redimension (Alto, Ancho)
img = ImageTk.PhotoImage(img)
btn1 = Button(ventana,image=img,text="Hola").place(x=20,y=415)
btn2 = Button(ventana,image=img,text="Hola").place(x=623,y=415)
btn3 = Button(ventana,image=img,text="Hola").place(x=20,y=330)
btn4 = Button(ventana,image=img,text="Hola").place(x=623,y=330)
btn5 = Button(ventana,image=img,text="Hola").place(x=20,y=250)
btn4 = Button(ventana,image=img,text="Hola").place(x=623,y=250)


ventana.mainloop()