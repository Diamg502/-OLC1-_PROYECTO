from Abstract.NodoAST import NodoAST
from Instrucciones.Declaracion import Declaracion
from Instrucciones.Return import Return
from Abstract.Instruccion import Instruccion
from TS.Excepcion import Excepcion
from TS.Tipo import TIPO
from TS.TablaSimbolos import TablaSimbolos
from Instrucciones.Break import Break

class For(Instruccion):
    def __init__(self, condicion, instrucciones,incremento,inicializar, fila, columna):
        self.condicion = condicion
        self.instrucciones = instrucciones
        self.incremento = incremento
        self.fila = fila
        self.inicializar = inicializar
        self.columna = columna

    def interpretar(self, tree, table):
        nuevaTabla = None
        if isinstance(self.inicializar,Declaracion): 
            nuevaTabla = TablaSimbolos(table)
            variablex = self.inicializar.interpretar(tree,nuevaTabla)  #Inicializando la interpretacion dela nueva tabla DECLARACIOB
        else:
            variablex = self.inicializar.interpretar(tree,table)  #Inicializando la interpretacion dela nueva tabla ASIGNACION
        if isinstance(variablex,Excepcion): return variablex

        while True:
            if nuevaTabla != None:
                condicion = self.condicion.interpretar(tree, nuevaTabla) #VALIDANDO 
            else:
                condicion = self.condicion.interpretar(tree, table)      
            if isinstance(condicion, Excepcion): return condicion

            if self.condicion.tipo == TIPO.BOOLEANO:
                if bool(condicion) == True:   # VERIFICA SI ES VERDADERA LA CONDICION
                    if nuevaTabla != None:
                        nuevaTabla2 = TablaSimbolos(nuevaTabla)       #NUEVO ENTORNO
                    else:
                        nuevaTabla2 = TablaSimbolos(table)       #NUEVO ENTORNO     
                    if isinstance(condicion, Excepcion): return condicion
                    
                    for instruccion in self.instrucciones:
                        result = instruccion.interpretar(tree, nuevaTabla2) #EJECUTA INSTRUCCION ADENTRO DEL IF
                        if isinstance(result, Excepcion) :
                            tree.getExcepciones().append(result)
                            tree.updateConsola(result.toString())
                        if isinstance(result, Break): return None
                        if isinstance(result, Return): return result
                    Avancex = self.incremento.interpretar(tree,nuevaTabla2)   
                    if isinstance (Avancex,Excepcion): return Avancex 
                else:
                    break   
                return Excepcion("Semantico", "Tipo de dato no booleano en IF.", self.fila, self.columna)

    def getNodo(self):                                      #VERIFICAR DESPUES
        nodo = NodoAST("FOR")
        instrucciones = NodoAST("INSTRUCCIONES")
        for instr in self.instrucciones:
            instrucciones.agregarHijoNodo(instr.getNodo())
        nodo.agregarHijoNodo(instrucciones)
        return nodo    

            