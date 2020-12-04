# Задание 5

revenue = float(input('Revenue: '))
cost = float(input('cost: '))

d = revenue - cost
if d > 0:
    print(f'Profit: {d}')
elif d < 0:
    print(f'Loss: {d}')
else:
    print('By zeros')

print(f'Profitability: {d / cost * 100}')

n = int(input('Number of employees: '))

print(d / n)
