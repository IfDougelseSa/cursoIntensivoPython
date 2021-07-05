from typing import List

#Fila
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
    def elementos(self):
        return (self.items)

#Lista
lista = [1, 2, 3, 4, 5]


elemento1 = lista.pop(0)
elemento2 = lista.pop(0)
elemento3 = lista.pop(0)
elemento4 = lista.pop(0)
elemento5 = lista.pop(0)





# Pilha
pilha: List[int] = []  # {1}

# Adicionando elementos na pilha
pilha.append(elemento1)
pilha.append(elemento2)
pilha.append(elemento3)
pilha.append(elemento4)
pilha.append(elemento5)

# Obtendo o elemento mais novo
elemento_pilha1 = pilha.pop()
elemento_pilha2 = pilha.pop()
elemento_pilha3 = pilha.pop()
elemento_pilha4 = pilha.pop()
elemento_pilha5 = pilha.pop()



f = Queue()
f.enqueue(elemento_pilha1)
f.enqueue(elemento_pilha2)
f.enqueue(elemento_pilha3)
f.enqueue(elemento_pilha4)
f.enqueue(elemento_pilha5)


#Adicionando elementos na lista
lista.append(6)
lista.append(7)
lista.append(8)
lista.append(9)
lista.append(10)


#Removendo elementos
elemento1 = lista.pop(0)
elemento2 = lista.pop(0)
elemento3 = lista.pop(0)
elemento4 = lista.pop(0)
elemento5 = lista.pop(0)

# Adicionando elementos na pilha
pilha.append(elemento1)
pilha.append(elemento2)
pilha.append(elemento3)
pilha.append(elemento4)
pilha.append(elemento5)


# Obtendo o elemento mais novo
elemento_pilha6 = pilha.pop()
elemento_pilha7 = pilha.pop()
elemento_pilha8 = pilha.pop()
elemento_pilha9 = pilha.pop()
elemento_pilha10 = pilha.pop()


f = Queue()
f.enqueue(elemento_pilha6)
f.enqueue(elemento_pilha7)
f.enqueue(elemento_pilha8)
f.enqueue(elemento_pilha9)
f.enqueue(elemento_pilha10)

print(f.size())
print(f.elementos())



