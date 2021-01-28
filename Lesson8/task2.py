# Задание 2

class ExByZero(Exception):
    pass

t = True
a = int(input())
try:
    if a == 0:
        raise ExByZero
except ExByZero as e:
    print('By zero!!!')
    t = False

if t:
    print(1/a)