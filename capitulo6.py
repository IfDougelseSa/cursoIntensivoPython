"""
Dicionários

Acessando valores em um dicionário
Especifique o nome do dicionário e coloque a chave entre colchetes
Exemplo: print(alien_0['color']

Adicionando novos pares chave-valor

Para acrescentar um novo par chave-valor, especifique o nome do dicionário, seguido na nova chave
entre colchetes, juntamente com o novo valor.

Exemplo:
nome_dicionario['chave'] = valor

Modificando valores em um dicionário
Apenas utilizar o nome do dicionário juntamente com a chave e modificar o valor

Exemplo:
nome_dicionario['chave] = novo_valor

Removendo pares chave-valor
Para remover uma chave e um valor de um dicionário, basta utilizar o del com o nome do dicionário
e a chave

Exemplo:
del nome_dicionario['chave']

Percorrendo todos os pares chave-valor com um laço.

É possível percorrer um dicionário utilizando o laço for

Exemplo:
for key, values in nome_dicionario.itens()
    print(key)
    print(values)

o key armazena a chave e o values armazena os valores.

Para percorrer um dicionário deve-se criar duas variáveis, uma para armazenar a chave e outra
para armazenar o valor.


Percorrendo todas as chaves de um dicionário com um laço
O método key permite percorrer apenas as chaves

Exemplo:

for keys in nome_dicionario.keys():
    print(keys)

Com isso, apenas a chave será percorrida.

Percorrer a chave é o comportamento padrão, portanto o método keys é o mesmo que:

for keys in nome_dicionarios:
    print(keys)

O método keys não serve so para laços, ele também devolve uma lista de todas as chaves.

Percorrendo as chaves de um dicionário em ordem usando um laço.
Podemos usar a função sorted() para obter uma cópia ordenada das chaves:

Exemplo:

for keys in sorted(nome_dicionario.keys())
    print(keys)

Será ordenado em ordem alfabética

Percorrendo todos os valores de um dicionário com um laço
O método values() pode ser usado para devolver uma lista de valores sem as chaves

Exemplo:
for values in nome_dicionario.values()
    print(values)

Para ver os resultados sem repetições podemos utilizar o set()

for values in set(nome_dicionario.values())
    print(values)

Será mostrado os valores sem repetições

Informações aninhadas

Adicionar dicionários em uma lista ou adicionar listas em dicionários.
"""
