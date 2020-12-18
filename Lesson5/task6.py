# Задание 6

def parseline(s):
    l = s.split()
    s = 0
    for i in range(1, len(l)):
        if l[i] != '—':
            t = l[i].partition('(')
            s += int(t[0])
    return (l[0].partition(':')[0], s)

with open("task6.txt", "r", encoding="utf-8") as f:
    l = f.readlines()
    d = {}
    for e in l:
        t = parseline(e)
        d[t[0]] = t[1]

print(d)