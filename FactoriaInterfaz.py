from abc import ABC, abstractmethod

from ProductoInterfaz import *

class AbstractInterfaz(ABC):
    
    @abstractmethod
    def crearPantalla(self):
        pass

class FabricaScreenPrincipal(AbstractInterfaz):

    def crearPantalla(self):
        return Pantalla0()


class FabricaScreens(AbstractInterfaz):

    def crearPantalla(self):
        return Pantalla1()


class FabricaAgrario(AbstractInterfaz):

    def crearPantalla(self):
        return PantallaAgrario()


class FabricaBancolombia(AbstractInterfaz):

    def crearPantalla(self):
        return PantallaBancolombia()
        

class FabricaDavivienda(AbstractInterfaz):

    def crearPantalla(self):
        return PantallaDavivienda()
        