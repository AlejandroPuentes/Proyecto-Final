from abc import ABC, abstractmethod

from FactoriaInterfaz import *
from Cajero import *

class AbstractBuilder(ABC):

    @abstractmethod
    def __init__(self):
        self.Cajero = None
        self.AbstractInterfaz = None
    
    def buildPantalla(self):
        pass

class BuilderPantalla0(AbstractBuilder):

    def __init__(self):
        self.Cajero = Cajero()
        self.AbstractInterfaz = FabricaScreenPrincipal()
    
    def buildPantalla(self):
        self.Cajero.setFondoPantalla(self.AbstractInterfaz.crearPantalla())

class BuilderPantalla1(AbstractBuilder):

    def __init__(self):
        self.Cajero = Cajero()
        self.AbstractInterfaz = FabricaScreens()
    
    def buildPantalla(self):
        self.Cajero.setFondoPantalla(self.AbstractInterfaz.crearPantalla())

class BuilderAgrario(AbstractBuilder):

    def __init__(self):
        self.Cajero = Cajero()
        self.AbstractInterfaz = FabricaAgrario()
    
    def buildPantalla(self):
        self.Cajero.setFondoPantalla(self.AbstractInterfaz.crearPantalla())

class BuilderBancolombia(AbstractBuilder):

    def __init__(self):
        self.Cajero = Cajero()
        self.AbstractInterfaz = FabricaBancolombia()
    
    def buildPantalla(self):
        self.Cajero.setFondoPantalla(self.AbstractInterfaz.crearPantalla())

class BuilderDavivienda(AbstractBuilder):

    def __init__(self):
        self.Cajero = Cajero()
        self.AbstractInterfaz = FabricaDavivienda()
    
    def buildPantalla(self):
        self.Cajero.setFondoPantalla(self.AbstractInterfaz.crearPantalla())

class BuilderManager():

    def __init__(self):
        self.builder = None
    
    def setBuilder(self, builder):
        self.builder = builder
    
    def buildCajero(self):
        self.builder.buildPantalla()
    
    ##def getCajero(self):
        ##return self.builder.getCajero()