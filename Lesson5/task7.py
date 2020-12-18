# Задание 7

import json

with open("task7.txt", "r", encoding="utf-8") as f:
    s = f.readline()
    sum = 0
    n = 0
    d = {}
    while s != "":
        l = s.split()
        p = float(l[2]) - float(l[3])
        print(f"{l[1]} {l[0]}: profit = {p}")
        if p >= 0:
            sum += p
            n += 1
        d[l[0]] = p
        s = f.readline()
    sum /= n
    print(f"Average profit = {sum}")
    d1 = { "average_profit": sum }
    l = [ d, d1 ]

with open("task7out.txt", "w", encoding="utf-8") as f:
    json.dump(l, f)