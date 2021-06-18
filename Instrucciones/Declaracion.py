from TS.Excepcion import Excepcion
from Abstract.Instruccion import Instruccion
from TS.Simbolo import Simbolo



class Declaracion(Instruccion):
    def __init__(self, tipo, identificador, fila, columna, expresion=None):
        self.identificador = identificador
        self.tipo = tipo
        self.expresion = expresion
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        value = self.expresion.interpretar(tree,table)                                                      #Valor asignar a la variable
        if isinstance(value, Exception): return value

        if self.tipo == self.expresion.tipo:                                                                #NO ES OBLIGATORIA
            return Excepcion("Semantico", "Tipo de dato diferente en Declaracion", self.fila, self.columna) #NO ES OBLIGATORIA

        simbolo = Simbolo(str(self.identificador), self.tipo, self.fila, self.columna, value)

        result = table.setTabla(simbolo)

        if isinstance(result, Excepcion): return result
        return None

        


