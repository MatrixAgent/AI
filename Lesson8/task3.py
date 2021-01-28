# Задание 3

class NotInt(Exception):
    pass

l = []
s = ''
while True:
    s = input()
    if s == 'stop':
        break
    try:
        try:
            l.append(int(s))
        except:
            raise NotInt
    except NotInt:
        print('Not int!')

print(l)
