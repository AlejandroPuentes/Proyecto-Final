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
        
        self.text1 = Label(self.root, text = "Iniciar Sesión" )
        self.text1.place(x=423, y = 455)
        self.text2 = Label(self.root, text = "Registrarse" )
        self.text2.place(x=423, y = 360)

        self.btn1 = Button(self.root,image=self.imgbtn, command = lambda: self.update(self.fondo, 1))
        self.btn1.place(x=623,y=415)
        self.btn2 = Button(self.root,image=self.imgbtn, command = lambda: self.update(self.fondo, 0))
        self.btn2.place(x=623,y=330)

        tkimage2 = ImageTk.PhotoImage(imagen2)
        fondo2 = Label(ventana,image=tkimage2, width = 445, height = 365 ).place(x=150,y=125)
        '''
    