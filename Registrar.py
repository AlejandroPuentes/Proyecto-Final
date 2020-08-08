class registro ():
    def __init__(self ):
        self.usuario = None
        self.documento = None
        self.clave = None
        self.banco = None
    
    def setUsuario(self,usuario):
        self.usuario = usuario

    def getUsuario(self):
        return self.usuario

    def setDocumento(self,docu):
        self.documento = docu

    def getDocumento(self):
        return self.documento

    def setClave(self,clave):
        self.clave = clave

    def getClave(self):
        return self.clave

    def setBanco(self,banco):
        self.banco = banco

    def getBanco(self):
        return self.banco