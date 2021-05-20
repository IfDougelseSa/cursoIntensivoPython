# Ordinal numbers

list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for value in list:
    if value == 1:
        print(f'{value}st')
    elif value == 2:
        print(f'{value}nd')
    elif value == 3:
        print(f'{value}rd')
    else:
        print(f'{value}th')
