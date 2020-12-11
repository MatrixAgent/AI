# Задание 3

def my_func(a, b, c):
    if a >= b:
        s = a
        t = b
    else:
        s = b
        t = a
    if t >= c:
        s += t
    else:
        s += c

    return s

print(my_func(2, 1, 3))
