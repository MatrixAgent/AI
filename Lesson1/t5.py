# Task 5

l = []
r = int(input())
while r != -1:
    i = 0
    for i in range(0, len(l) - 1):
        if r > l[i]:
            l.insert(i, r)
            break;
    if i == len(l):
        l.append(r)
    print(l)
    r = int(input())

