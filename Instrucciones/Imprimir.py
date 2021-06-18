from Abstract.Instruccion import Instruccion
from TS.Excepcion import Excepcion
from TS.Tipo import Tipo

class Imprimir(Instruccion):                            #Se agrega lo que lleva el print
    def __init__(self, expresion, fila, columna):
        self.expresion = expresion
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        value = self.expresion.interpretar(tree,table)  #RETORNA CUALQUIER VALOR
        if isinstance(value, Excepcion):
            return value
        
        if self.expresion.tipo == Tipo.ARREGLO:
            return Excepcion("Semantico", "No se puede imprimir un arreglo completo", self.fila, self.columna)

        tree.updateConsola(value)
        return None

    

