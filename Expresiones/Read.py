from Abstract.NodoAST import NodoAST
from Abstract.Instruccion import Instruccion
from TS.Tipo import TIPO
from tkinter import simpledialog

class Read(Instruccion):
    def __init__(self, fila, columna):
        self.fila = fila
        self.columna = columna
        self.tipo = TIPO.CADENA
    
    def interpretar(self, tree, table):
        #tree.get_SalidaTexto().insert('insert', tree.getConsola())
        #print(tree.getConsola()) #IMPRIME LA CONSOLA
        #print("ingreso a READ. INGRESE UN VALOR")
        #ESTO ES PARA EL EJEMPLO
        pregunta = simpledialog.askstring("Input","Ingresar Valor")
        
        if pregunta == None:
            pregunta = "null"
            
        #tree.get_SalidaTexto().delete('1.0', 'end')    
        #tree.updateConsola('input: '+ pregunta)
        self.valor = pregunta
        #lectura = input() #SE OBTIENE EL VALOR
        return pregunta



    def getNodo(self):
        nodo = NodoAST("READ")
        return nodo