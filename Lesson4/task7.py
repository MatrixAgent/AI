# Задание 7

def fact(n):
    r = 1
    for i in range(n):
        r *= (i + 1)
        yield r

for i in fact(10):
    print(i)