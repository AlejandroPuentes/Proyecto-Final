from Builder import *
from Cajero import *

app = BuilderManager()

opciones = [BuilderPantalla0(), BuilderPantalla1(), BuilderAgrario(), BuilderBancolombia(), BuilderDavivienda()]

app.setBuilder(opciones[0])
app.buildCajero()