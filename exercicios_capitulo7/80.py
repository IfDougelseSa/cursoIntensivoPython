# Dream vacation!!

quiz = {}
active = True

while active:
    name = input("Type your name: ")
    place = input("Where will you gonna be ir your dream vacation? ")
    quiz[name] = place
    repeat = input("Would you like to let another person respond?(yes/no) ")
    if repeat == 'no':
        active = False
print(f'The quiz have been done!')
for name, place in quiz.items():
    print(f'{name} would like to go to {place}.')


