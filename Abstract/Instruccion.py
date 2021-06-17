from abc import ABC, abstractmethod

class Instruccion(ABC):                         #instrucciones que nos servira hacer 
    def __init__(self, fila, columna):
        self.fila = fila
        self.columna = columna
        super().__init__()

    @abstractmethod                             #cada vez que una clase herede instruccion debera usar interpretar
    def interpretar(self, tree, table):         #hacen referencia a Arbol, Tabla del TS
        pass 

    