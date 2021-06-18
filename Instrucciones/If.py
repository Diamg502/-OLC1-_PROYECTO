from Abstract.Instruccion import Instruccion
from TS.Excepcion import Excepcion
from TS.Tipo import Tipo
from TS.Tabla_Simbolo import Tabla_Simbolos
from Instrucciones.Break import Break

class If(Instruccion):
    def __init__(self, condicion, instruccionesIf, instruccionesElse, ElseIf, fila, columna):
        self.condicion = condicion
        self.instruccionesIf = instruccionesIf
        self.instruccionesElse = instruccionesElse
        self.ElseIf = ElseIf
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        condicion = self.condicion.interpretar(tree, table)
        if isinstance(condicion, Exception): return Excepcion

        if self.condicion.tipo == Tipo.BOOLEANO:
            if bool(condicion) == True:                                                                               #VERIFICA SI ES TRUE LA CONDICION            
                nuevaTabla = Tabla_Simbolos(table)
                for instruccion in self.instruccionesIf:                                                #Nuevo Entorno
                    result = instruccion.interpretar(tree,nuevaTabla)                                   #EJECUTA INSTRUCCION ADENTRO DEL IF
                    if isinstance(result, Excepcion):
                        tree.getExcepciones().append(result)
                        tree.updateConsola(result.toString())
                    if isinstance(result, Break): return result
            else:                                                                                           #ELSE
                if self.instruccionesElse != None:
                    nuevaTabla = Tabla_Simbolos(table)
                    for instruccion in self.instruccionesElse:
                        result = instruccion.interpretar(tree,nuevaTabla)
                        if isinstance(result, Excepcion):
                            tree.getExcepciones().append(result)
                            tree.updateConsola(result.toString())
                elif self.ElseIf != None:
                    result = self.ElseIf.interpretar(tree, table)
                    if isinstance(result, Excepcion): return result
                    if isinstance(result, Break): return result

        else:
            return Excepcion("Semantico", "Tipo de dato no booleado en IF.", self.fila, self.columna)