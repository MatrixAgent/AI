# Задание 5

from functools import reduce

def mult(a, b):
    return a * b

l = [a for a in range(100, 1001) if a % 2 == 0]
print(reduce(mult, l))
