import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk

class Cajero():

    def __init__(self):

        self.fondoPantalla = None

    def setFondoPantalla(self, fondoPantalla):

        self.fondoPantalla = fondoPantalla
    
    def getFondoPantalla(self):

        return self.fondoPantalla

        
