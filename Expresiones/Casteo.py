from Abstract.NodoAST import NodoAST
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
                elif self.expresion.tipo == TIPO.CHARACTER:                                                         #CARACTER A DECIMAL   
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
                elif self.expresion.tipo == TIPO.CHARACTER:                                                         #CARACTER A STRING(CADENA)
                    try:
                        return int(self.obtenerVal(self.expresion.tipo, val))                                        #SE PASA A CADENA CON STR  
                    except:
                         return Excepcion("Semantico", "NO SE PUEDE CASTEAR para int.", self.fila, self.columna) 
                return Excepcion("Semantico", "Tipo Erroneo de casteo para int.", self.fila, self.columna)   

#------------------------------------------STRING(CADENA)-----------------------------------------------------------

        if self.tipo == TIPO.CADENA:                                                                            
                if self.expresion.tipo == TIPO.DECIMAL:                                                           #DECIMAL A CADENA
                    try:
                        return str(self.obtenerVal(self.expresion.tipo, val))                                      #SE PASA A DECIMAL CON FLOAT
                    except:
                         return Excepcion("Semantico", "NO SE PUEDE CASTEAR para string.", self.fila, self.columna)
                elif self.expresion.tipo == TIPO.ENTERO:                                                         #ENTERO A STRING(CADENA)
                    try:
                        return str(self.obtenerVal(self.expresion.tipo, val))                                        #SE PASA A CADENA CON STR  
                    except:
                         return Excepcion("Semantico", "NO SE PUEDE CASTEAR para string.", self.fila, self.columna)  
                return Excepcion("Semantico", "Tipo Erroneo de casteo para string.", self.fila, self.columna)  

#------------------------------------------CARACTER(CHAR)-----------------------------------------------------------

        if self.tipo == TIPO.CHARACTER:                                                                            
                if self.expresion.tipo == TIPO.ENTERO:                                                           #DECIMAL A CADENA
                    try:
                        return str(self.obtenerVal(self.expresion.tipo, val))                                      #SE PASA A DECIMAL CON FLOAT
                    except:
                         return Excepcion("Semantico", "NO SE PUEDE CASTEAR para char.", self.fila, self.columna)
                return Excepcion("Semantico", "Tipo Erroneo de casteo para CHAR.", self.fila, self.columna)

#------------------------------------------CARACTER(CHAR)-----------------------------------------------------------

        if self.tipo == TIPO.BOOLEANO:                                                                            
                if self.expresion.tipo == TIPO.CADENA:                                                           #DECIMAL A CADENA
                    try:
                        return str(self.obtenerVal(self.expresion.tipo, val))                                      #SE PASA A DECIMAL CON FLOAT
                    except:
                         return Excepcion("Semantico", "NO SE PUEDE CASTEAR para str.", self.fila, self.columna)
                return Excepcion("Semantico", "Tipo Erroneo de casteo para BOOLEAN.", self.fila, self.columna)       
    
    def getNodo(self):
        nodo = NodoAST("CASTEO")
        nodo.agregarHijo(str(self.tipo))
        nodo.agregarHijoNodo(self.expresion.getNodo())
        return nodo
    
    
    def obtenerVal(self, tipo, val):
            if tipo == TIPO.ENTERO:
                return int(val)
            elif tipo == TIPO.DECIMAL:
                return float(val)
            elif tipo == TIPO.BOOLEANO:
                return bool(val)
            return str(val)