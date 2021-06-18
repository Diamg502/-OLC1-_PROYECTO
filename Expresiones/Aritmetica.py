from Abstract.Instruccion import Instruccion
from TS.Excepcion import Excepcion
from TS.Tipo import Tipo, OperadorAritmetico

class Aritmetica(Instruccion):
    def __init__(self, operador, OperacionIzq, OperacionDer, fila, columna):
        self.operador = operador
        self.OperadorIzq = OperacionIzq
        self.OperadorDer = OperacionDer
        self.fila = fila
        self.columna = columna
        self.tipo = None

    def interpretar(self, tree, table):
        izq = self.OperadorIzq.interpretar(tree,table)
        if isinstance(izq, Excepcion): return izq
        if self.OperadorDer != None:
            der = self.OperadorDer.interpretar(tree,table)
            if isinstance(der, Excepcion): return der
        
        if self.operador == OperadorAritmetico.MAS:                                                     #SUMA       AGREGAR TODOS LOS TIPOS
            if self.OperadorIzq.tipo == Tipo.ENTERO and self.OperadorDer.tipo == Tipo.ENTERO:
                self.tipo = Tipo.ENTERO
                return self.obtenerVal(self.OperadorIzq.tipo, izq) + self.obtenerVal(self.OperadorIzq.tipo, der)
            elif self.OperadorIzq.tipo == Tipo.ENTERO and self.OperadorDer.tipo == Tipo.DECIMAL:
                self.tipo = Tipo.DECIMAL
                return self.obtenerVal(self.OperadorIzq.tipo, izq) + self.obtenerVal(self.OperadorIzq.tipo, der)
            elif self.OperadorIzq.tipo == Tipo.ENTERO and self.OperadorDer.tipo == Tipo.CADENA:
                self.tipo = Tipo.CADENA
                return str(self.obtenerVal(self.OperadorIzq.tipo, izq)) + self.obtenerVal(self.OperadorIzq.tipo, der)
            return Excepcion("Semantico", "TIpo Erroneo de operacion para +.", self.fila,self.columna)
        elif self.operador == OperadorAritmetico.MENOS:                                                            #RESTA 
            if self.OperadorIzq.tipo == Tipo.ENTERO and self.OperadorDer.tipo == Tipo.ENTERO:
                self.tipo = Tipo.ENTERO
                return self.obtenerVal(self.OperadorIzq.tipo, izq) - self.obtenerVal(self.OperadorIzq.tipo, der)
            return Excepcion("Semantico", "TIpo Erroneo de operacion para -.", self.fila,self.columna)
        elif self.operador == OperadorAritmetico.UMENOS:                                                           #UMENOS  NEGACION UNARIA
            if self.OperadorIzq.tipo == Tipo.ENTERO:
                self.tipo = Tipo.ENTERO
                return - self.obtenerVal(self.OperadorIzq.tipo, izq)
            elif self.OperadorIzq.tipo == Tipo.DECIMAL:
                self.tipo = Tipo.DECIMAL
                return - self.obtenerVal(self.OperadorIzq.tipo, izq)
            return Excepcion("Semantico", "TIpo Erroneo de operacion para - unario.", self.fila,self.columna)
        return Excepcion("Semantico", "TIpo de operacion o especificado.", self.fila,self.columna)

    def obtenerVal(self, tipo, val):
        if tipo == Tipo.ENTERO:
            return int(val)
        elif tipo == Tipo.DECIMAL:
            return float(val)
        elif tipo == Tipo.BOOLEANO:
            return bool(val)
        return str(val)

    