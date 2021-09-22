class ABB:

    def __init__(self):
        self.raiz = None

    def getRaiz(self):
        return self.raiz

    def inserir(self, valor):
        if(self.raiz == None):
            self.raiz = Node(valor)
        else:
            self._inserir(valor, self.raiz)

    def _inserir(self, valor, node):
        if (valor < node.valor):
            if (node.esq != None):
                self._inserir(valor, node.esq)
            else:
                node.esq = Node(valor)
        else:
            if(node.dir != None):
                self._inserir(valor, node.dir)
            else:
                node.dir = Node(valor)

    def buscar(self, valor):
        if(self.raiz != None):
            return self._buscar(valor, self.raiz)
        else:
            return None

    def _buscar(self, valor, node):
        if(valor == node.valor):
            return None
        elif (valor < node.valor and node.esq != None):
            return self._buscar(valor, node.esq)
        elif (valor > node.valor and node.dir != None):
            return self._buscar(valor, node.dir)

    def imprimir(self, tipo):
        if(self.raiz != None):
            if tipo == 'Pre':
                return self._imprimirPre(self.raiz)
            elif tipo == 'Em':
                return self._imprimirEm(self.raiz)
            elif tipo == 'Pos':
                return self._imprimirPos(self.raiz)

    def _imprimirPre(self, node):
        if(node != None):
            print(str(node.valor), end=",")
            self._imprimirPre(node.esq)
            self._imprimirPre(node.dir)

    def _imprimirEm(self, node):
        if(node != None):
            self._imprimirEm(node.esq)
            print(str(node.valor), end=",")
            self._imprimirEm(node.dir)

    def _imprimirPos(self, node):
        if(node != None):
            self._imprimirPos(node.esq)
            self._imprimirPos(node.dir)
            print(str(node.valor), end=",")

class Node:
    def __init__(self, valor):
        self.valor = valor
        self.dir = None
        self.esq = None
