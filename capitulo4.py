"""
Percorrendo listas com o laço for

O for pega o valor da lista em armazena em uma variavel temporariamente, depois pega o outro valor
e armazena na mesma variavel temporariamente, até acabar os elementos da lista e ir para o próximo
comando.


funcao range()
Facilita gerar uma série de numeros
É possível converter os resultado do range em uma lista de numeros

Exemplo:

numbers = list(range(1,6))

Exemplos de range:

squares = []


for values in range(1, 11):
    square = values**2
    squares.append(square)
print(squares)

Valores da lista:

min("nome_lista") Encontrar valor minimo
max("nome_lista") Encontrar valor maximo
sum("nome_lista") Encontrar a soma da lista

List comprehension:
Permite gerar a lista em uma linha de codigo

Exemplo:
squares = [value**2 for value in range(1,11)]print(squares)

Fatiando uma lista

Exemplo:

print(list[0:3])

Se o primeiro índice de uma fatia for omitido,
Python começará sua fatiaautomaticamente no início da lista

Exemplo:

print(list[:3])

Se quiser os itens a partir de um elemento

print(list[3:])

Copiando uma lista

list = []
nova_lista = list[:]

Assim temos duas listas independentes.

caso fazer nova_lista = list
Quando for adicionar um elemento em uma, será adicionado na outra lista também.




"""