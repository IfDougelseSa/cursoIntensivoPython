pizzas = ["palmito", "calabresa", "frango"]


friend_pizzas = pizzas[:]
pizzas.append("queijo")
friend_pizzas.append("brocolis")



for pizza in pizzas:
    print(f"My favorite pizzas are {pizza}")


for pizza in friend_pizzas:
    print(f"My friends favorite pizzas are {pizza}")



