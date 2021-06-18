from Abstract.Instruccion import Instruccion
from TS.Excepcion import Excepcion
from TS.Tipo import Tipo, OperadorRelacional

class Relacional(Instruccion):
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
        der = self.OperadorDer.interpretar(tree,table)
        if isinstance(der, Excepcion): return der

        if self.operador == OperadorRelacional.MENOR:                                                     #SUMA       AGREGAR TODOS LOS TIPOS
            if self.OperadorIzq.tipo == Tipo.ENTERO and self.OperadorDer.tipo == Tipo.ENTERO:             
                return self.obtenerVal(self.OperadorIzq.tipo, izq) < self.obtenerVal(self.OperadorIzq.tipo, der)
            elif self.OperadorIzq.tipo == Tipo.ENTERO and self.OperadorDer.tipo == Tipo.DECIMAL:             
                return self.obtenerVal(self.OperadorIzq.tipo, izq) < self.obtenerVal(self.OperadorIzq.tipo, der)
            elif self.OperadorIzq.tipo == Tipo.DECIMAL and self.OperadorDer.tipo == Tipo.ENTERO:             
                return self.obtenerVal(self.OperadorIzq.tipo, izq) < self.obtenerVal(self.OperadorIzq.tipo, der)
            elif self.OperadorIzq.tipo == Tipo.DECIMAL and self.OperadorDer.tipo == Tipo.DECIMAL:             
                return self.obtenerVal(self.OperadorIzq.tipo, izq) < self.obtenerVal(self.OperadorIzq.tipo, der)
            elif self.OperadorIzq.tipo == Tipo.BOOLEANO and self.OperadorDer.tipo == Tipo.BOOLEANO:             
                return self.obtenerVal(self.OperadorIzq.tipo, izq) < self.obtenerVal(self.OperadorIzq.tipo, der)
            return Excepcion("Semantico", "TIpo Erroneo de operacion para <.", self.fila,self.columna)

        elif self.operador == OperadorRelacional.MAYOR:                                                           #RESTA 
            if self.OperadorIzq.tipo == Tipo.ENTERO and self.OperadorDer.tipo == Tipo.ENTERO:             
                return self.obtenerVal(self.OperadorIzq.tipo, izq) > self.obtenerVal(self.OperadorIzq.tipo, der)  #True / False
            elif self.OperadorIzq.tipo == Tipo.ENTERO and self.OperadorDer.tipo == Tipo.DECIMAL:             
                return self.obtenerVal(self.OperadorIzq.tipo, izq) > self.obtenerVal(self.OperadorIzq.tipo, der)
            elif self.OperadorIzq.tipo == Tipo.DECIMAL and self.OperadorDer.tipo == Tipo.ENTERO:             
                return self.obtenerVal(self.OperadorIzq.tipo, izq) > self.obtenerVal(self.OperadorIzq.tipo, der)
            elif self.OperadorIzq.tipo == Tipo.DECIMAL and self.OperadorDer.tipo == Tipo.DECIMAL:             
                return self.obtenerVal(self.OperadorIzq.tipo, izq) > self.obtenerVal(self.OperadorIzq.tipo, der)
            elif self.OperadorIzq.tipo == Tipo.BOOLEANO and self.OperadorDer.tipo == Tipo.BOOLEANO:             
                return self.obtenerVal(self.OperadorIzq.tipo, izq) > self.obtenerVal(self.OperadorIzq.tipo, der)
            return Excepcion("Semantico", "TIpo Erroneo de operacion para >.", self.fila,self.columna)
        
        elif self.operador == OperadorRelacional.IGUALIGUAL:                                                           #RESTA 
            if self.OperadorIzq.tipo == Tipo.ENTERO and self.OperadorDer.tipo == Tipo.ENTERO:             
                return self.obtenerVal(self.OperadorIzq.tipo, izq) == self.obtenerVal(self.OperadorIzq.tipo, der)  #True / False
            elif self.OperadorIzq.tipo == Tipo.ENTERO and self.OperadorDer.tipo == Tipo.DECIMAL:             
                return self.obtenerVal(self.OperadorIzq.tipo, izq) == self.obtenerVal(self.OperadorIzq.tipo, der)
            elif self.OperadorIzq.tipo == Tipo.DECIMAL and self.OperadorDer.tipo == Tipo.ENTERO:             
                return self.obtenerVal(self.OperadorIzq.tipo, izq) == self.obtenerVal(self.OperadorIzq.tipo, der)
            elif self.OperadorIzq.tipo == Tipo.DECIMAL and self.OperadorDer.tipo == Tipo.DECIMAL:             
                return self.obtenerVal(self.OperadorIzq.tipo, izq) == self.obtenerVal(self.OperadorIzq.tipo, der)
            elif self.OperadorIzq.tipo == Tipo.BOOLEANO and self.OperadorDer.tipo == Tipo.BOOLEANO:             
                return self.obtenerVal(self.OperadorIzq.tipo, izq) == self.obtenerVal(self.OperadorIzq.tipo, der)
            elif self.OperadorIzq.tipo == Tipo.BOOLEANO and self.OperadorDer.tipo == Tipo.BOOLEANO:             
                return self.obtenerVal(self.OperadorIzq.tipo, izq) == self.obtenerVal(self.OperadorIzq.tipo, der)
            elif self.OperadorIzq.tipo == Tipo.CHARACTER and self.OperadorDer.tipo == Tipo.CHARACTER:             
                return self.obtenerVal(self.OperadorIzq.tipo, izq) == self.obtenerVal(self.OperadorIzq.tipo, der)
            elif self.OperadorIzq.tipo == Tipo.CADENA and self.OperadorDer.tipo == Tipo.ENTERO:                         #colocar a los demas CAdena el str
                return self.obtenerVal(self.OperadorIzq.tipo, izq) == str(self.obtenerVal(self.OperadorIzq.tipo, der)) 
            elif self.OperadorIzq.tipo == Tipo.CADENA and self.OperadorDer.tipo == Tipo.DECIMAL:             
                return self.obtenerVal(self.OperadorIzq.tipo, izq) == self.obtenerVal(self.OperadorIzq.tipo, der)
            elif self.OperadorIzq.tipo == Tipo.CADENA and self.OperadorDer.tipo == Tipo.BOOLEANO:             
                return self.obtenerVal(self.OperadorIzq.tipo, izq) == self.obtenerVal(self.OperadorIzq.tipo, der)
            elif self.OperadorIzq.tipo == Tipo.CADENA and self.OperadorDer.tipo == Tipo.CADENA:             
                return self.obtenerVal(self.OperadorIzq.tipo, izq) == self.obtenerVal(self.OperadorIzq.tipo, der)
            elif self.OperadorIzq.tipo == Tipo.ENTERO and self.OperadorDer.tipo == Tipo.CADENA:             
                return self.obtenerVal(self.OperadorIzq.tipo, izq) == self.obtenerVal(self.OperadorIzq.tipo, der)
            elif self.OperadorIzq.tipo == Tipo.DECIMAL and self.OperadorDer.tipo == Tipo.CADENA:             
                return self.obtenerVal(self.OperadorIzq.tipo, izq) == self.obtenerVal(self.OperadorIzq.tipo, der)
            elif self.OperadorIzq.tipo == Tipo.BOOLEANO and self.OperadorDer.tipo == Tipo.CADENA:             
                return self.obtenerVal(self.OperadorIzq.tipo, izq) == self.obtenerVal(self.OperadorIzq.tipo, der)
            return Excepcion("Semantico", "TIpo Erroneo de operacion para ==.", self.fila,self.columna)
        return Excepcion("Semantico", "TIpo de operacion o especificado.", self.fila,self.columna)

    def obtenerVal(self, tipo, val):
        if tipo == Tipo.ENTERO:
            return int(val)
        elif tipo == Tipo.DECIMAL:
            return float(val)
        elif tipo == Tipo.BOOLEANO:
            return bool(val)
        return str(val)

    

