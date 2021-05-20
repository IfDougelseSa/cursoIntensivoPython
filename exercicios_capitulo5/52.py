# Test condicionais

name = input('Digite seu nome: ')
age = int(input('Type your age: '))

if age < 4:
    price = 0
elif age < 8:
    price = 5
elif age < 65:
    price = 10
else:
    price = 0

print(f'Hello Mr/Mrs {name}, you have to pay {price} bucks.')




