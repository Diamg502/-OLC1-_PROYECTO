from Abstract.NodoAST import NodoAST
from TS.Tipo import OperadorAritmetico, TIPO
from TS.Excepcion import Excepcion
from Abstract.Instruccion import Instruccion
from TS.Simbolo import Simbolo
from Expresiones.Identificador import Identificador


class MasMenos(Instruccion):
    def __init__(self, identificador, expresion, fila, columna):
        self.identificador = identificador
        self.expresion = expresion
        self.fila = fila
        self.columna = columna
        self.arreglo = False
        self.tipo = None

    def interpretar(self, tree, table):

        if isinstance(self.expresion, Identificador):

            value = self.expresion.interpretar(tree, table) # Valor a asignar a la variable

            if isinstance(value, Excepcion): return value

            if self.expresion.getTipo() in (TIPO.ENTERO, TIPO.DECIMAL):

                if self.identificador == OperadorAritmetico.INC:
                    symbol = Simbolo(self.expresion.getID(),self.expresion.getTipo(),self.arreglo,self.fila,self.columna,value+1)
                elif self.identificador == OperadorAritmetico.DEC:
                    symbol = Simbolo(self.expresion.getID(),self.expresion.getTipo(),self.arreglo,self.fila,self.columna,value-1)
                    
                result = table.actualizarTabla(symbol)

                if isinstance(result,Excepcion): return result

                self.tipo = self.expresion.getTipo()
                return symbol.getValor()
            else:
                return Excepcion("Semantico", "Tipo de OPERADOR Diferente en Asignacion", self.getFila(), self.getColumna())
        else:
            return Excepcion("Semantico", "Tipo de VARIABLE Diferente en Asignacion", self.getFila(), self.getColumna())

    def getNodo(self):
        nodo = NodoAST("INCREMENTO")
        nodo.agregarHijo(str(self.identificador))
        nodo.agregarHijoNodo(self.expresion.getNodo())
        return nodo

    
    def set_exp(self,exp):
        self.expresion = exp

    def get_exp(self):
        return self.expresion

    def getType(self):
        return self.tipo        


