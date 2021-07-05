from TS.Excepcion import Excepcion
from TS.Tipo import TIPO
from Instrucciones.Funcion import Funcion
import math

class TypeOf(Funcion):
    def __init__(self, nombre, parametros, instrucciones, fila, columna):
        self.nombre = nombre.lower()
        self.parametros = parametros
        self.instrucciones = instrucciones
        self.fila = fila
        self.columna = columna
        self.tipo = TIPO.NULO

    def interpretar(self, tree, table):
        simbolo = table.getTabla("typeof##param1")
        if simbolo == None: return Excepcion("Semantico", "No se encontro el parametro de truncate", self.fila, self.columna)

        if simbolo.getTipo() != TIPO.ENTERO and simbolo.getTipo() != TIPO.DECIMAL and simbolo.getTipo() != TIPO.CADENA and simbolo.getTipo() != TIPO.BOOLEANO and simbolo.getTipo() != TIPO.CHARACTER:
            return Excepcion("Semantico", "Tipo de parametro Typeof no cnoicnide", self.fila,self.columna)

        self.tipo = simbolo.getTipo()
        return simbolo.getTipo()