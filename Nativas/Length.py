from TS.Excepcion import Excepcion
from TS.Tipo import TIPO
from Instrucciones.Funcion import Funcion
import math

class Length(Funcion):
    def __init__(self, nombre, parametros, instrucciones, fila, columna):
        self.nombre = nombre.lower()
        self.parametros = parametros
        self.instrucciones = instrucciones
        self.fila = fila
        self.columna = columna
        self.tipo = TIPO.NULO

    def interpretar(self, tree, table):
        aux = ""
        simbolo = table.getTabla("length##param1")
        if simbolo == None: return Excepcion("Semantico", "No se encontro el parametro de length", self.fila, self.columna)

        if simbolo.getTipo() != TIPO.ARREGLO and simbolo.getTipo() != TIPO.CADENA:
            return Excepcion("Semantico", "Tipo de parametro Length no cnoicnide", self.fila,self.columna)

        if simbolo.getTipo() == TIPO.ENTERO:
            aux = str(simbolo.getValor())
        else:
            aux = simbolo.getValor()


        self.tipo = simbolo.getTipo()
        return len(aux)