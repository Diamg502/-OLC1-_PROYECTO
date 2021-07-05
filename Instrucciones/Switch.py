from Abstract.NodoAST import NodoAST
from Abstract.Instruccion import Instruccion
from TS.Excepcion import Excepcion
from TS.TablaSimbolos import TablaSimbolos
from Instrucciones.Return import Return
from Instrucciones.Break import Break


class Switch(Instruccion):
    def __init__(self, expresion,casos, default,fila, columna):
        self.expresion = expresion
        self.casos = casos
        self.defult = default
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        if self.casos != None:
            var1 = self.expresion.interpretar(tree,table)
            for caso in self.casos:
                var2 = caso.interpretar(tree,table)
                if var1 == var2:
                    nuevaTabla = TablaSimbolos(table)
                    for instruccion in caso.instrucciones:
                        result = instruccion.interpretar(tree, nuevaTabla) #EJECUTA INSTRUCCION ADENTRO DEL IF
                        if isinstance(result, Excepcion) :
                            tree.getExcepciones().append(result)
                            tree.updateConsola(result.toString())
                        if isinstance(result, Break): return None
                        if isinstance(result, Return): return result

        if self.defult !=None:
            nuevaTabla = TablaSimbolos(table)
            for instruccion in self.defult:
                result = instruccion.interpretar(tree, nuevaTabla) #EJECUTA INSTRUCCION ADENTRO DEL IF
                if isinstance(result, Excepcion) :
                    tree.getExcepciones().append(result)
                    tree.updateConsola(result.toString())
                if isinstance(result, Break): return None
                if isinstance(result, Return): return result
            pass

    def getNodo(self):                                      #VERIFICAR DESPUES
        nodo = NodoAST("SWITCH")
        nodo.agregarHijoNodo(self.expresion.getNodo())

        
        casos = NodoAST("SWITCH CASOS")
        for instr in self.casos:
            casos.agregarHijoNodo(instr.getNodo())
        nodo.agregarHijoNodo(casos)

        default = NodoAST("INSTRUCCIONES DEFAULT ")
        default.agregarHijoNodo(instr.getNodo())

        return nodo        
    