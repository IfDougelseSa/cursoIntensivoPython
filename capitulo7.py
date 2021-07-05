"""
Entrada de usuário e laços while


% O operador módulo informa o resto de uma divisão.

O laço for toma uma coleção de itens e executa um bloco de código uma vez para cada item da coleção.
Em comparação, o laço while executa durante o tempo em que, ou enquanto, uma determinada condição for
verdadeira.

Usando uma flag

Se muitos eventos possíveis puderem ocorrer para o programa terminar, tentar testar todas essas con-
dições em uma única instrução while torna-se difícil. Para isso é necessaŕio definir uma flag como True
se caso algum evento pare de funcionar a flag torna-se False e o programa sai do laço.

Usando break para sair do laço

Para sair de um laço, sem executar qualquer codigo restante, é utilizado o break.

Usando continue em um laço

Server para "ignorar" e voltar para o laço

Usando laços com listas e dicionários

Um laço for é eficiente para percorrer uma lista, mas não se deve modificar uma lista em um laço for,
pois o Python terá problemas para manter o controle da lista. Para modificar uma lista enquanto trabalha
com ela, é melhor utilizar o while.

Removendo todas as instâncias de valores específicos em uma lista

list = ['value', 'value']

while 'value' in list:
    list.remove('value')

Com isso, todos os valores value serão removidos da lista

Preenchendo um dicionário com dados de entrada do usuário

Exemplo:

Definir uma flag e um dicionario vazio. Depois, fazer perguntar para adicionar no dicionário e se quiser
encerrar o programar usar um if para mudar a flag para false.

responses = {}

active = True

name = input("Digite seu nome")
response = input("valor atribuido para a chave")

# Para armazenar no dicionário

responses[name] = response

"""
