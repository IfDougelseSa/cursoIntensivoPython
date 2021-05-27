# Cinema ticket

active = True


while active:
    age = int(input("Type your age: "))
    if age == 0:
        active = False
    elif age <= 3:
        print(f'You have free ticket')
    elif 4 <= age <= 12:
        print(f'Your ticket cost 10 bucks.')
    elif age > 12:
        print(f'Your ticket cost 15 bucks.')

