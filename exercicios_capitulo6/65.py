# dictionary with three importants rivers

rivers = {'Amazonas': 'Brasil',
          'San Francisco': 'Eua',
          'Tamisa': 'England'}

for river, country in rivers.items():
    print(f'The {river} flows through {country}')

for river in rivers:
    print(river)

for country in rivers.values():
    print(country)
