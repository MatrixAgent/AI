# Задание 5

with open("task5.txt", "w") as f:
    f.write("1 3 15 100 93 7")
s = 0
with open("task5.txt", "r") as f:
    l = f.readline().split()
    while l != []:
        for e in l:
            s += float(e)
        l = f.readline().split()
print(s)
