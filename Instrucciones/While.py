from Instrucciones.Break import Break
from Abstract.Instruccion import Instruccion
from TS.Excepcion import Excepcion
from TS.Tipo import Tipo
from TS.Tabla_Simbolo import Tabla_Simbolos
from Instrucciones.Break import Break

class While(Instruccion):
    def __init__(self, condicion, instrucciones, fila, columna):
        self.condicion = condicion
        self.instrucciones = instrucciones
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):

        while True:
            condicion = self.condicion.interpretar(tree, table)
            if isinstance(condicion, Exception): return Excepcion

            if self.condicion.tipo == Tipo.BOOLEANO:
                if bool(condicion) == True:                                                                               #VERIFICA SI ES TRUE LA CONDICION            
                    nuevaTabla = Tabla_Simbolos(table)
                    for instruccion in self.instrucciones:                                                #Nuevo Entorno
                        result = instruccion.interpretar(tree,nuevaTabla)                                   #EJECUTA INSTRUCCION ADENTRO DEL IF
                        if isinstance(result, Excepcion):
                            tree.getExcepciones().append(result)
                            tree.updateConsola(result.toString())
                        if isinstance(result, Break): return None
                else:
                    break
            else:
                return Excepcion("Semantico", "Tipo de dato no booleado en IF.", self.fila, self.columna)