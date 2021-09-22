class pilha:
    def __init__(self):
        self.items = []
    def vazia(self):
        return self.items == []
    def tamanho(self):
        return len(self.items)
    def empilhar (self, item):
        self.items.append(item)
    def desenpilhar(self):
        return self.items.pop()
    def topo(self):
        return self.items[-1]
class Fila:
    def __init__(self):
        self.items = []
    def enfileirar(self, item):
        self.items.insert(0, item)
    def desemfileirar(self):
        return self.items.pop()
    def tamanho(self):
        return len(self.items)
    def vazia(self):
        return self.items == []
    def frente(self):
        return self.items[-1]

class no:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

    def setValor(self, novo_valor):
        self.valor = novo_valor

    def setProximo(self, proximo):
        self.valor = novo_valor

    def getValor(self):
        return self.valor

    def getProximo(self):
        return self.proximo
    def __str__(self):
        return str(self.valor)
