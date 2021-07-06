from Abstract.Instruccion import Instruccion
from re import T
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
        if simbolo == None: return Excepcion("Semantico", "No se encontro el parametro de Typeof", self.fila, self.columna)

        if simbolo.getTipo() != TIPO.ENTERO and simbolo.getTipo() != TIPO.DECIMAL and simbolo.getTipo() != TIPO.CADENA and simbolo.getTipo() != TIPO.BOOLEANO and simbolo.getTipo() != TIPO.CHARACTER and simbolo.getTipo() != TIPO.ARREGLO :
            return Excepcion("Semantico", "Tipo de parametro Typeof no cnoicnide", self.fila,self.columna)

        self.tipo = simbolo.getTipo()
        return self.get_tipo(simbolo.getTipo())

    def get_tipo(self, tipo):
        if tipo == TIPO.CADENA:
            return 'String'
        elif tipo == TIPO.CHARACTER:
            return 'Char'
        elif tipo == TIPO.DECIMAL:
            return 'Double'
        elif tipo == TIPO.ENTERO:
            return 'Int'
        elif tipo == TIPO.ARREGLO.ENTERO:
            return 'Arreglo -> Int'