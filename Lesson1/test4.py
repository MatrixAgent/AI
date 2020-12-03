s = input('String: ')
l = s.split(' ')
for i, e in enumerate(l):
    print(f'{i + 1} - {e[:10]}')