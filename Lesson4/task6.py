# Задание 6

from itertools import count
from itertools import cycle

def ints(a):
    i = count(a)
    b = next(i)
    while b < 10:
        yield b
        b = next(i)

print([a for a in ints(2)])

def list_cycle(l):
    i = cycle(l)
    ll = next(i)
    for j in range(10):
        yield ll
        ll = next(i)

print([e for e in list_cycle([1, 2, 3])])