# Задание 2

n = int(input('Input number of list elements:'))
l = []
for i in range(n):
    e = input(f'{i+1}th element:')
    l.append(e)

for i in range(0, n, 2):
    if i < n - 1:
        l[i], l[i+1] = l[i+1], l[i]

print(l)