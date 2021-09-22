class NodoLista:
    def __init__(self, dado=0, prox_nodo=None):
        self.dado = dado
        self.proximo = prox_nodo
    def __repr__(self):
        return '%s - %s' % (self.dado, self.proximo)
class listano:
    def __init__(self):
        self.cabeca = None
    def __repr__(self):
        return "[" + str(self.cabeca) + "]"
def insere(lista, novo_dado):
    novo_nodo = NodoLista(novo_dado)
    novo_nodo.proximo = lista.cabeca
    lista.cabeca = novo_nodo
def remove(self, valor):
    assert self.cabeca
    if self.cabeca.dado == valor:
        self.cabeca = self.cabeca.proximo
    else:
        ante = None
        frente = self.cabeca
        while frente and frente.dado != valor:
            ante = frente
            frente = frente.proximo
        if frente:
            ante.proximo = frente.proximo
        else:

            ante.proximo = None
lista = listano()
insere(lista,33)
insere(lista,74)
insere(lista,54)
insere(lista,5)
insere(lista,20)
print("Lista \n",lista)
print("Removendo o valor 5")
remove(lista,5)
print(lista)
a=int(input("digite um valor para remover:\n"))
remove(lista,a)
print(lista)
