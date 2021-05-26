# favorite language

favorite = {'Sabrina': 'Portuguese',
            'Douglas': 'English',
            'Diogo': '',
            'Guilherme': ''}
for name, language in favorite.items():
    if language == '':
        print(f'You need to answer the question {name}')
    else:
        print(f'Thanks to answer the question {name}')

