# Lista para usuários de um site
list = ['admin', 'douglas', 'sabrina', 'diogo', 'daniela']
if not list:
    print('A lista está vazia')
else:
    for user in list:
        if user == 'admin':
            print(f'Ola, {user}. O que gostaria de fazer?')
        else:
            print(f'Olá, {user}.')

