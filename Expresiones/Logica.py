from Abstract.Instruccion import Instruccion
from TS.Excepcion import Excepcion
from TS.Tipo import Tipo, OperadorLogico

class Logica(Instruccion):
    def __init__(self, operador, OperacionIzq, OperacionDer, fila, columna):
        self.operador = operador
        self.OperadorIzq = OperacionIzq
        self.OperadorDer = OperacionDer
        self.fila = fila
        self.columna = columna
        self.tipo = Tipo.BOOLEANO

    def interpretar(self, tree, table):
        izq = self.OperadorIzq.interpretar(tree,table)
        if isinstance(izq, Excepcion): return izq
        if self.OperadorDer != None:
            der = self.OperadorDer.interpretar(tree,table)
            if isinstance(der, Excepcion): return der
        if self.operador == OperadorLogico.AND:                                                     #AND       AGREGAR TODOS LOS TIPOS            
            if self.OperadorIzq.tipo == Tipo.BOOLEANO and self.OperadorDer.tipo == Tipo.BOOLEANO:             
                return self.obtenerVal(self.OperadorIzq.tipo, izq) and self.obtenerVal(self.OperadorIzq.tipo, der)
            return Excepcion("Semantico", "TIpo Erroneo de operacion para &&.", self.fila,self.columna)
        elif self.operador == OperadorLogico.OR:                                                     #OR       AGREGAR TODOS LOS TIPOS            
            if self.OperadorIzq.tipo == Tipo.BOOLEANO and self.OperadorDer.tipo == Tipo.BOOLEANO:             
                return self.obtenerVal(self.OperadorIzq.tipo, izq) or self.obtenerVal(self.OperadorIzq.tipo, der)
            return Excepcion("Semantico", "TIpo Erroneo de operacion para ||.", self.fila,self.columna)
        elif self.operador == OperadorLogico.NOT:                                                     #NOT       AGREGAR TODOS LOS TIPOS            
            if self.OperadorIzq.tipo == Tipo.BOOLEANO:             
                return not self.obtenerVal(self.OperadorIzq.tipo, izq)
            return Excepcion("Semantico", "TIpo Erroneo de operacion para !.", self.fila,self.columna)
        return Excepcion("Semantico", "TIpo de operacion no especificado.", self.fila,self.columna)
    
    def obtenerVal(self, tipo, val):
        if tipo == Tipo.ENTERO:
            return int(val)
        elif tipo == Tipo.DECIMAL:
            return float(val)
        elif tipo == Tipo.BOOLEANO:
            return bool(val)
        return str(val)