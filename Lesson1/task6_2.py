# Алгоритмическое решение 6-ой задачи

a = int(input('a = '))
b = int(input('b = '))
q = 1.1

n = 1
while a < b:
    a *= q
    n += 1

print(n)
