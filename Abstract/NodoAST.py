class NodoAST():
    def __init__(self, valor):
        self.valor = valor
        self.hijo = []

    def setHijos(self, hijos):              #Agregar hijo normal
        self.hijos = hijos

    def agregarHijo(self, valorHijo):           #Agregar hijo al AST
        self.hijos.append(NodoAST(valorHijo))

    def agregarHijos(self, hijos):         #AGREGAR UNA LISTA DE HIJOS
        for hijo in hijos:
            self.hijos.append(hijo)

    def agregarHijoNodo(self, hijo):
        self.hijo.append(hijo)

    def agregarPrimerHijo(self, valorHijo):         #AGREGAR NODO AL INICIO DEtodo
        self.hijo.insert(0, NodoAST(valorHijo))

    def agregarPrimerHijoNodo(self, hijo):
        self.hijos.insert(0,hijo)

    def getValor(self):
        return str(self.valor)

    def setValor(self, valor):
        self.valor = valor

    def getHijos(self):
        return self.hijos    

    
