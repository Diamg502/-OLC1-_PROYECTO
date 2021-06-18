from Abstract.Instruccion import Instruccion


class Identificador(Instruccion):
    def __init__(self, identificador, fila, columna):
        self.identificador = identificador
        self.fila = fila
        self.columna = columna
        self.tipo = None

    def interpretar(self, tree, table):
        simbolo = table.getTabla(self.identificador.lower())

        if simbolo == None:
            return Exception("Semantico", " Variable" + self.identificador + " No Encontrado", self.fila, self.columna)

        self.tipo = simbolo.getTipo()
        return simbolo.getValor()

