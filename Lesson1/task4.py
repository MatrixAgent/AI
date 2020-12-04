# Задание 4

n = input('Figure: ')
i = 0
m = 0
while i < len(n):
    v = int(n[i])
    if v > m:
        m = v
    i += 1

print(m)
