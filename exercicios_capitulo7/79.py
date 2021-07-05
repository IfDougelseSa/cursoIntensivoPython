# Sandwiches

sandwich_orders = ['bun kebab', 'pastrami','chutney sandwich', 'pastrami','croquette sando','pastrami']
finished_sandwiches = []
print(f'We dont have pastrami sandwichs today!!!')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print(sandwich_orders)

while sandwich_orders:
    prepared_sandwich = sandwich_orders.pop()
    print(f'I have prepared your {prepared_sandwich}')
    finished_sandwiches.append(prepared_sandwich)
for finished_sandwich in finished_sandwiches:
    print(f'I did {finished_sandwich} sandwiche.')