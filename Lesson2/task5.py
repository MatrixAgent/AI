# Задание 5

l = [7, 5, 3, 3, 2]
r = int(input())
while r != -1:
    for i in range(0, len(l)):
        if r > l[i]:
            l.insert(i, r)
            break;
    if i == len(l) - 1:
        l.append(r)
    print(l)
    r = int(input())
