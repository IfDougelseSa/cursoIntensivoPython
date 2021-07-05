"""
Funções

São blocos de códigos nomeados, concebidos para realizar uma tarefa específica.

Argumentos e parâmetros

O que está entre os parênteses de uma função é chamado de parâmetro. Quando vocÊ chama uma função
você passa uma informação, essa informação é chamada de argumento.

Argumentos posicionais

Quando chamamos uma função, Python precisa fazer a correspondência entre cada argumento da chamada da
função e um parâmetro da definição. Para cada parâmetro fornecido é necessário um argumento, sendo prefe-
rivel os argumentos corresponderem com os parâmetros (A ordem é importante).

Argumentos nomeados

Associar diretamente o nome e o valor no argumento

Exemplo:
funcao(valor="nome", valor2="nome2)
Reduz a quantidade de problemas

Valores default

Ao escrever uma função, podemos definir um valor default para cara parâmetro. Ou seja, com um argumento
já especificado, o Python so vai perdir o outro argumento.

Chamadas de função equivalentes.

Valores de retorno
A funcção pode processasr alguns dados e então devolver um valor ou um conjunto de valores.

Devolvendo dicionários

Passando uma lista para uma função

Evitando que uma função modifique uma lista

Para isso, basta fazer uma copia da lista. Para enviar uma copia da lista para função, basta seguir o exem-
plo.

Exemplo:

nome_da_funcao(nome_da_lista[:])

A notação [:] cria uma cópia da lista para ser enviada à função.

Passando um número arbitrário de argumentos

*parametro

Adiciona vários argumentos.

O * Fala para o Python criar uma tupla vazia chamada toppings e reunir os valores recebidos nessa tupla.

Misturando argumentos posicionais e arbitrários

Para misturar uma função que aceite argumentos posicionais e arbitrários, os argumentos arbitrários
devem ser colocados no final da função.

Usando arugmentos nomeados arbitrários

usar **paramentro e usar um dicionário para adicionar os elementos

Armazenando funções em módulos
Armazenar funções em um arquivo separado permite ocultar os detalhes  do código de seu programa
e se concetrar na lógica de nível mais alto.

Criar as funções em arquivo separado. Para importar, bastar utilizar import nome_do_arquivo. Para utilizar as
funções do arquivo importado, bastar nome_do_arquivo.nome_funcap().

Importando funções específicas
from nome_do_arquivo import nome_funcao, nome_funcao2 ...

Com essa sintaxe, não é necessário colocar o nome do arquivo na hora de chamar a função
Exemplo: nome_funcao()

Usando a palavra reservada as para atribuir um alias a uma função
from nome_arquivo import nome_funcao as apelido
A palavra as da um "apelido", renomeia a função.

Usando a palavra reservada as para atribuir um alias a um módulo
import modulo as m

Importando todas as funções de um módulo
from nome_arquivo import *
"""
