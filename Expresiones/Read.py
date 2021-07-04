from Abstract.NodoAST import NodoAST
from Abstract.Instruccion import Instruccion
from TS.Tipo import TIPO
from tkinter import *

class Read(Instruccion):
    def __init__(self, fila, columna):
        self.fila = fila
        self.columna = columna
        self.tipo = TIPO.CADENA
    
    def interpretar(self, tree, table):
        #print(tree.getConsola()) #IMPRIME LA CONSOLA
        #print("ingreso a READ. INGRESE UN VALOR")
        #ESTO ES PARA EL EJEMPLO
        lectura = input() #SE OBTIENE EL VALOR
        return lectura



    def getNodo(self):
        nodo = NodoAST("READ")
        return nodo