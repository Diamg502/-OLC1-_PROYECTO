
from Abstract.NodoAST import NodoAST
from Abstract.Instruccion import Instruccion


class Case(Instruccion):
    def __init__(self, expresion,instrucciones, fila, columna):
        self.expresion = expresion
        self.instrucciones = instrucciones
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        return self.expresion.interpretar(tree,table)

    def getNodo(self):                                  #VERIFICAR MAS ADELANTE
        nodo = NodoAST("CASE")
        nodo.agregarHijo(str(self.instrucciones))
        nodo.agregarHijoNodo(self.expresion.getNodo())
        return nodo

        
        