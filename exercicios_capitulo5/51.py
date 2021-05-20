age = 18  #O livro pede para criar 5 condições falsas e 5 condições verdadeiras

if age == 18:
    print("You already have 18 years old.")

age = 17

if age != 18:
    print(("You havent 18 years old."))

list = ['parrot', 'dog', 'cat', 'fish']

if 'parrot' in list:
    print("MOM, I WANT A PARROT!!!!!")

if 'cockroach' not in list:
    print("UFAAA, I DIDNT WANT TO HAVE A COCKROACK TO BE MY PET")

x = int(input("Type a number: "))

if x == 42:
    print("This is the right number.")
else:
    print("You type the wrong number.")

tuple = (1, 2, 3, 4, 5, 6)

total = 0
total2 = 0

for values in tuple:
    if values % 2 == 0:
        total = total + values
    else:
        total2 = total2 + values

print(f'The total of even numbers in tuple is {total}.')
print(f'The total of odd numbers in tuple is {total2}.')

love = input("Do u love me?")

if love == 'yes':
    print("Will you marry me?")
else:
    print("Hello dark my old friend...")


