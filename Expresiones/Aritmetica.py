from TS.TablaSimbolos import TablaSimbolos
from TS.Simbolo import Simbolo
from Expresiones.Identificador import Identificador
from Abstract.Instruccion import Instruccion
from TS.Excepcion import Excepcion
from TS.Tipo import TIPO, OperadorAritmetico
from Instrucciones.MasMenos import MasMenos

class Aritmetica(Instruccion):
    def __init__(self, operador, OperacionIzq, OperacionDer, fila, columna):
        self.operador = operador
        self.OperacionIzq = OperacionIzq
        self.OperacionDer = OperacionDer
        self.fila = fila
        self.columna = columna
        self.tipo = None

    
    def interpretar(self, tree, table):                                             #OBTENCION DE DATOS
        izq = self.OperacionIzq.interpretar(tree, table)
        if isinstance(izq, Excepcion): return izq
        if self.OperacionDer != None:
            der = self.OperacionDer.interpretar(tree, table)
            if isinstance(der, Excepcion): return der

        #--------------------------------------------------------------SUMA------------------------------------------------------
        if self.operador == OperadorAritmetico.MAS:                                                                         #SUMA
            if self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.ENTERO:                             #ENTERO AND ENTERO
                self.tipo = TIPO.ENTERO                                                                                     #Retorna un entero
                return self.obtenerVal(self.OperacionIzq.tipo, izq) + self.obtenerVal(self.OperacionDer.tipo, der)          
            elif self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.DECIMAL:                          #ENTERO AND DECIMAL
                self.tipo = TIPO.DECIMAL                                                                                    #Retorna un decimal
                return self.obtenerVal(self.OperacionIzq.tipo, izq) + self.obtenerVal(self.OperacionDer.tipo, der)          
            elif self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.CADENA:                           #ENTERO AND CADENA
                self.tipo = TIPO.CADENA                                                                                     #Retorna una cadena
                return str(self.obtenerVal(self.OperacionIzq.tipo, izq)) + self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.BOOLEANO:                         #ENTERO AND BOOLEAN
                self.tipo = TIPO.ENTERO                                                                                     #Retorna una ENTERO
                return self.obtenerVal(self.OperacionIzq.tipo, izq) + self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.ENTERO:                          #DOUBLE AND ENTERO
                self.tipo = TIPO.DECIMAL                                                                                    #Retorna un decimal
                return self.obtenerVal(self.OperacionIzq.tipo, izq) + self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.DECIMAL:                         #DOUBLE AND DOUBLE
                self.tipo = TIPO.DECIMAL                                                                                    #Retorna un decimal
                return self.obtenerVal(self.OperacionIzq.tipo, izq) + self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.BOOLEANO:                        #DOUBLE AND BOOLEAN
                self.tipo = TIPO.DECIMAL                                                                                    #Retorna un decimal
                return self.obtenerVal(self.OperacionIzq.tipo, izq) + self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.CADENA:                          #DOUBLE AND CADENA
                self.tipo = TIPO.CADENA                                                                                    #Retorna un CADENA
                return str(self.obtenerVal(self.OperacionIzq.tipo, izq)) + self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.BOOLEANO and self.OperacionDer.tipo == TIPO.ENTERO:                          #BOOLEAN AND ENTERO
                self.tipo = TIPO.ENTERO                                                                                    #Retorna un ENTERO
                return self.obtenerVal(self.OperacionIzq.tipo, izq) + self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.BOOLEANO and self.OperacionDer.tipo == TIPO.DECIMAL:                          #BOOLEAN AND DOUEBLE
                self.tipo = TIPO.DECIMAL                                                                                    #Retorna un DECIMAL
                return self.obtenerVal(self.OperacionIzq.tipo, izq) + self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.BOOLEANO and self.OperacionDer.tipo == TIPO.BOOLEANO:                          #BOOLEAN AND BOLEANO
                self.tipo = TIPO.ENTERO                                                                                    #Retorna un ENTERO
                return self.obtenerVal(self.OperacionIzq.tipo, izq) + self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.BOOLEANO and self.OperacionDer.tipo == TIPO.CADENA:                          #BOOLEAN AND STRING
                self.tipo = TIPO.CADENA                                                                                    #Retorna un CADENA
                return str(self.obtenerVal(self.OperacionIzq.tipo, izq)) + self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.CHARACTER and self.OperacionDer.tipo == TIPO.CHARACTER:                          #CHARACTER AND CARACTER
                self.tipo = TIPO.CADENA                                                                                    #Retorna un CADENA
                return str(self.obtenerVal(self.OperacionIzq.tipo, izq)) + str(self.obtenerVal(self.OperacionDer.tipo, der))
            elif self.OperacionIzq.tipo == TIPO.CHARACTER and self.OperacionDer.tipo == TIPO.CADENA:                          #CHARACTER AND CADENA
                self.tipo = TIPO.CADENA                                                                                    #Retorna un CADENA
                return str(self.obtenerVal(self.OperacionIzq.tipo, izq)) + self.obtenerVal(self.OperacionDer.tipo, der)            
            elif self.OperacionIzq.tipo == TIPO.CADENA and self.OperacionDer.tipo == TIPO.ENTERO:                           #CADENA AND ENTERO
                self.tipo = TIPO.CADENA                                                                                     #Retorna una cadena
                return self.obtenerVal(self.OperacionIzq.tipo, izq) + str(self.obtenerVal(self.OperacionDer.tipo, der))     
            elif self.OperacionIzq.tipo == TIPO.CADENA and self.OperacionDer.tipo == TIPO.CADENA:                           #CADENA AND CADENA
                self.tipo = TIPO.CADENA                                                                                     #Retorna una cadena
                return self.obtenerVal(self.OperacionIzq.tipo, izq) + self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.CADENA and self.OperacionDer.tipo == TIPO.DECIMAL:                           #CADENA AND DOUBLE
                self.tipo = TIPO.CADENA                                                                                     #Retorna una cadena
                return self.obtenerVal(self.OperacionIzq.tipo, izq) + str(self.obtenerVal(self.OperacionDer.tipo, der))
            elif self.OperacionIzq.tipo == TIPO.CADENA and self.OperacionDer.tipo == TIPO.BOOLEANO:                           #CADENA AND BOOLEAN
                self.tipo = TIPO.CADENA                                                                                     #Retorna una cadena
                return self.obtenerVal(self.OperacionIzq.tipo, izq) + str(self.obtenerVal(self.OperacionDer.tipo, der))
            elif self.OperacionIzq.tipo == TIPO.CADENA and self.OperacionDer.tipo == TIPO.CHARACTER:                           #CADENA AND CHAR
                self.tipo = TIPO.CADENA                                                                                     #Retorna una cadena
                return self.obtenerVal(self.OperacionIzq.tipo, izq) + str(self.obtenerVal(self.OperacionDer.tipo, der))
            return Excepcion("Semantico", "Tipo Erroneo de operacion para +.", self.fila, self.columna)                     #Retorna un error de operacion

    #*----------------------------------------------------RESTA-----------------------------------------------------------------------------------------------------

        elif self.operador == OperadorAritmetico.MENOS: #RESTA                                                                
            if self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.ENTERO:                             #ENTERO AND ENTERO
                self.tipo = TIPO.ENTERO                                                                                     #RETORNA ENTERO
                return self.obtenerVal(self.OperacionIzq.tipo, izq) - self.obtenerVal(self.OperacionDer.tipo, der)    
            elif self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.DECIMAL:                             #ENTERO AND DOUBLE
                self.tipo = TIPO.DECIMAL                                                                                     #RETORNA ENTERO
                return self.obtenerVal(self.OperacionIzq.tipo, izq) - self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.BOOLEANO:                             #ENTERO AND BOOLEAN
                self.tipo = TIPO.ENTERO                                                                                     #RETORNA ENTERO
                return self.obtenerVal(self.OperacionIzq.tipo, izq) - self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.ENTERO:                             #DOUBLE AND ENTERO
                self.tipo = TIPO.DECIMAL                                                                                     #RETORNA ENTERO
                return self.obtenerVal(self.OperacionIzq.tipo, izq) - self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.DECIMAL:                             #DOUBLE AND DOUBLE
                self.tipo = TIPO.DECIMAL                                                                                     #RETORNA ENTERO
                return self.obtenerVal(self.OperacionIzq.tipo, izq) - self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.BOOLEANO:                             #DOUBLE AND BOOLEEAN
                self.tipo = TIPO.DECIMAL                                                                                     #RETORNA ENTERO
                return self.obtenerVal(self.OperacionIzq.tipo, izq) - self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.BOOLEANO and self.OperacionDer.tipo == TIPO.ENTERO:                             #BOOLEAN AND ENTERO
                self.tipo = TIPO.ENTERO                                                                                     #RETORNA ENTERO
                return self.obtenerVal(self.OperacionIzq.tipo, izq) - self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.BOOLEANO and self.OperacionDer.tipo == TIPO.DECIMAL:                             #BOOLEAN AND DOBLE
                self.tipo = TIPO.DECIMAL                                                                                     #RETORNA ENTERO
                return self.obtenerVal(self.OperacionIzq.tipo, izq) - self.obtenerVal(self.OperacionDer.tipo, der)       
            return Excepcion("Semantico", "Tipo Erroneo de operacion para -.", self.fila, self.columna)

#-----------------------------------------------------------MULTIPLICACION*--------------------------------------------------

        elif self.operador == OperadorAritmetico.POR: #MULTIPLICACION
            if self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.ENTERO:                         #ENTERO AND ENTERO
                self.tipo = TIPO.ENTERO                                                                                    #RETORNA UN ENTERO
                return self.obtenerVal(self.OperacionIzq.tipo, izq) * self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.DECIMAL:                         #ENTERO AND DOUBLE
                self.tipo = TIPO.DECIMAL                                                                                    #RETORNA UN ENTERO
                return self.obtenerVal(self.OperacionIzq.tipo, izq) * self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.ENTERO:                         #DOUBLE AND ENTERO
                self.tipo = TIPO.DECIMAL                                                                                    #RETORNA UN ENTERO
                return self.obtenerVal(self.OperacionIzq.tipo, izq) * self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.DECIMAL:                         #DOUBLE AND DOUBLE
                self.tipo = TIPO.DECIMAL                                                                                    #RETORNA UN ENTERO
                return self.obtenerVal(self.OperacionIzq.tipo, izq) * self.obtenerVal(self.OperacionDer.tipo, der)
            return Excepcion("Semantico", "Tipo Erroneo de operacion para *.", self.fila, self.columna)

#----------------------------------------------------------DIVISION--------------------------------------------------------------------

        elif self.operador == OperadorAritmetico.DIV: #DIVISION
            if self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.ENTERO:                         #ENTERO AND ENTERO
                self.tipo = TIPO.DECIMAL                                                                                    #RETORNA UN ENTERO
                if self.obtenerVal(self.OperacionDer.tipo,der)==0:
                    return Excepcion("Matematico", "imposible dividir entre 0.", self.fila, self.columna)
                else:
                    return self.obtenerVal(self.OperacionIzq.tipo, izq) / self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.DECIMAL:                         #ENTERO AND DOUBLE
                self.tipo = TIPO.DECIMAL    
                if self.obtenerVal(self.OperacionDer.tipo,der)==0:
                    return Excepcion("Matematico", "imposible dividir entre 0.", self.fila, self.columna)
                else:                                                                                #RETORNA UN ENTERO
                    return self.obtenerVal(self.OperacionIzq.tipo, izq) / self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.ENTERO:                         #DOUBLE AND ENTERO
                self.tipo = TIPO.DECIMAL  
                if self.obtenerVal(self.OperacionDer.tipo,der)==0:
                    return Excepcion("Matematico", "imposible dividir entre 0.", self.fila, self.columna)
                else:                                                                                  #RETORNA UN ENTERO
                    return self.obtenerVal(self.OperacionIzq.tipo, izq) / self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.DECIMAL:                         #DOUBLE AND DOUBLE
                self.tipo = TIPO.DECIMAL  
                if self.obtenerVal(self.OperacionDer.tipo,der)==0:
                    return Excepcion("Matematico", "imposible dividir entre 0.", self.fila, self.columna)
                else:                                                                                  #RETORNA UN ENTERO
                    return self.obtenerVal(self.OperacionIzq.tipo, izq) / self.obtenerVal(self.OperacionDer.tipo, der)
            return Excepcion("Semantico", "Tipo Erroneo de operacion para /.", self.fila, self.columna)

#----------------------------------------------------------POTENCIA--------------------------------------------------------------------

        elif self.operador == OperadorAritmetico.POT: #POTENCIA
            if self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.ENTERO:                         #ENTERO AND ENTERO
                self.tipo = TIPO.DECIMAL                                                                                    #RETORNA UN ENTERO
                aux = self.obtenerVal(self.OperacionIzq.tipo,izq)
                for i in range(self.obtenerVal(self.OperacionDer.tipo,der)-1):
                    aux = aux * self.obtenerVal(self.OperacionIzq.tipo, izq)
                return aux
            elif self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.DECIMAL:                         #ENTERO AND DOUBLE
                self.tipo = TIPO.DECIMAL                                                                                    #RETORNA UN ENTERO
                aux = self.obtenerVal(self.OperacionIzq.tipo,izq)
                for i in range(self.obtenerVal(self.OperacionDer.tipo,der)-1):
                    aux = aux * self.obtenerVal(self.OperacionIzq.tipo, izq)
                return aux
            elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.ENTERO:                         #DOUBLE AND ENTERO
                self.tipo = TIPO.DECIMAL                                                                                    #RETORNA UN ENTERO
                aux = self.obtenerVal(self.OperacionIzq.tipo,izq)
                for i in range(self.obtenerVal(self.OperacionDer.tipo,der)-1):
                    aux = aux * self.obtenerVal(self.OperacionIzq.tipo, izq)
                return aux
            elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.DECIMAL:                         #DOUBLE AND DOUBLE
                self.tipo = TIPO.DECIMAL                                                                                    #RETORNA UN ENTERO
                aux = self.obtenerVal(self.OperacionIzq.tipo,izq)
                for i in range(self.obtenerVal(self.OperacionDer.tipo,der)-1):
                    aux = aux * self.obtenerVal(self.OperacionIzq.tipo, izq)
                return aux
            return Excepcion("Semantico", "Tipo Erroneo de operacion para ^.", self.fila, self.columna)


#---------------------------------------------------------------INCREMENTO-----------------------------------------------------------
        elif self.operador in (OperadorAritmetico.INC,OperadorAritmetico.DEC): #INCREMENTA
            if isinstance(self.OperacionIzq, Identificador):

                value = self.OperacionIzq.interpretar(tree, table) # Valor a asignar a la variable

                if isinstance(value, Excepcion): return value

                if self.OperacionIzq.getTipo() in (TIPO.ENTERO, TIPO.DECIMAL):

                    if self.operador == OperadorAritmetico.INC:
                        symbol = Simbolo(self.OperacionIzq.getID(),self.OperacionIzq.getTipo(),self.fila,self.columna,value+1)
                    elif self.operador == OperadorAritmetico.DEC:
                        symbol = Simbolo(self.OperacionIzq.getID(),self.OperacionIzq.getTipo(),self.fila,self.columna,value-1)
                        
                    result = table.actualizarTabla(symbol)

                    if isinstance(result,Excepcion): return result

                    self.tipo = self.OperacionIzq.getTipo()
                    return symbol.getValor()
                else:
                    return Excepcion("Semantico", "Tipo de OPERADOR Diferente en Asignacion", self.getFila(), self.getColumna())
            else:
                return Excepcion("Semantico", "Tipo de VARIABLE Diferente en Asignacion", self.getFila(), self.getColumna())
#---------------------------------------------------------------DECREMENTO-----------------------------------------------------------
        elif self.operador == OperadorAritmetico.DEC: #INCREMENTA
            if self.OperacionDer.tipo == TIPO.ENTERO:                         #ENTERO AND ENTERO
                self.tipo = TIPO.DECIMAL                                                                                    #RETORNA UN ENTERO
                return MasMenos(self.operador.getID(),self.operador,self.fila,self.columna)
            elif self.OperacionDer.tipo == TIPO.DECIMAL:                         #ENTERO AND DOUBLE
                self.tipo = TIPO.DECIMAL                                                                                    #RETORNA UN ENTERO
                return MasMenos(self.operador.getID(),self.operador,self.fila,self.columna)
            return Excepcion("Semantico", "Tipo Erroneo de operacion para ++.", self.fila, self.columna)

#---------------------------------------------------------------NEGACION UNARIA---------------------------
        elif self.operador == OperadorAritmetico.UMENOS: #NEGACION UNARIA
            if self.OperacionIzq.tipo == TIPO.ENTERO:
                self.tipo = TIPO.ENTERO
                return - self.obtenerVal(self.OperacionIzq.tipo, izq)
            elif self.OperacionIzq.tipo == TIPO.DECIMAL:
                self.tipo = TIPO.DECIMAL
                return - self.obtenerVal(self.OperacionIzq.tipo, izq)
            return Excepcion("Semantico", "Tipo Erroneo de operacion para - unario.", self.fila, self.columna)
        return Excepcion("Semantico", "Tipo de Operacion no Especificado.", self.fila, self.columna)



    def obtenerVal(self, tipo, val):
        if tipo == TIPO.ENTERO:
            return int(val)
        elif tipo == TIPO.DECIMAL:
            return float(val)
        elif tipo == TIPO.BOOLEANO:
            return bool(val)
        return str(val)
        