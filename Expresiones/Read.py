from Abstract.Instruccion import Instruccion
from TS.Tipo import TIPO

class Read(Instruccion):
    def __init__(self, fila, columna):
        self.fila = fila
        self.columna = columna
    
    def interpretar(self, tree, table):
        print(tree.getConsola()) #IMPRIME LA CONSOLA
        print("ingreso a READ. INGRESE UN VALOR")
        print.setConsola() #RESETEA LA CONSOLA
        #ESTO ES PARA EL EJEMPLO
        lectura = input() #SE OBTIENE EL VALOR
        return lectura