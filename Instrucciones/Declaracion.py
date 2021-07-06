from Abstract.NodoAST import NodoAST
from TS.Tipo import TIPO
from TS.Excepcion import Excepcion
from Abstract.Instruccion import Instruccion
from TS.Simbolo import Simbolo


class Declaracion(Instruccion):
    def __init__(self, identificador, fila, columna, expresion=None):
        self.identificador = identificador
        self.expresion = expresion
        self.fila = fila
        self.columna = columna
        self.arreglo = False

    def interpretar(self, tree, table):
        if self.expresion != None:
            value = self.expresion.interpretar(tree, table) # Valor a asignar a la variable
            if isinstance(value, Excepcion): return value
            simbolo = Simbolo(str(self.identificador), self.expresion.tipo,self.arreglo, self.fila, self.columna, value)
            result = table.setTabla(simbolo)
            if isinstance(result, Excepcion): return result
            return None
        else:
            #value = self.expresion.interpretar(tree, table) # Valor a asignar a la variable
            value = "Null"
            if isinstance(value, Excepcion): return value
            simbolo = Simbolo(str(self.identificador), TIPO.NULO,self.arreglo, self.fila, self.columna, value)
            result = table.setTabla(simbolo)
            if isinstance(result, Excepcion): return result
            return None

    def getNodo(self):
        nodo = NodoAST("DECLARACION")
        nodo.agregarHijo(str(self.identificador))
        if self.expresion != None:
            nodo.agregarHijoNodo(self.expresion.getNodo())
        else:
            vvalue = "NULL"
            nodo.agregarHijoNodo(vvalue)
        return nodo
