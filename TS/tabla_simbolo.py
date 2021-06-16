

from TS.exception import exepcion


class TablaSimbolos:
    def __init__(self, anterior = None):
        self.tabla = {}                                                      #diccionario vacio
        self.anterior = anterior
        self.funciones = []

    def setTabla(self, simbolo):                                             #agregar una variable
        if simbolo.id in self.tabla :                                        #verifica que no se declare una variable mas de una vez
            return exepcion("semantico", "variable" + simbolo.id + "ya existe", simbolo.fila, simbolo.columna)
        else:                                                                #Si no existe se agrega a la tabla de simbolos
            self.tabla[simbolo.id] = simbolo
            return None

    def getTabla(self, id):                                                  #Obtener una variable de la tabla
        tablaActual = self
        while tablaActual != None:
            if id in self.tabla : 
                return self.tabla[id]
            else:
                tablaActual = tablaActual.anterior
        return None

    def actualizarTabla(self, simbolo):                                     #Cambiar el contenido de una variable
        tablaActual = self
        while tablaActual != None:
            if simbolo.id in self.tabla : 
                self.tabla[simbolo.id].setValor(simbolo.getValor())
                self.tabla[simbolo.id].setTipo(simbolo.getTipo())
                return "Variable actualizada"
            else:
                tablaActual = tablaActual.anterior
        return None
