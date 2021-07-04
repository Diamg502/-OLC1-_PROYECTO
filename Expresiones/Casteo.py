from Abstract.Instruccion import Instruccion
from TS.Excepcion import Excepcion
from TS.Tipo import TIPO

class Casteo(Instruccion):
    def __init__(self,tipo,expresion, fila, columna):
        self.tipo = tipo
        self.expresion = expresion
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        val = self.expresion.interpretar(tree,table)

#-----------------------------------------------------DOUBLE-------------------------------------------------------------

        if self.tipo == TIPO.DECIMAL:                                                                            
                if self.expresion.tipo == TIPO.ENTERO:                                                           #ENTERO A DECIMAL
                    try:
                        return float(self.obtenerVal(self.expresion.tipo, val))                                      #SE PASA A DECIMAL CON FLOAT 
                    except:
                         return Excepcion("Semantico", "NO SE PUEDE CASTEAR para float.", self.fila, self.columna)
                elif self.expresion.tipo == TIPO.CADENA:                                                         #STRING A DECIMAL   
                    try:
                        return float(self.obtenerVal(self.expresion.tipo, val))                                      #SE PASA A DECIMAL CON FLOAT  
                    except:
                         return Excepcion("Semantico", "NO SE PUEDE CASTEAR para float.", self.fila, self.columna)
                return Excepcion("Semantico", "Tipo Erroneo de casteo para double.", self.fila, self.columna)

#------------------------------------------ENTERO-----------------------------------------------------------

        if self.tipo == TIPO.ENTERO:                                                                            
                if self.expresion.tipo == TIPO.DECIMAL:                                                           #DECIMAL A ENTERO
                    try:
                        return int(self.obtenerVal(self.expresion.tipo, val))                                      #SE PASA A DECIMAL CON FLOAT
                    except:
                         return Excepcion("Semantico", "NO SE PUEDE CASTEAR para int.", self.fila, self.columna)
                elif self.expresion.tipo == TIPO.CADENA:                                                         #DECIMAL A STRING(CADENA)
                    try:
                        return int(self.obtenerVal(self.expresion.tipo, val))                                        #SE PASA A CADENA CON STR  
                    except:
                         return Excepcion("Semantico", "NO SE PUEDE CASTEAR para int.", self.fila, self.columna)  
                return Excepcion("Semantico", "Tipo Erroneo de casteo para int.", self.fila, self.columna)    
    
    
    
    
    def obtenerVal(self, tipo, val):
            if tipo == TIPO.ENTERO:
                return int(val)
            elif tipo == TIPO.DECIMAL:
                return float(val)
            elif tipo == TIPO.BOOLEANO:
                return bool(val)
            return str(val)