from Abstract.NodoAST import NodoAST
from Abstract.Instruccion import Instruccion
from TS.Excepcion import Excepcion
from TS.Tipo import TIPO
from TS.TablaSimbolos import TablaSimbolos

class Default(Instruccion):
    def __init__(self,instrucciones, fila, columna):
        self.instrucciones = instrucciones
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        result = self.instrucciones.interpretar(tree, table)
        if isinstance(result, Excepcion): return result

        self.tipo = self.expresion.tipo #TIPO DEL RESULT
        self.result = result            #VALOR DEL RESULT

        return self

    def getNodo(self):
        nodo = NodoAST("DEFAULT")                           # REVISAR DESPUES
        instrucciones = NodoAST("INSTRUCCIONES")
        for instr in self.instrucciones:
            instrucciones.agregarHijoNodo(instr.getNodo())
        nodo.agregarHijoNodo(instrucciones)
        return nodo    