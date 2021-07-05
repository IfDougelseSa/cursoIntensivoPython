# Sandwiches itens
def sandwiche_itens(*itens):
    for item in itens:
        print(f'You asked {item}')

print(f'Pedido 1: ')
sandwiche_itens("Bread", "Cheese", "Lettuce")
print(f'Pedido 2: ')
sandwiche_itens("bread", "hambuguer")
print(f'Pedido 3: ')
sandwiche_itens("Bread", "Cheese", "Tomato")


