# Task 6

n = int(input('Number of products: '))
i = 0
db = []
while i < n:
    no = int(input('Product number:'))
    name = input('Name: ')
    price = input('Price: ')
    number = input('Nomber of: ')
    unit = input('Unit: ')
    db.append((no, {'name': name, 'price': price, 'number': number, 'unit': unit}))
    i += 1

analytics = { 'name': [], 'price': [], 'number': [], 'unit': []}
for e in db:
    for v in e[1].items():
        analytics[v[0]].append(v[1])

print(analytics)