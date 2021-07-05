from TS.Excepcion import Excepcion
from TS.Tipo import TIPO
from Instrucciones.Funcion import Funcion
import math

class Round(Funcion):
    def __init__(self, nombre, parametros, instrucciones, fila, columna):
        self.nombre = nombre.lower()
        self.parametros = parametros
        self.instrucciones = instrucciones
        self.fila = fila
        self.columna = columna
        self.tipo = TIPO.NULO

    def interpretar(self, tree, table):
        simbolo = table.getTabla("round##param1")
        if simbolo == None: return Excepcion("Semantico", "No se encontro el parametro de Round", self.fila, self.columna)

        if simbolo.getTipo() != TIPO.DECIMAL:
            return Excepcion("Semantico", "Tipo de parametro Round no cnoicnide", self.fila,self.columna)

        self.tipo = simbolo.getTipo()

        aux = math.trunc(simbolo.getValor())  #5
        aux2 = simbolo.getValor()-aux   #5.5-5
        resultado = 0
        
        if aux2 >= 0.5:
            resultado = math.ceil(simbolo.getValor())
        else:
            resultado = math.floor(simbolo.getValor())


        return resultado