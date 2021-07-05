# Sandwiches

sandwich_orders = ['bun kebab', 'chutney sandwich', 'croquette sando']
finished_sandwiches = []

while sandwich_orders:
    prepared_sandwich = sandwich_orders.pop()
    print(f'I have prepared your {prepared_sandwich}')
    finished_sandwiches.append(prepared_sandwich)
for finished_sandwich in finished_sandwiches:
    print(f'I did {finished_sandwich} sandwiche.')




