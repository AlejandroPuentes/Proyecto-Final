from abc import ABC, abstractmethod

class AbstractProducto(ABC):

        @abstractmethod
        def dibujar(self):
            pass

class Pantalla0(AbstractProducto):
    def dibujar(self):
        ##imagen de pantalla
        imagen = Image.open("Sprites/Pantalla/0.png")
        imagen.thumbnail((465,365))

class Pantalla1(AbstractProducto):
    def dibujar(self):
        ##imagen de pantalla
        imagen = Image.open("Sprites/Pantalla/1.png")
        imagen.thumbnail((465,365))

class PantallaAgrario(AbstractProducto):
    def dibujar(self):
        ##imagen de pantalla
        imagen = Image.open("Sprites/Pantalla/Agrario.png")
        imagen.thumbnail((465,365))

class PantallaBancolombia(AbstractProducto):
    def dibujar(self):
        ##imagen de pantalla
        imagen = Image.open("Sprites/Pantalla/Bancolombia.png")
        imagen.thumbnail((465,365))

class PantallaDavivienda(AbstractProducto):
    def dibujar(self):
        ##imagen de pantalla
        imagen = Image.open("Sprites/Pantalla/Davivienda.png")
        imagen.thumbnail((465,365))