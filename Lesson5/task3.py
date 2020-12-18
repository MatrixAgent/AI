# Задание 3

# Вопрос: если входной файл test.txt содержит русские буквы, то прграмма падает.
# Как это лечится?

with open("task3.txt", "r", encoding="utf-8") as f:
    l = f.readline().split()
    s = float(l[1])
    c = l == [] if 0 else 1
    while l != []:
        if float(l[1]) < 20000:
            print(l[0])
        s += float(l[1])
        l = f.readline().split()
        c += 1

print(f"Average salary: {s / c}")