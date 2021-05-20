# Checking user name

current_users = ['doug', 'sa', 'di', 'gui', 'dani']
new_users = ['doug', 'sa', 'ines', 'bisa', 'snow']

for user in new_users:
    if user in current_users:
        print(f'The name was already used: {user.lower()}')
    else:
        print(f'You can use this name: {user.lower()}')


