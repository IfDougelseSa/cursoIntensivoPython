# Ingredients for a pizza
ingredients = []
active = True


print(f'When you finish, type quite!!!!')


while active:
    new_ingredient = input("Type the ingredient: ")
    if new_ingredient == "quit":
        active = False
    else:
        ingredients.append(new_ingredient)
        print(f'The {new_ingredient} has been added!')
print(ingredients)

