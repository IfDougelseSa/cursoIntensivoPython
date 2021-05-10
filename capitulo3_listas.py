"""
Uma lista é uma coleção de itens em uma ordem em particular.
Podemoscriar uma lista que inclua as letras do alfabeto, os dígitos de 0 a 9 ou os nomes de
todas as pessoas de sua família.
Você pode colocar qualquerinformação que quiser em uma lista, e os itens de sua lista não precisam
estar  relacionados  de  nenhum  modo  em  particular.
Como  uma  lista geralmente contém mais de um elemento, é uma boa ideia deixar seu nomeno plural, por exemplo,
letters, digits ou names. Em Python, colchetes ([]) indicam uma lista, e elementos individuais da
lista são separados por vírgulas.

Acessando elementos de uma lista

Listas  são  coleções  ordenadas,  portanto  você  pode  acessar  qualquer elemento de uma lista informando
 a posição – ou índice – do item desejadoao interpretador Python. Para acessar um elemento de uma lista,
 escreva onome da lista seguido do índice do item entre colchetes.


 Para alterar elementos em uma lista, basta escrever o nome da lista com o elemento e receber outro nome
 de elemento.

 exemplo:
 carros = ["honda, porsche, ducati]
 carros[0] = "fusca"

 Pronto!

 Acrescentando elemento em uma lista

 nome_lista.append("elemento")
 O elemento será acrescentado no final da lista.

 Inserindo elementos em uma lista
 Para adicionar elemento em qualquer posição basta usar o método insert()

 Exemplo:

 nome_lista.insert(1, "nome_elemento)

 Com isso, todos os valores serão deslocados para a direita.


 Removendo elementos de uma lista:
 Se a posição for conhecida, basta usar o del

Exemplo:

del nome_lista[]

Método pop()

Remove o último item de uma lista, mas permite que você trabalhe com esse item depois da remoção.


nome_elemento = nome_lista.pop()

O elemento vai ser removido e ficará guardado em nome_elemento.
Além disso, se você incluir o índice no pop, ele removerá o elemento que vocẽ deseja.
Sempre que usar o pop o item não ficará mais armazenado na lista.

Se não souber o valor, mas sim o nome do elemento, é possível remover esse elemento usando
o remove()

exemplo:

nome_lista.remove('nome_elemento')
O remove pode armazenar um valor excluído na lista.

Exemplos na prática:
list = ["segunda", "terca", "quarta", "quinta", "sexta"]


best_day = list.pop(4)
print(f'The best day of the week is {best_day}.')
print(list)

worst_day = "segunda"
list.remove(worst_day)
print(f'The worst day of the week is {worst_day}.')

Ordenando uma lista de forma permanente com o metodo sort()

Para ordenar uma lista em ordem alfabética basta utilizar o metodo sort
Exemplo:
nome_lista.sort()

Para orderna uma lista em ordem alfabética inversa utililizar reverse=True
Exemplo:

nome_lista.sort(reverse=True)
Esse método altera a lista de forma permanente.

Ordenando uma lista de forma temporária

Preservar a ordem original, mas apresentar de forma ordenada.

Utilizar o método sorted()

Exemplo:
print(sorted(nome_lista))

Essa funçao aceita o argumento reverse=True


Exibindo uma lista em ordem inversa

Para exibir uma lista em ordem inversa, basta utilizar o método reverse()

O método reverse muda a ordem da lista permanentemente.

Exemplo:

nome_lista.reverse()

Se adicionar o reverse() novamente, a lista volta para o estado original.

Desconbrindo tamanho de uma lista

Utilizar o len()

"""
