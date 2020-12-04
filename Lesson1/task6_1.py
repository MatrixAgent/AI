# Это математическое решение 6-ой задачи

import math

b = int(input('a = ')) # a
r = int(input('b = ')) # b
q = 1.1
n = math.log(r / b, q) + 1

n1 = int(n)

if n1 != n:
    n1 += 1

print(n1)
