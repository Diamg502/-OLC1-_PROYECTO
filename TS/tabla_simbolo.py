

from TS.Simbolo import Simbolo
from TS.Excepcion import exepcion


class Tabla_Simbolos:
    def __init__(self, anterior = None):
        self.tabla = {}                                                      #diccionario vacio
        self.anterior = anterior
        self.funciones = []

    def setTabla(self, simbolo):                                             #agregar una variable
        if simbolo.id.lower() in self.tabla :                                        #verifica que no se declare una variable mas de una vez
            return exepcion("semantico", "variable" + simbolo.id + "ya existe", simbolo.fila, simbolo.columna)
        else:                                                                #Si no existe se agrega a la tabla de simbolos
            self.tabla[simbolo.id.lower()] = simbolo
            return None

    def getTabla(self, id):                                                  #Obtener una variable de la tabla
        tablaActual = self
        while tablaActual.tabla != None:
            if id in tablaActual.tabla: 
                return tablaActual.tabla[id]                                        #Retorna un simbolo
            else:
                tablaActual = tablaActual.anterior
        return None

    def actualizarTabla(self, simbolo):                                     #Cambiar el contenido de una variable
        tablaActual = self
        while tablaActual != None:
            if simbolo.id in self.tabla : 
                if self.tabla[simbolo.id].getTipo() == simbolo.getTipo(): #para cambiarle el valor a nulo: or simbolo.getTipo == Tipo.NUL-----------------------
                    self.tabla[simbolo.id].setValor(simbolo.getValor())
                    self.tabla[simbolo.id].setTipo(simbolo.getTipo())
                    return None                                                 #Variable Actualizada
                return Exception("Semantico", "Tipo de dato diferente a la asignacion", simbolo.getFila(), simbolo.getColumna)
            else:
                tablaActual = tablaActual.anterior
        return Exception("Semantico", "Variable no encontrada en Asignacion", simbolo.getFila(), simbolo.getColumna)
