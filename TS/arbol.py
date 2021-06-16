class Arbol: #AST Arbol sintaxis abstracta
    def __init__(self, instrucciones ):
        self.instrucciones = instrucciones
        self.excepciones = []
        self.consola = []                           #salida del interprete, todos los prints guardados
        self.Tsglobal = None

    def getInstrucciones(self):
        return self.instrucciones

    def setInstrucciones(self, instrucciones):
        self.instrucciones = instrucciones

    def getExepciones(self):
        return self.excepciones

    def setExepciones(self, excepciones):
        self.excepciones = excepciones

    def getConsola(self):
        return self.consola

    def setConsola(self,consola):
        self.consola = consola

    def getTsGlobal(self):
        return self.consola

    def setTsGlobal(self,Tsglobal):
        self.Tsglobal = Tsglobal

            

