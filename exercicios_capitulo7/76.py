"""
active = True
while active:
    new_ingredient = input("Type the ingredient: ")
    if new_ingredient == "quit":
        active = False
    else:
        ingredients.append(new_ingredient)
        print(f'The {new_ingredient} has been added!')
print(ingredients)


ingredients = []
new_ingredient = ''
while new_ingredient != 'quit':
    new_ingredient = input("Type the ingredient: ")
    ingredients.append(new_ingredient)
    print(f'The {new_ingredient} has been added!')
print(ingredients)
"""

ingredients = []
new_ingredient = ''


print(f'When you finish, type quite!!!!')


while new_ingredient != 'quit':
    new_ingredient = input("Type the ingredient: ")
    if new_ingredient == "quit":
        break
    else:
        ingredients.append(new_ingredient)
        print(f'The {new_ingredient} has been added!')
print(ingredients)

