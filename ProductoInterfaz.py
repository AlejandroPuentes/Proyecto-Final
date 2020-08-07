from abc import ABC, abstractmethod

import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk

class AbstractProducto(ABC):

    @abstractmethod
    def __init__(self):
        pass

    def getImage(self):
        pass


class Pantalla0(AbstractProducto):
    def __init__(self):
        self.image = 'Sprites/Pantalla/0.png'

    def getImage(self):
        return self.image

class Pantalla1(AbstractProducto):
    def __init__(self):
        self.image = 'Sprites/Pantalla/1.png'

class PantallaAgrario(AbstractProducto):
    def __init__(self):
        self.image = 'Sprites/Pantalla/Agrario.png'

class PantallaBancolombia(AbstractProducto):
    def __init__(self):
        self.image = 'Sprites/Pantalla/Bancolombia.png'

class PantallaDavivienda(AbstractProducto):
    def __init__(self):
        self.image = 'Sprites/Pantalla/Davivienda.png'